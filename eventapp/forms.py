from django import forms
from .models import Event, Profile, Categorie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'categories', 'description', 'venue', 'bookng_last_date', 'arrival_date', 'end_date']
        widgets = {
            'bookng_last_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        categories = forms.ModelMultipleChoiceField(
            queryset=Categorie.objects.all(),
            widget = forms.CheckboxSelectMultiple,
            required=True
        )

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
        fields = ['categories', 'description', 'bookng_last_date', 'arrival_date', 'end_date']
        widgets = {
            'bookng_last_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        categories = forms.ModelMultipleChoiceField(
            queryset=Categorie.objects.all(),
            widget = forms.CheckboxSelectMultiple,
            required=True
        )
        
class SerachForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Categorie.objects.all(), required=False)
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
        