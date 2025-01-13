from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegistrationForm(UserCreationForm):
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    gender = forms.ChoiceField(label='Пол', choices=User.gender.field.choices, required=False)
    city = forms.CharField(max_length=100, label='Город', required=False)
    avatar = forms.ImageField(label='Аватар', required=False)
    bio = forms.CharField(label='О себе', widget=forms.Textarea, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'birth_date', 'gender', 'city', 'avatar', 'bio')

class LoginForm(AuthenticationForm):
    pass # Используем стандартную форму аутентификации Django