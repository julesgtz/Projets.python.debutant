from django.shortcuts import render, redirect
from .forms import urlForms
from . import models
from django.http import Http404
import string
import random
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=="GET":
        form = urlForms
        return render(request, "webadmin/index.html", {"form": form})
    elif request.method=="POST":
        form = urlForms(request.POST)
        if form.is_valid():
            donnees = form.save(commit=False)
            try:
                short_url = models.url.objects.get(long_url=donnees.long_url)
                return render(request, "webadmin/index.html", {"url": short_url})
            except:
                short_url = "".join([random.choice(string.ascii_letters + string.digits) for n in range(5)])
                donnees.short_url = short_url
                donnees.save()
                return render(request, "webadmin/index.html", {"url": short_url})
        else:
            return render(request, "webadmin/index.html", {"form": form})
    else:
        raise Http404("Request method unavailable")


def redirect(request, short_url):
    if request.method == "GET":
        data = models.url.objects.get(short_url=short_url)
        return HttpResponseRedirect(data.long_url)
    else:
        return Http404

