from django.views.generic import ListView, DetailView
from world.models import World
# from django.shortcuts import render
from django.shortcuts import redirect


def random_world(request):
    world = World.objects.order_by('?').first()
    return redirect(world.get_absolute_url())


class WorldListView(ListView):
    model = World


class WikiListView(ListView):
    model = World
    template_name = 'world/wiki_list.html'


class WorldDetailView(DetailView):
    model = World
