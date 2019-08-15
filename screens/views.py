from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.utils.timezone import now
from .models import Location, Screen


def index(request):
    locations = Location.objects.all()
    context = {'locations': locations}
    return render(request, 'index.html', context)


def get_screens_by_location(request, slug):
    location = get_object_or_404(Location, slug=slug)
    current_datetime = now()
    screens = get_list_or_404(Screen,
                              location=location,
                              is_active=True,
                              start_date__lte=current_datetime,
                              due_date__gte=current_datetime)
    screen = None

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
        screen = screens[0]
        context = {'screen': screen,
                   'next_index': 1}

    if context:
        if screen.url[-4] == ".":
            type = 'image'
        else:
            type = 'video'

        context['type'] = type

    if request.GET.get('tv') and request.GET.get('tv') == "true":
        return render(request, 'tv.html', context)

    return render(request, 'screens.html', context)
