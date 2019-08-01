from django.shortcuts import render
from .models import Location


def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'index.html', context)
