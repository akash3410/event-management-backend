from django.shortcuts import render, redirect
from .models import Event, Booking
from .forms import AddEventForm, SignUpForm, EventUpdateForm, SerachForm, UpdateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    booked_events = list()
    events = Event.objects.all()
    if request.user.is_authenticated:
        booked_events = Booking.objects.filter(user=request.user).values_list('event_id', flat=True)
    forms = SerachForm()
    if request.method == "POST":
        forms = SerachForm(request.POST)
        if forms.is_valid():
            query = forms.cleaned_data.get('query')
            
            if query:
                events = Event.objects.filter(title__icontains=query)
                
    return render(request, 'eventapp/events.html', {'events': events, 'forms': forms, 'booked_events': booked_events})

@login_required
def add_events(request):
    if request.method == 'POST':
        forms = AddEventForm(request.POST)
        if forms.is_valid():
            event = forms.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('home_page')
    forms = AddEventForm()
    return render(request, "eventapp/add_events.html", {'forms': forms})

def registration(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            login(request, user)
            return redirect("profile")
        else:
            forms = SignUpForm(request.POST)
            return render(request, 'eventapp/registration.html', {'forms': forms})
    forms = SignUpForm()
    return render(request, 'eventapp/registration.html', {'forms': forms})

def signIn(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm(data=request.POST)
    return render(request, 'eventapp/loginview.html', {'forms': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You are successfully logged out!")
    return redirect("home_page")

@login_required
def profile_view(request):
    user = request.user
    events = Event.objects.filter(user=user)
    return render(request, "eventapp/profile.html", {'user': user, 'events': events})

@login_required
def update_event(request, event_id):
    try:
        event = Event.objects.filter(pk=event_id, user=request.user).first()
        if request.method == "POST":
            forms = EventUpdateForm(request.POST, instance=event)
            if forms.is_valid():
                forms.save()
                return redirect('profile')
        else:
            forms = EventUpdateForm(instance=event)
        return render(request, 'eventapp/update_event.html', {'forms': forms})
    except Event.DoesNotExist:
        return redirect('profile')

@login_required  
def delete_event(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
        return redirect("profile")
    except Event.DoesNotExist:
        return redirect("profile")
    
def event_details(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        return render(request, 'eventapp/event_details.html', {'event': event})
    except Event.DoesNotExist:
        return redirect('home_page')

@login_required
def user_update(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form.save()
            return redirect('profile')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'eventapp/userUpdateForm.html', {'form': form})

@login_required
def book_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        if event.available_seat > 0:
            if not Booking.objects.filter(user=request.user, event=event):
                Booking.objects.create(user=request.user, event=event)
                event.available_seat -= 1
                event.save()
        return redirect('home_page')
    return render(request, 'eventapp/booking.html', {'event': event})

@login_required
def bokked_events(request):
    user = request.user
    booked = Booking.objects.filter(user=user)
    return render(request, 'eventapp/booked_event.html', {'bookeds': booked})

@login_required
def cancel_booking(request, event_id):
    try:
        user = request.user
        event = Event.objects.get(id=event_id)
        booked = Booking.objects.get(event_id=event_id)
        event.available_seat += 1
        event.save()
        booked.delete()
        print(event)
        return redirect("home_page")
    except Event.DoesNotExist:
        return redirect("home_page")