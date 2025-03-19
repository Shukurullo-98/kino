from django import forms
from django.contrib.auth.models import User

from .models import Cinema, Comment, Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('title', 'context', 'photo', 'category', 'video')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Film nomi'
            }),

            'context': forms.Textarea(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Film xaqida'
            }),

            'photo': forms.FileInput(attrs={
                'class': 'form-control mt-2'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select mt-2'
            }),

            'video': forms.TextInput(attrs={
                'class': 'form-control mt-2',
                'placeholder': 'Film adresi'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Parol',
    }))


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Parol',
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Parolni tastiqlang',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ism',
    }))

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ism',
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Familya',
    }))

    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Pochta',
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control mt-3',
                'placeholder': 'Kommentariya',
                'rows': 7
            }),

        }


class EditAccountForm(forms.ModelForm):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': 150,
    }))

    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': 150,
    }))

    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': 150
    }))

    email = forms.EmailField(required=False, max_length=255, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'maxlength': 255,
    }))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditProfileForm(forms.ModelForm):
    photo = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
    }))
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'maxlength': '15',
    }))
    about_user = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3,
        'maxlength': 100,
    }))

    class Meta:
        model = Profile
        fields = ('photo', 'phone_number', 'about_user')