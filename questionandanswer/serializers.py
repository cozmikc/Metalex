from rest_framework import serializers
from .models import Question, Answer, Tag, Upvote, Downvote, Comment



class UpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upvote
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField(read_only=True)
    downvotes = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        fields = "__all__"

    def get_upvotes(self, obj):
        vote = obj.upvote_set.all()
        serializer = UpvoteSerializer(vote, many=True)
        return serializer.data

    def get_downvotes(self, obj):
        vote = obj.downvote_set.all()
        serializer = DownvoteSerializer(vote, many=True)
        return serializer.data
    
    def get_comments(self,obj):
        comment = reversed(obj.comment_set.all())
        serializer = CommentSerializer(comment, many=True)
        return serializer.data
    


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(read_only=True)
    upvotes = serializers.SerializerMethodField(read_only=True)
    downvotes = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    

    class Meta:
        model = Question
        fields = "__all__"

    

    def get_answers(self, obj):
        answers = reversed(obj.answer_set.all())
        serializer = AnswerSerializer(answers, many=True)
        return serializer.data   

    def get_upvotes(self, obj):
        vote = obj.upvote_set.all()
        serializer = UpvoteSerializer(vote, many=True)
        return serializer.data

    def get_downvotes(self, obj):
        vote = obj.downvote_set.all()
        serializer = DownvoteSerializer(vote, many=True)
        return serializer.data
    
    def get_comments(self,obj):
        comment = obj.comment_set.all()
        serializer = CommentSerializer(comment, many=True)
        return serializer.data 

  



class DownvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Downvote
        fields = "__all__"
 

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"



    


