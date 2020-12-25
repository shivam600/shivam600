from django.shortcuts import render
from Quiz.models import Quiz
from Quiz.models import Quiz2 


def start_quiz(request):
	return render(request,'start_quiz.html')	


def quiz(request):
	questions = Quiz.objects.all()
	context = {'questions':questions}
	return render(request, 'quiz.html', context)

def quiz2(request):
	questions = Quiz2.objects.all()
	context = {'questions':questions}
	return render(request, 'quiz2.html', context)	



