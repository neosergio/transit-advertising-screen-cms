from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Location, Screen


def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'index.html', context)


def get_screens_by_location(request, slug):
    location = get_object_or_404(Location, slug=slug)
    screens = get_list_or_404(Screen, location=location, is_active=True)

    if request.GET.get('index'):
        index = int(request.GET.get('index'))
        if len(screens) <= index:
            screen = screens[0]
            next_index = 1
        else:
            screen = screens[index]
            next_index = index + 1

        context = {'screen': screen,
                   'next_index': next_index}
    else:
        context = {'screen': screens[0],
                   'next_index': 1}
    return render(request, 'screens.html', context)
