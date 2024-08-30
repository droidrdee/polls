from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.db.models import F
from .models import Question
from django.urls import reverse
from django.views import generic



class IndexView(generic.ListView):
    # latest_question_list = Question.objects.order_by("pub_date")[:5]
    # context = { "latest_question_list": latest_question_list, }
    # return render(request, "pol/index.html", context)
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    # try:
        # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "pol/detail.html", {"question": question})
    
    model = Question
    template_name = "polls/detail.html"



class ResultsView(generic.DetailView):
    # response = "You are looking at the result of question %s. "
    # return HttpResponse(response % question_id)
    #   question = get_object_or_404(Question, pk=question_id)
    #   return render(request, "pol/result.html", {"question": question})  
    
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selectec_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, 
            "pol/detail/html",
            {
                "question": question,
                "error_message": "You didn't selected a choice"
            },
        )    
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse("polls:results", arge=(question.id,)))    
    