from urllib import request
from rest_framework import generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import PostSerializer, PostCommentSerializer




# Create your views here.



class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'body']
    search_fields = ['title', 'body']


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addPostComment(request,pk):
    user = request.user
    data = request.data
    post = Post.objects.get(_id=pk)
    if data['comment'] != "":
        userComment = PostComment.objects.create(
            post = post,
            name = user.name,
            user = user,
            userImage = user.profile_pic,
            comment = data['comment']
    )
    serializer = PostCommentSerializer(userComment, many=False)
    return Response(serializer.data)
    


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updatePostComment(request,pk):
    user = request.user
    data = request.data
    userComment = PostComment.objects.get(_id=pk)
    if user == userComment.user and data['comment'] != "":
        userComment.comment = data['comment']
        userComment.save()
        serializer = PostCommentSerializer(userComment, many=False)
        return Response(serializer.data)


@api_view(['DELETE'])
def removePostComment(request,pk):
    user = request.user
    data = request.data
    userComment = PostComment.objects.get(_id=pk)
    if user == userComment.user:
        userComment.delete()
        return Response('Comment deleted')
    else:
        return Response('Access Denied', status=status.HTTP_400_BAD_REQUEST)
    
    