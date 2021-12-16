from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, EmailInput
from members.models import Customer, UserProgress, UserPicture
# from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


# class UserCustomerUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Customer
# 		fields = ['profile_photo']



class UserCreateForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2' )


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name')
		widgets = {
			'username':   TextInput(attrs={'class': 'form-control','placeholder': 'Қолданушы атауы',}),
			'email': 	  TextInput(attrs={'class': 'form-control','placeholder': 'почта',}),
			'first_name': TextInput(attrs={'class': 'form-control','placeholder': 'Есімі',}),
			'last_name':  TextInput(attrs={'class': 'form-control','placeholder': 'Тегі',}),
			}
class UserRegisterFinish(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class UserCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('user', 'birth_day', 'birth_mounth', 'birth_year')




class UserPictureUpdate(forms.ModelForm):
	class Meta:
		model = UserPicture
		fields = ('__all__')
		# exclude = ['user']
		 


class UserProgressSave(forms.ModelForm):
	class Meta:
		model = UserProgress
		fields = ('user', 'result_all', 'result_true', 'result_false', 'course', 'false_answers')