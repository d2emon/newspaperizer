from django.views.generic import TemplateView
from newspaperizer.settings import settings
from wiki import load_wiki
import os


class PageView(TemplateView):
    template_name = 'wiki/page.html'
    path = settings.get('wiki_root', "/wiki/mywiki")

    def get_children(self, path):
        try:
            items = next(os.walk(path))[1]
        except StopIteration:
            items = []
        items = list(filter(lambda f: not f.startswith('.') and not f.startswith('__'), items))
        return items

    def get_context_data(self, **kwargs):
        subpath = kwargs.get('path', '')
        if subpath:
            subpath = os.path.normpath(subpath) + '/'
        path = os.path.join(self.path, subpath)

        import logging
        logging.debug("%s::%s", path, subpath)
        context = super(PageView, self).get_context_data(**kwargs)
        context['children'] = [{"title": c, "path": "{}{}/".format(subpath, c)} for c in self.get_children(path)]
        context['path'] = subpath
        context['upper'] = os.path.join(subpath, '..')
        context['title'] = os.path.basename(os.path.normpath(path))
        context['content'] = load_wiki(path, attach="/web/wiki/mywiki/{}__attach/".format(subpath))
        return context
