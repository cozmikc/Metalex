from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes, permission_classes
from .models import *
from .serializers import SubscriberSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import FormParser, MultiPartParser
from django.conf import settings
import requests




# Create your views here.

URL = settings.MAILCHIMP_URL
KEY = settings.MAILCHIMP_KEY

@api_view(['POST'])
def addSubscriber(request):
    data = request.data
    postEmail = data['email']
    scanEmail = str(postEmail).split('.')
    alreadyExists = Subscriber.objects.filter(email=postEmail).exists()
    if alreadyExists:
        return Response({"detail":"Email already subscribed"}, status=status.HTTP_400_BAD_REQUEST) 
    if scanEmail != "" and scanEmail[1] == "com":
        try:
            embed_url = URL+'/lists/9ec6176ece'
            data = {
            'members':[
                {'email_address': postEmail,
                'status':'subscribed',
                'merger_fields':{
                    'FNAME':'',
                    'LNAME':''}}]}
            headers = {
                'Accept':'application/json',
                'Content-type':'application/json',
                'Authorization': 'auth '+KEY
                }
            response = requests.post(embed_url, json=data, headers=headers)

            if response.status_code == 200 or response.status_code == 201:
                newSubscriber = Subscriber.objects.create(email = postEmail )
                SubscriberSerializer(newSubscriber, many=False)
                return Response({'detail':'Thank you for subscribing'})


        except requests.RequestException:
            return Response({'detail':'Something went wrong try again!'})


    else:
        return Response('Invalid request!')

                

            
        


            




# @api_view(["POST"])
# @permission_classes([IsAuthenticated, IsAdminUser])
# @parser_classes([MultiPartParser, FormParser])
# def sendEmail(request):
#     data = request.data
#     mail = Mail.objects.create(
#         title = data['title'],
#         body = data['body']
#     )

#     serializer = MailSerializer(mail, many=False)
#     return Response(serializer.data)

    

    
