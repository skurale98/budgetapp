from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        if commit:
            user.save()

        return user

class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()