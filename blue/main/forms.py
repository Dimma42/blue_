from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import  User
#from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='username', help_text='maximum 150 characters', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')



class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')

    class Meta:
        #model = CustomUser
        model = User
        fields = UserCreationForm.Meta.fields + ('username',)
        field_classes = {'username': UsernameField}
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        if self.meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus']=True
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise form.ValidationError(
                self.error_message['password_mismath'],
                code='password_masmatch',
            )
        return password2