from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = "__all__"


    def get_comments(self,obj):
        comments = reversed(obj.postcomment_set.all())
        serializer = PostCommentSerializer(comments, many=True)
        return serializer.data



class PostCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostComment
        fields = "__all__"