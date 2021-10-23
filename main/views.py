from django.shortcuts import render
from django.views.generic import ListView
from .models import Question



class MainView(ListView):
	model = Question
	ordering = '-id'
	template_name = 'main/task.html'


'''

# |=================================|
# | Бұл код ақпараттарды 'data.txt' |
# | файлынан, 'db.sqlite3' файлына  |
# | жазу үшін қолданылды			|
# |=================================|


database = Question.objects.all()
# print(database)
class Data():
	answers = {}
	gh = 0
	bh = 0
	with open(r"D:\Django\tarih\project\main\data.txt" , encoding='utf-8') as f:

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