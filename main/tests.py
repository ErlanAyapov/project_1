from django.test import TestCase
from .models import Question

# Create your tests here.
database = Question.objects.all()
print(database)
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
		# database = Question(question = answers['task_' + str(bh)].split('\n'), answer = answers['answer_' + str(bh)].split('\n'))
		# database.save()
		# print(f'Ақпарат: {bh}, сәттті сақталды!')
		print(question = answers['task_' + str(bh)].split('\n'))