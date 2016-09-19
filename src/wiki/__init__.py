from django.utils.translation import ugettext_lazy as _


def load_wiki(path, title='', attach='__attach'):
    import re
    try:
        filename = "{}{}/__content.html".format(path, title)
        html = open(filename, 'r').read()
    except FileNotFoundError:
        html = ''

    found = re.search(r'<body>(.*)</body>', html, re.DOTALL)
    if not found:
        return _("Wiki {} not found. File {} is not exists.".format(title, filename))

    text = found.group(1)
    subs = re.sub(r'="__attach/(.*)"', r'="{}\1"'.format(attach), text)
    return subs
    print(subs)
    return text
