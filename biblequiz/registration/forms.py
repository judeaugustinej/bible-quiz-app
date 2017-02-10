from django import forms

from .models import Register


class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = Register
        fields = ('full_name', 
        	      'age',
        	      'language',
        	      'mobile_number',
        	      'email_id',
        	      'paid',)