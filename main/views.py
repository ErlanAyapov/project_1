from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DeleteView
from members.models import UserPicture
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post
import datetime


class PostDeleteView(DeleteView):
	model = Post
	template_name = 'main/post_delete.html'
	success_url = reverse_lazy('main')


class MainView(ListView):
	model = Post
	ordering = '-id'
	template_name = 'main/index.html'
	def get_context_data(self, **kwargs):
		context = super(MainView, self).get_context_data(**kwargs)
		context['user_pic'] = UserPicture.objects.order_by('-pk')

def main_view(request):
	post = Post.objects.order_by('-pk')
	user_pic = UserPicture.objects.order_by('-pk')

	data = {
		'posts':post,
		'user_pic':user_pic
	}
	return render(request, 'main/index.html', data)

def post_add(request):

	if request.method == 'POST':
		form = PostCreateForm(request.POST)

		if form.is_valid():
			form = form.save(commit = False)
			form.date = datetime.datetime.now()
			form.author = request.user
			form.save()
			return redirect('main')


	form = PostCreateForm()
	data = {
		'post_form':form,
	}
	return render(request, 'main/post_add.html', data)









# print(os.path.abspath(os.curdir))
'''

# |=================================|
# | Бұл код ақпараттарды 'data.txt' |
# | файлынан, 'db.sqlite3' файлына  |
# | жазу үшін қолданылды, толық 	|
# | ақпарат алу үшін +(747)816-04-85|
# |=================================|


database = Question.objects.all()
# print(database)
class Data():
	answers = {}
	gh = 0
	bh = 0
	with open(r"/app/main/data.txt" , encoding='utf-8') as f:

		for line in f:
			gh += 1

			if gh % 2 == 0:
				answers['answer_' + str(bh)] = line
				bh += 1
			else: 
				answers['task_' + str(bh)] = line

	bh = 0

	for obj in answers:
		bh += 1
		database = Question(
			question = str(answers['task_' + str(bh)].splitlines()).join(answers['task_' + str(bh)].splitlines()),
			answer = str(answers['answer_' + str(bh)].splitlines()).join(answers['answer_' + str(bh)].splitlines())

		)
		database.save()
		print(f'Ақпарат: {bh}, сәттті сақталды!')

		# print(answers['task_' + str(bh)].splitlines()).join(answers['task_' + str(bh)].splitlines())


'''