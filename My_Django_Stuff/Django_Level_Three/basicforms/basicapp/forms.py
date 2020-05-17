from django import  forms

from django.core import validators


def nameStartWith_Z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Please start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[nameStartWith_Z])
    #name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Re-nter dfd")
    text = forms.CharField()
    """
    botcathcer = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    """

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email must match")