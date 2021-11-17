from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserUpdateForm, UserCustomerForm, UserPictureUpdate, UserProgressSave
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout 
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.models import User
from .models import Customer, UserProgress, UserPicture
from django.shortcuts import get_object_or_404
import base64
from .models import *


def register(request):
	error = ''
	if request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST.get('username')  
			password = request.POST.get('password1')  
			user = authenticate(request, username = username, password = password)
			if user is not None: 
				login(request, user)
				return HttpResponseRedirect('/account/register/' + str(request.user.id))
				# return redirect('main')
		else:
			error = 'Пороли не совпадает или логин занят!'
			data = {
				'register_form':form,
				'message':error,
			}
			return render(request, 'members/register.html', data)
	else:
		form = UserCreateForm()
	return render(request, 'members/register.html', {'register_form':form})


def logout(request):
	django_logout(request)
	return redirect('main')


def authentication(request):
	error = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None: 
			login(request, user)
			return redirect('main')
		else:
			error = 'Логин және құпия сөз сәйкес емес немес сізде аккаунт жоқ!'
			return render(request, 'members/members.html', {'error':error})	
	return render(request, 'members/members.html')


def user_customer(request, pk):
	if request.method == 'POST':
		form = UserCustomerForm(request.POST)
		if form.is_valid():
			form.save(commit = False)
			form.user = request.user
			form.save()
			return redirect('main')
		 

	form = UserCustomerForm()
	data = {
		'customer_form':form,
		'day':range(1, 32, 1),
		'mounth':['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір', 'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қырқүйек', 'Қазан', 'Қараша', 'Желтоқсан'],
		'year':range(2013, 1970, -1),
	}
	return render(request, 'members/customer.html', data)


# def user_customer(request, pk):
# 	if request.method == 'POST':
# 		form = UserCustomerForm(request.POST)
# 		if form.is_valid():
# 			form.save(commit = False)
# 			form.user = request.user
# 			form.save()
# 			return redirect('main')
		 

# 	form = UserCustomerForm()
# 	data = {
# 		'customer_form':form,
# 		'day':range(1, 32, 1),
# 		'mounth':['Қаңтар', 'Ақпан', 'Наурыз', 'Сәуір', 'Мамыр', 'Маусым', 'Шілде', 'Тамыз', 'Қырқүйек', 'Қазан', 'Қараша', 'Желтоқсан'],
# 		'year':range(2013, 1970, -1),
# 	}
# 	return render(request, 'members/customer.html', data)


class UserProfile(DetailView):
	model = User
	template_name = 'members/profile.html'

	def get_context_data(self, **kwargs):
		context = super(UserProfile, self).get_context_data(**kwargs)
		context['last_progress'] = UserProgress.objects.all()
		context['user_profile'] = UserPicture.objects.order_by('-pk')
		# context['request_user'] = User.user.id

		return context


class UserUpdate(CreateView):
	model = UserPicture
	form_class = UserUpdateForm()
	template_name = 'members/user_update.html'
    # fields = ['title', 'slug', 'body', 'image']
	def form_valid(self, form):
		form.save()
		return redirect('main')



# class PictureUserUpdate(UpdateView):
	
# 	model = Customer
# 	# form_class = UserPictureUpdate()
# 	# slug_field = 'id'
# 	template_name = 'members/update_picture.html'

# 	fields = ['profile_photo', 'image']
# 	def form_valid(self, form):
# 		form.save()
# 		return redirect('main')
# 	def get_object(self, queryset=None):
# 		return get_object_or_404(Customer, pk=self.kwargs.get('pk'))

def pic_update(request, pk):
	if request.method == 'POST':
		form = UserPictureUpdate(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/account/profile/' + str(request.user.id))
		 

	form = UserPictureUpdate()
	data = {
		'form_picture':form,
		 
	}
	return render(request, 'members/update_picture.html', data)

def progress_save(request, pk):
	if request.method == 'POST':
		form = UserProgressSave(request.POST)
		if form.is_valid():
			form.save(commit = False)
			# form.user = request.user
			form.save()
			return redirect('main')
		 

	form = UserProgressSave()
	data = {
		'progress_save_form':form,
		 
	}
	return render(request, 'succes_pages/progress_save.html', data)


class UserList(ListView):
	model = User
	template_name = 'members/users.html'

	def get_context_data(self, **kwargs):
		context = super(UserList, self).get_context_data(**kwargs)
		context['user_profile'] = UserPicture.objects.order_by('-pk')
		return context