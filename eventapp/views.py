from django.shortcuts import render, redirect
from .models import Event
from .forms import AddEventForm, SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'eventapp/index.html')

def all_events(request):
    events = Event.objects.all()
    return render(request, "eventapp/events.html", {'events': events})

def add_events(request):
    if request.method == 'POST':
        forms = AddEventForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('all_events')
    forms = AddEventForm()
    return render(request, "eventapp/add_events.html", {'forms': forms})

def registration(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("home_page")
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
            return redirect("home_page")
        else:
            form = AuthenticationForm(data=request.POST)
            return render(request, 'eventapp/loginview.html', {'forms': form})
    form = AuthenticationForm()
    return render(request, 'eventapp/loginview.html', {'forms': form})
