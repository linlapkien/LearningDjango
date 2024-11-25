from django import forms

from core.models import Contact

# This is Contact form
class ContactForm(forms.ModelForm):
    
    email = forms.EmailField(max_length=255, required=True, widget = forms.EmailInput(attrs={"placeholder": "Email name", "class": "form-control"}))
    
    name = forms.CharField(max_length=255, required=True, widget = forms.TextInput(attrs={"placeholder": "Full name", "class":"form-control"}))
    
    telephone = forms.CharField(required=False, widget = forms.TextInput(attrs={"placeholder": "Phone number", "autocomplete": "off", "class": "form-control"}))
    
    message = forms.CharField(max_length=1000, required=True, widget = forms.Textarea(attrs={"placeholder": "Message"}))
    
    class Meta:
        model = Contact
        fields = ("name", "email", "telephone", "message")
    