from django.http import HttpResponse
from django.views.generic import TemplateView, RedirectView
from newspaperizer.settings import settings
from wiki import load_wiki
import os


class PageView(TemplateView):
    template_name = 'wiki/page.html'
    path = settings.get('wiki', dict()).get('wiki_root', "/wiki/mywiki")
    attach = settings.get('wiki', dict()).get('wiki_url', "/web/wiki/")

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

        context = super(PageView, self).get_context_data(**kwargs)
        context['children'] = [{"title": c, "path": "{}{}".format(subpath, c)} for c in self.get_children(path)]
        context['path'] = subpath
        context['upper'] = os.path.join(os.path.normpath(subpath), '..')
        context['title'] = os.path.basename(os.path.normpath(path))
        context['content'] = load_wiki(path, attach="{}{}__attach/".format(self.attach, subpath))
        return context


class AttachView(RedirectView):
    path = settings.get('wiki', dict()).get('wiki_url', "/web/wiki/")

    def get_redirect_url(self, *args, **kwargs):
        subpath = kwargs.get('path', '')
        filename = kwargs.get('file', '')
        return os.path.join(self.path, subpath, '__attach', filename)
