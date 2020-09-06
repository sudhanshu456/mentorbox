from django import forms

from accounts.models import CustomProfile

class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model=CustomProfile
        fields='__all__'
        exclude=['user']
	    