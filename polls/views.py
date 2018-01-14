from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Home Page
def home(request):
    template_name = 'polls/home.html'
    return render(request, 'polls/home.html')

# Gap Analysis Home
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

        resultset = {}

        for q in Question.objects.raw('select * from polls_question'):
            choicelist = []
            for c in Choice.objects.raw('select * from polls_choice where question_id=' + str(q.id)):
                choicelist.append(c)
                resultset[q]=choicelist

        return resultset


# DEPRECATED: Individual Question (Detail)
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# DEPRECATED: Poll Result
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# DEPRECATED: Vote Function
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))