from django.conf import settings
from django.shortcuts import render


ORG_URL = settings.ORG_URL
REDIRECT_APP_URL = settings.REDIRECT_APP_URL

c = {
    "org": ORG_URL,
    "embed_link": REDIRECT_APP_URL
}


def view_home(request):
    return render(request, 'index.html', c)

