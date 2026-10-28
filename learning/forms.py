from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class LabAnswerForm(forms.Form):
    answer = forms.CharField(
        max_length=160,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Type your answer",
                "autocomplete": "off",
                "aria-label": "Your answer",
            }
        ),
    )
