from .models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'password1', 'password2', 'profile_pic', 'first_name', 'last_name')
        widgets = {            
            'profile_pic': forms.FileInput(attrs={'class': 'form-control bg-info'}),
        } 

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('bio','profile_pic')
        widgets = {           
            'bio': forms.Textarea(attrs={'class': 'form-control bg-info', 'placeholder': 'Biography*'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control bg-info'}),
        }


        