import urllib
import hashlib

from django import template
from django.contrib.sites.models import Site

from condbox import settings

register = template.Library()


def gravatar_url(parser, token):
    try:
        tag_name, email = token.split_contents()

    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires 1 argument" % token.contents.split()[0]

    return GravatarNode(email)


class GravatarNode(template.Node):
    def __init__(self, email):
        self.email = template.Variable(email)

    def render(self, context):
        try:
            email = self.email.resolve(context)
        except template.VariableDoesNotExist:
            return ''

        site = Site.objects.get_current()

        default = "http://%s%simg/avatar.png" % (site.domain, settings.STATIC_URL)
        print default
        size = settings.GRAVATAR_SIZE

        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d': default, 's': str(size)})

        return gravatar_url

register.tag('gravatar', gravatar_url)
