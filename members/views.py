from django.shortcuts import render, redirect
from .forms import  UserRegisterFinish, UserCreateForm, UserUpdateForm, UserCustomerForm, UserPictureUpdate, UserProgressSave
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as django_logout 
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from .models import Customer, UserProgress, UserPicture
from django.shortcuts import get_object_or_404
import base64
from .models import *
from main.models import Post
# from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory


class DeletePostView(DeleteView):
	model = UserPicture
	template_name = 'delete_image.html'
	success_url = HttpResponseRedirect('/')

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


class UserRegisterFinishView(UpdateView):
	model = User
	form_class = UserRegisterFinish
	template_name = 'members/input_name.html'
	
	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect('/account/picture/' + str(self.request.user.id))

def register(request):
	global request_user
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
				request_user = request.user.id
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
			request_user = request.user.id
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
			return HttpResponseRedirect('/account/register/continue/' + str(request.user.id))
		 

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

	def get_context_data(self, **kwargs):
		context = super(UserProfile, self).get_context_data(**kwargs)
		context['last_progress'] = UserProgress.objects.all()
		context['posts'] = Post.objects.all()
		context['user_profile'] = UserPicture.objects.order_by('-pk')

		return context


class UserProgressDetail(DetailView):
	model = UserProgress
	template_name = 'members/progress_res.html'



class UserUpdate(CreateView):
	model = UserPicture
	form_class = UserUpdateForm()
	template_name = 'members/user_update.html'
    # fields = ['title', 'slug', 'body', 'image']
	def form_valid(self, form):
		form.save()
		return redirect('main')



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

class CustomeUpdateView(UpdateView):
    model = UserPicture
    form_class = UserPictureUpdate
    template_name = 'pict/picture_update.html'
     
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(f'/account/profile/{ self.request.user.id}/')



# class UpdateCustomerView(UpdateWithInlinesView):
#     model = Customer
#     inlines = [User]
#     fields = ['profile_photo', 'user']
#     template_name = 'members/user_update.html'

# class UserCustomerUpdateView(UpdateView):
# 	model = Customer
# 	form_class = UserCustomerUpdateForm
# 	template_name = 'members/user_update.html'
	
# 	def form_valid(self, form):
# 		form.save()
# 		return HttpResponseRedirect('/')