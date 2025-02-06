from django import forms
from .models import Profile

#Form for editing Profile, showing all model fields except user
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']