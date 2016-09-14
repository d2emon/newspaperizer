from django.views.generic import ListView, DetailView, TemplateView
from world.models import World
# from django.shortcuts import render
from django.shortcuts import redirect


def random_world(request):
    world = World.objects.order_by('?').first()
    return redirect(world.get_absolute_url())


class OrphanView(TemplateView):
    template_name = 'world/orphans_list.html'
    path = "../media/worlds"

    def get_orphans(self):
        import os
        try:
            items = next(os.walk(self.path))[1]
        except StopIteration:
            items = []
        items = list(filter(lambda f: not f.startswith('.') and not f.startswith('__') and not World.objects.filter(title=f).exists(), items))
        return items

    def get_context_data(self, **kwargs):
        context = super(OrphanView, self).get_context_data(**kwargs)
        context['orphans'] = self.get_orphans()
        return context


class WorldListView(ListView):
    model = World


class WikiListView(ListView):
    model = World
    template_name = 'world/wiki_list.html'


class WorldDetailView(DetailView):
    model = World
