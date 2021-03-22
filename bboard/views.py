from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Bb, Rubric

# Create your views here.
def index(request):
    return render(request, 'bboard/index.html')

class BbListView(ListView):
    model = Bb
    template_name = 'bboard/bb/list.html'