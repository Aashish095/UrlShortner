from django.shortcuts import render,redirect
from .models import short_urls
from .form import UrlForm
from .shortend import shortner



def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token).first()
    return redirect(long_url.long_url)


def Make(request):
    form = UrlForm(request.POST)
    a = ''
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortner().issue_token()
            NewUrl.short_url = a
            NewUrl.link = "http://127.0.0.1:8000/" + a
            NewUrl.save()

        else:
            form = UrlForm()
            a = "Invalid Url"

    new_url = "http://127.0.0.1:8000/" + a

    return render(request,'home.html',{'form':form,'new_url':new_url})
