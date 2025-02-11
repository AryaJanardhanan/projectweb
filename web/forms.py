from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#django Forms
class EnquiryForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label ='Email')
    message = forms.CharField(label='Your msg', widget=forms.Textarea)


#Model forms
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age','ad_num', 'department']


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'image', 'fl']       

