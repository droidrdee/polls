from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    context = { "latest_question_list": latest_question_list, }
    return render(request, "pol/index.html", context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise


def results(request, question_id):
    response = "You are looking at the result of question %s. "
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting on question %s. " % question_id) 