from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Day, Option, Rating

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_lunch_list'

    def get_queryset(self):
        """Return the 4 most recently published lunch days."""
        return Day.objects.filter(
            date__lte=timezone.now()
        ).order_by('-date')[:4]

class PastView(generic.ListView):
    template_name = 'polls/past.html'
    context_object_name = 'latest_lunch_list'
    paginate_by = 6
    model = Day

    def get_queryset(self):
        """Return all the published lunch days."""
        return Day.objects.filter(
            date__lte=timezone.now()
        ).order_by('-date')

class ResultsView(generic.DetailView):
    model = Day
    template_name = 'polls/results.html'

def vote(request, day_id):
    day = get_object_or_404(Day, pk=day_id)
    try:
        selected_option = day.option_set.get(pk=request.POST['option'])
        rating_num = request.POST['rating']
    except (KeyError, Option.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'option': option,
            'error_message': "You didn't select an option or rating.",
        })
    else:
        rating_obj = Rating.objects.create(option=selected_option, rating=rating_num)
        rating_obj.save()
        return HttpResponseRedirect(reverse('polls:results', args=(day.id,)))

