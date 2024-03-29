from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from .models import LawyerNotification, QuestionNotification, PaymentPlanNotification
from chamber.models import Chamber
from questionandanswer.models import Question
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serilaizers import *

# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getLawyerNotifications(request):
    user = request.user
    try:
        member = Chamber.objects.get(member=user)
        notifications = LawyerNotification.objects.filter(user=member)
        serializer = LawyerNotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    except:
        return Response([])
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeLawyerNotifications(request):
    user = request.user
    try:
        member = Chamber.objects.get(member=user)
        alreadyExists = LawyerNotification.objects.filter(user=member).exists()
        if alreadyExists:
            notifications = LawyerNotification.objects.filter(user=member)
            notifications.delete()
            return Response("Notification removed")
    except:
        return Response([])



@api_view(['GET']) 
@permission_classes([IsAuthenticated])
def getPlanNotifications(request):
    user = request.user
    try:
        member = Chamber.objects.get(member=user)
        notifications = PaymentPlanNotification.objects.filter(member=member)
        serializer = PaymentPlanNotificationSerializer(notifications, many=True)
        return Response(serializer.data)

    except:
        return Response([])




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removePlanNotifications(request):
    user = request.user
    try:
        member = Chamber.objects.get(member=user)
        alreadyExists = PaymentPlanNotification.objects.filter(member=member).exists()
        if alreadyExists:
            notifications = PaymentPlanNotification.objects.filter(member=member)
            notifications.delete()
            return Response("Notification removed")
    except:
        return Response([])

    finally:
        return Response('No notification found!')





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getQuestionNotifications(request,pk):
    try:
        question = Question.objects.filter(user=pk).filter(user=pk)
        notifications = QuestionNotification.objects.filter(question__in=question)
        serializer = QuestionNotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    except:
        return Response([])



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRecentQuestionNotifications(request,pk):
    try:
        question = Question.objects.filter(user=pk).filter(user=pk)
            
        notifications = RecentQuestionNotification.objects.filter(question__in=question)

        serializer = RecentQuestionNotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    except:
        return Response([])
    

   


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeQuestionNotifications(request,pk):
    try:
        question = Question.objects.filter(user=pk).filter(user=pk)
        alreadyExists = QuestionNotification.objects.filter(question__in=question).exists() 
        if alreadyExists:
            notifications = QuestionNotification.objects.filter(question__in=question)
            notifications.delete()
            return Response('Notifications removed')
    except:
        return Response([])

    finally:
        return Response('No notifications found!')



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeRecentQuestionNotifications(request,pk):
    try:
        question = Question.objects.filter(user=pk).filter(user=pk)
        alreadyExists = RecentQuestionNotification.objects.filter(question__in=question).exists() 
        if alreadyExists:
            notifications = RecentQuestionNotification.objects.filter(question__in=question)
            notifications.delete()
            return Response('Notifications removed')
    except:
        return Response([])

    finally:
        return Response('No notification found!')



    


    
   
