import profile
from django.db.models import Max
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, filters, status
from .models import Question, Answer, Upvote, Downvote, Comment, Tag
from .serializers import CommentSerializer, QuestionSerializer, AnswerSerializer, TagSerializer
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from lexquirynotifications.models import QuestionNotification, RecentQuestionNotification




 # Create your views here.


#QUESTIONS



class getQuestions(generics.ListAPIView):
    queryset = Question.objects.all().order_by('-_id')
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['question','country', 'state', 'city','askedAt']
    search_fields = ['question','country', 'state', 'city','askedAt']
 


class getUnansweredQuestions(generics.ListAPIView):
    queryset = Question.objects.all().filter(answer__isnull=True).order_by("-_id")
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['question','country', 'state', 'city','askedAt']
    search_fields = ['question','country', 'state', 'city','askedAt']
  


class getTopQuestions(generics.ListAPIView):
    queryset = Question.objects.all().annotate(Max('numAnswers')).order_by('-numAnswers')
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['question','country', 'state', 'city','askedAt']
    search_fields = ['question','country', 'state', 'city','askedAt']


class getRecentQuestions(generics.ListAPIView):
    year = datetime.now().year
    month = datetime.now().month
    queryset = Question.objects.all().filter(askedAt__year = year, askedAt__month=month).order_by("-_id")
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['question','country', 'state', 'city','askedAt']
    search_fields = ['question','country', 'state', 'city','askedAt']
  


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addQuestion(request):
    data = request.data 
    user = request.user   
    userQuestion = Question.objects.create(
        user = user,
        name = user.name,
        question = data['question'],
        country = data['country'],
        state = data['state'],
        city = data['city'],
        userImage = user.profile_pic
        
    )
    serializer = QuestionSerializer(userQuestion, many=False)
    recentQuestionsLength = len(RecentQuestionNotification.objects.all()) + 1
    RecentQuestionNotification.objects.create(
        question = userQuestion,
        text = f'There are {recentQuestionsLength} new questions you are competent to answer. Remember answering questions are a good way to to meet prospective clients and increase your impression.'
    )

    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateQuestion(request, pk):
    user = request.user
    question = Question.objects.get(_id=pk)
    data = request.data
    if data['question'] == '' and user == question.user:
        return Response('No question was updated', status=status.HTTP_400_BAD_REQUEST)
    elif user == question.user:
        question.question = data['question']
        question.save()
        serializer = QuestionSerializer(question, many=False)
        return Response(serializer.data)

    else:
        return Response('Access denied', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeQuestion(request,pk):
    user = request.user
    question = Question.objects.get(_id=pk)
    if user == question.user:
        question.delete()
        return Response('Question Deleted')
    else:
        return Response('Access denied', status=status.HTTP_400_BAD_REQUEST)



#ANSWERS

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAnswer(request,pk):
    data = request.data
    user = request.user
    question = Question.objects.get(_id=pk)
    answers = question.answer_set.all()

    if data['answer'] == '':
        return Response('No answer was added', status=status.HTTP_400_BAD_REQUEST)
    
    elif user != question.user:
        userAnswer = Answer.objects.create(
            user = user,
            name = user.name,
            userquestion = question,
            answer = data['answer'],
            upVotes = data['upvotes'],
            downVotes = data['downvotes'],
            comments = data['comments'],
            tags = data['tags'],
            userImage = user.profile_pic
            )
        question.numAnswers = len(answers)
        question.save()

        QuestionNotification.objects.create(
            question = question,
            text = f'{user.name} just answered your question',
            notificationImage = user.profile_pic
        )
        serializer = AnswerSerializer(userAnswer, many=False)
        return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateAnswer(request, pk):
    user = request.user
    answer = Answer.objects.get(_id=pk)
    data = request.data
    if data['answer'] == '' and user == answer.user:
        return Response('No answer was updated', status=status.HTTP_400_BAD_REQUEST)
    elif user == answer.user:
        answer.answer = data['answer']
        answer.save()
        serializer = AnswerSerializer(answer, many=False)
        return Response(serializer.data)

    else:
        return Response('Access denied', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeAnswer(request,pk):
    user = request.user
    answer = Answer.objects.get(_id=pk)
    if user == answer.user:
        answer.delete()
        return Response('Answer Deleted')
    else:
        return Response('Access Denied', status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUpvote(request, pk,qpk):
    user = request.user
    question = Question.objects.get(_id=qpk)
    answer = Answer.objects.get(_id=pk)
    
    data = request.data

    alreadyUpvoted = answer.upvote_set.filter(user=user).exists()
    alreadyDownvoted = answer.downvote_set.filter(user=user).exists()
    
    if alreadyUpvoted:
        upvote = Upvote.objects.get(user=user)
        upvote.delete()
        return Response('Upvote removed')

    elif not alreadyUpvoted and alreadyDownvoted:
        Upvote.objects.create(
            user = user,
            userquestion = question,
            name = user.name,
            answer = answer,
            votes = data['upvotes']

        )
        answer.downvote_set.filter(user=user).delete()
        votes = answer.downvote_set.all()
        answer.downVotes = len(votes)
        answer.save()

        return Response('Upvote Added')
        
        
    
    else:
        Upvote.objects.create(
            user = user,
            userquestion = question,
            name = user.name,
            answer = answer,
            votes = data['upvotes']

        )
        votes = answer.upvote_set.all()
        answer.upVotes = len(votes)
        answer.save()
    
    
    return Response('Upvote Added')



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addDownvote(request, pk,qpk):
    user = request.user
    question = Question.objects.get(_id=qpk)
    answer = Answer.objects.get(_id=pk)
    
    data = request.data

    alreadyDownvoted = answer.downvote_set.filter(user=user).exists()
    alreadyUpvoted = answer.upvote_set.filter(user=user).exists()
    
    if alreadyDownvoted:
        downvote = Downvote.objects.get(user=user)
        downvote.delete()
        return Response("Downvote removed")
    
    elif not alreadyDownvoted and alreadyUpvoted:
        Downvote.objects.create(
            user = user,
            userquestion = question,
            name = user.name,
            answer = answer,
            votes = data['downvotes']

        )
        answer.upvote_set.filter(user=user).delete()
        votes = answer.upvote_set.all()
        answer.upVotes = len(votes)
        answer.save()

        return Response('Downvote Added')
        
    else:
        Downvote.objects.create(
            user = user,
            userquestion = question,
            name = user.name,
            answer = answer,
            votes = data['downvotes']

        )
        votes = answer.downvote_set.all()
        
        answer.downVotes = len(votes)
        answer.save()
        
        return Response('Downvote Added')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addComment(request, pk, qpk):
    user = request.user
    answer = Answer.objects.get(_id=pk)
    question = Question.objects.get(_id=qpk)
    data = request.data

    if data['comment'] == '':
        return Response('No comment was added', status=status.HTTP_400_BAD_REQUEST)

    else:
        userComment = Comment.objects.create(
            user = user,
            name = user.name,
            userquestion = question,
            useranswer = answer,
            comment = data['comment'],
            userImage = user.profile_pic

    )

    serializer = CommentSerializer(userComment, many=False)
    return Response(serializer.data)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateComment(request, pk):
    user = request.user
    userComment = Comment.objects.get(_id=pk)
    data = request.data
    if data['comment'] == '' and user == userComment.user:
        return Response('No comment was updated', status=status.HTTP_400_BAD_REQUEST)
    elif user == userComment.user:
        userComment.comment = data['comment']
        userComment.save()
        serializer = CommentSerializer(userComment, many=False)
        return Response(serializer.data)

    else:
        return Response('Access denied', status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeComment(request,pk):
    user = request.user
    comment = Comment.objects.get(_id=pk)
    if user == comment.user:
        comment.delete()
        return Response('comment deleted')
    else:
        return Response ('Access Denied', status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET'])
def getTags(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)
