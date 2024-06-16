# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['role'] == 'Admin':
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user
