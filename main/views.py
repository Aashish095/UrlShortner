from django.shortcuts import render,redirect
from .models import short_urls
from .form import UrlForm
from .shortend import shortner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer


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

@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'list':'/task-list/',
        'Detail views':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk/',
        'Delete':'/task-delete/<str:pk/',
    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    url=short_urls.objects.all()
    serializer = TaskSerializer(url,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    url=short_urls.objects.get(id=pk)
    serializer = TaskSerializer(url,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    url=short_urls.objects.get(id=pk)
    serializer = TaskSerializer(instance=url,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    url=short_urls.objects.get(id=pk)
    url.delete()

    return Response('item successfully delete')
    
