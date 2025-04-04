from django import forms
from django.core import validators


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(
        label="Enter your email again",
        validators=[validators.EmailValidator()])
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        label="Leave this field empty",
        validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("Make sure emails match")

        return all_clean_data
