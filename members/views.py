from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserUpdateForm, UserCustomerForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout 
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.models import User
from .models import Customer


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
				return HttpResponseRedirect('/аккаунт/тіркеу/' + str(request.user.id))
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


class UserProfile(DetailView):
	model = User
	template_name = 'members/profile.html'


class UserUpdate(UpdateView):
	model = User
	form_class = UserUpdateForm
	template_name = 'members/user_update.html'
    # fields = ['title', 'slug', 'body', 'image']
	def form_valid(self, form):
		form.save()
		return redirect('main')