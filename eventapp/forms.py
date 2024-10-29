from django import forms
from .models import Event, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'venue', 'bookng_last_date', 'arrival_date', 'end_date']
        widgets = {
            'bookng_last_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'phone']
        
class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description', 'bookng_last_date', 'arrival_date', 'end_date']
        widgets = {
            'bookng_last_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
class SerachForm(forms.Form):
    query = forms.CharField(
        label="",
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': "Enter Event's Name...", 
            'class': "form-control rounded-2 col-8"
        })
    )
    
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        