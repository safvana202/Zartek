import imp

from yaml import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from zartekApp.models import Posts,PostImage
from .serializers import PostsSerializer,likeSerializer


@api_view(['GET'])
def  getPosts(request):
    datas=PostImage.objects.all()
    serializer  = PostsSerializer(datas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def  addlikes(request):
    serializer = likeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)