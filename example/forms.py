from django import forms

class CapturePhoneNumbers(forms.Form):
	phone_numbers = forms.CharField(label="phone_numbers")