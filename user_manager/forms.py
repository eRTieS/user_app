from django import forms

from user_manager.helpers import email_validator, phone_validator


class NewUserForm(forms.Form):

    def __init__(self, request=None, *args, **kwargs):

        self.request = request
        self.user_cache = None

        super(NewUserForm, self).__init__(*args, **kwargs)

        for field in (self.fields['email'], self.fields['phone']):
            field.widget.attrs.update({'class': 'form-control '})

    name = forms.CharField(
        required=True,
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "names",
                "placeholder": "Enter name",
                "required data-error": "#name_error",
                "data-msg": "Required field!"
            }
        ),
        error_messages={"required": "The field is required!"}
    )

    phone = forms.CharField(
        required=True,
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "phone",
                "placeholder": "Enter phone number",
                "required data-error": "#phone_error",
                "data-msg": "Required field!"
            }
        ),
        error_messages={"required": "The field is required!"},
        validators=[phone_validator]
    )

    email = forms.EmailField(
        required=True,
        label='',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter email",
                "data-error": "#email_error",
                "data-msg": "Required field!",
                "data-email": "Enter valid email!"
            }
        ),
        error_messages={"invalid": "Enter valid email!"},
        validators=[email_validator]
    )
