from django.shortcuts import render
from .models import Event
# Create your views here.


def index(request):
    events = Event.objects.filter().order_by('start')
    return render(request, 'index.html', {'events': events})