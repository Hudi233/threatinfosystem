# -*- coding: utf-8 -*-

from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Choice
from .models import Question
from django.template import loader
# Create your views here.


def index(request):
    	latest_question_list = Question.objects.order_by('-pub_date')[:5]
    	template = loader.get_template('polls/index.html')
    	context = {
        	'latest_question_list': latest_question_list,
    	}
    	return HttpResponse(template.render(context, request))


def detail(request, question_id):
    	question = get_object_or_404(Question, pk=question_id)
    	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    	question = get_object_or_404(Question, pk=question_id)
    	return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    	question = get_object_or_404(Question, pk=question_id)
    	try:
        	selected_choice = question.choice_set.get(pk=request.POST['choice'])
    	except (KeyError, Choice.DoesNotExist):
        	return render(request, 'polls/detail.html', {
			'question': question,
            		'error_message': "You didn't select a choice.",
        	})
    	else:
        	selected_choice.votes += 1
        	selected_choice.save()
        	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
