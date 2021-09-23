from django.shortcuts import render,redirect
from main.models import short_urls
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializer import TaskSerializer

# Create your views here.
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
    
