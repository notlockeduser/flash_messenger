from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import Form
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username' , 'email', 'password1', 'password2']

class InputForm(Form):
	username = forms.CharField(max_length=100)
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)
	age = forms.IntegerField()
	job = forms.CharField(max_length=200)


class SearchForm(Form):
	search = forms.CharField(max_length=100)
