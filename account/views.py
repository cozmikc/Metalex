from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from chamber.models import Chamber, Contact
from chamber.serializers import ChamberSerializer





User = get_user_model()
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # Add custom claims
#         token['name'] = user.email
        # ...

        return token
    
    def validate(self,attrs):   
        data = super().validate(attrs)
        loggedMember = User.objects.get(email = attrs.get('email'))
        try:
            member = Chamber.objects.get(member=loggedMember)
            member.online = True
            member.save()

           
        except:
            print("Not in chamber")


        serializer = UserSerializerWithToken(self.user).data 
        for k,v in serializer.items():
            data[k]= v
        
        return data
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 


@api_view(['POST'])
def registerUser(request):
    data = request.data
    user = User.objects.create(
    name = data['name'],
    email = data['email'],
    phone = data['phone'],
    country = data['country'],
    state = data['state'],
    city = data['city'],
    is_lawyer = data['is_lawyer'],
    is_client = data['is_client'],
    is_lawfirm = data['is_lawfirm'],
    is_lawstudent = data['is_lawstudent'],
    password = make_password(data['password'])
    )
    serializer = UserSerializerWithToken(user, many=False)

    newUser = User.objects.get(id=user.id)
    if newUser.is_lawyer == True:
        Chamber.objects.create(
            member = newUser,
            name = newUser.name,
            country = newUser.country,
            state = newUser.state,
            city = newUser.city,
            phone = newUser.phone,
            is_lawyer = newUser.is_lawyer)
        newChamberMember = Chamber.objects.get(member=user.id)
        Contact.objects.create(
            member = newChamberMember,
            name = newChamberMember.name,
            phone = newChamberMember.phone,
            email = newUser.email
        )
            
        return Response(serializer.data)    
        
    elif User.objects.get(id=user.id).is_lawfirm == True:
        Chamber.objects.create(
            member = newUser,
            name = newUser.name,
            country = newUser.country,
            state = newUser.state,
            city = newUser.city,
            phone = newUser.phone,
            is_lawfirm = newUser.is_lawfirm)

        newChamberMember = Chamber.objects.get(member=user.id)
        Contact.objects.create(
            member = newChamberMember,
            name = newChamberMember.name,
            phone = newChamberMember.phone,
            email = newUser.email
        )
        return Response(serializer.data)

    else:
        return Response(serializer.data)




@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def updateUserProfile(request):
    user  = request.user
    serializer = UserSerializerWithToken(user, many=False)
    data = request.data
    user.name = data['name']
    user.email = data['email']
    user.phone = data['phone']
    user.country = data['country']
    user.state = data['state']
    user.city = data['city']
    user.profile_pic = data['profile_pic']

    print(data['profile_pic'])

    if data['profile_pic'] == 'null' or data['profile_pic'] == "":
        print(data['profile_pic'])
        user.profile_pic = user.profile_pic
    
    if data['password'] != '':
        user.password = make_password(data['password'])
    user.save()


    print(serializer.error_messages)


    
    if user.is_lawyer == True or user.is_lawfirm == True:
        data = Chamber.objects.get(member=user)
        data.name = user.name
        data.email = user.email
        data.country = user.country
        data.state = user.state
        data.city = user.city
        data.save()

    print(serializer.error_messages)

    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user  = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)




@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUserProfile(request,pk):
    user  = User.objects.get(id=pk)
    user.delete()
    return Response('User deleted')


@api_view(['PATCH'])
def loggedOutMember(request,pk):
    try:
        member = Chamber.objects.get(member=pk)
        member.online = False
        member.save()
        serializer = ChamberSerializer(member, many=False)
        return Response(serializer.data)
        
    except:
        return Response("No such member!")


