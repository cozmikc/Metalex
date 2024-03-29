from django.contrib.auth import get_user_model
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser
from .models import Chamber, PracticeArea, Qualification, Contact, MemberReview, PaymentPlan
from .serializers import ChamberSerializer, PracticeAreaSerializer, QualificationSerializer, ContactSerializer
from django_filters.rest_framework import DjangoFilterBackend
from lexquirynotifications.models import PaymentPlanNotification
from datetime import datetime

# Create your views here





class searchMembersRoute(generics.ListAPIView):
    queryset = Chamber.objects.all().filter(is_verified=True)
    serializer_class = ChamberSerializer
    permission_class = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name','category', 'country', 'description', 'state', 'city']
    search_fields = ['name','category', 'country', 'description', 'state', 'city']

    # def get(self,request):
    #     user = request.user
    #     print(user)
    #     return user



# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def loggedOutMember(request,pk):
#     try:
#         member = Chamber.objects.get(member=pk)
#         member.online = False
#         member.save()
#         serializer = ChamberSerializer(member, many=False)
#         return Response(serializer.data)

#     except:
#         return Response("No such member!")



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMemberDetails(request,pk,category):
    member = Chamber.objects.get(_id=pk,category=category)
    serializer = ChamberSerializer(member, many=False)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRelatedMembers(request, pk,category):
    data = Chamber.objects.filter(category=category).exclude(_id=pk)
    serializer = ChamberSerializer(data, many=True)
    return Response(serializer.data)
    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def updateProfileImage(request,pk):
    user = request.user
    data = request.data
    memberData = Chamber.objects.get(_id=pk)
    scanFile = data['profileImage'].split('.')
    if user == memberData.member and (scanFile[1] == 'jpg' or scanFile[1] == 'png'):
        memberData.profile_image = data['profileImage']
        memberData.save()
    serializer = ChamberSerializer(memberData, many=False)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def updateBannerDetails(request,pk):
    user = request.user
    data = request.data
    memberData = Chamber.objects.get(_id=pk)
    if user == memberData.member:
        memberData.banner_image = data['bannerImage']
        memberData.experience = data['experience']
        memberData.website = data['website']
        memberData.save()
        return Response("Banner details updated successfully")
    else:
        return Response("Permission denied", status=status.HTTP_400_BAD_REQUEST)

    

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def updateMemberDescription(request,pk):
    chamberData = Chamber.objects.get(_id=pk)
    user = request.user
    data = request.data
    if user == chamberData.member:
        chamberData.description = data['description']
        chamberData.save()   
        serializer = ChamberSerializer(chamberData,many=False)
        return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMemberPracticeArea(request,pk):
    data = PracticeArea.objects.filter(member=pk)
    serializer = PracticeAreaSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMemberPracticeArea(request,pk):
    data = request.data
    user = request.user
    chamberData = Chamber.objects.get(_id=pk)
    if user == chamberData.member:
        memberArea = PracticeArea.objects.create(
            member = chamberData,
            name = chamberData.name,
            area = data['area']
            )
        serializer = PracticeAreaSerializer(memberArea, many=False)
        return Response(serializer.data)

    else:
        return Response('Permission denied!')

            
               
                
            
    
   


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeMemberPracticeArea(request,pk,sk):
    user = request.user
    member = PracticeArea.objects.filter(member=sk)
    memberArea = PracticeArea.objects.get(_id=pk)
    if str(member[0]) == str(user):
        memberArea.delete()
        return Response('Area Deleted')
    else:
        return Response('Permission Denied',  status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMemberQualification(request,pk):
    data = Qualification.objects.filter(member=pk)
    serializer = QualificationSerializer(data,many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMemberQualification(request,pk):
    data = request.data
    user = request.user
    chamberData = Chamber.objects.get(_id=pk)
    if user == chamberData.member:
        memberQualification = Qualification.objects.create(
            member = chamberData,
            name = chamberData.name,
            degree = data['degree'],
            educationInstitution = data['educationInstitution'],
            educationDate = data['educationDate'],
            membershipInstitution = data['membershipInstitution'],
            membershipPosition = data['membershipPosition'],
            membershipDate = data['membershipDate']
        )
    serializer = QualificationSerializer(memberQualification, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMemberQualification(request,pk,sk):
    user = request.user
    data = request.data
    member = Qualification.objects.filter(member=sk)
    memberQualification = Qualification.objects.get(_id=pk)
    if str(member[0]) == str(user):
        memberQualification.degree = data['degree']
        memberQualification.educationInstitution = data['educationInstitution']
        memberQualification.educationDate = data['educationDate']
        memberQualification.membershipInstitution = data['membershipInstitution']
        memberQualification.membershipPosition = data['membershipPosition']
        memberQualification.membershipDate = data['membershipDate']
        memberQualification.save()  
        serializer = QualificationSerializer(memberQualification, many=False)
        return Response(serializer.data)


   

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMemberContact(request,pk):
    data = Contact.objects.get(member=pk)
    serializer = ContactSerializer(data,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMemberContact(request,pk,sk):
    user = request.user
    data = request.data
    contactData = Contact.objects.get(_id=pk)
    chamberData = Chamber.objects.get(_id=sk)
    if str(user) == str(contactData.member):
        contactData.location = data['location']
        contactData.email = data['email']
        contactData.twitter = data['twitter']
        contactData.facebook = data['facebook']
        contactData.phone = data['phone']
        contactData.save()
        chamberData.phone = contactData.phone
        chamberData.save()
        serializer = ContactSerializer(contactData,many=False)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMemberReview(request,pk):
    user = request.user
    chamberData = Chamber.objects.get(_id=pk)
    data = request.data

    alreadyExists = chamberData.memberreview_set.filter(user=user).exists()

    if alreadyExists:
        content = {'detail':'Member already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif user == chamberData.member:
        content = {'detail':'Permission denied!'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)   

    elif int(data['rating']) <= 0 or int(data['rating']) > 5:
        content = {'detail':'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        MemberReview.objects.create(
            member = chamberData,
            user = user,
            username = user.name,
            rating = data['rating'],
            comment = data['comment']
    )

    reviews = chamberData.memberreview_set.all()
    chamberData.numReviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating
    chamberData.memberRating = total / len(reviews)
    chamberData.save()

    return Response('Review Added')


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMemberReview(request,pk,sk):
    user = request.user
    data = request.data
    chamberData = Chamber.objects.get(_id=sk)
    reviewData = MemberReview.objects.get(_id=pk)
    
    alreadyExists = chamberData.memberreview_set.filter(user=user).exists()

    if int(data['rating']) <= 0 or int(data['rating']) > 5:
        content = {'detail':'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif alreadyExists: 
        reviewData.comment = data['comment']
        reviewData.rating = data['rating']
        reviewData.save()
        

    reviews = chamberData.memberreview_set.all()
    chamberData.numReviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating
    chamberData.memberRating = total / len(reviews)
    chamberData.save()
    return Response('Review Updated')
   


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeMemberReview(request,pk,sk):
    user = request.user
    data = request.data
    chamberData = Chamber.objects.get(_id=sk)
    reviewData = MemberReview.objects.get(_id=pk)

    alreadyExists = chamberData.memberreview_set.filter(user=user).exists()

    if alreadyExists:
        reviewData.delete()

    reviews = chamberData.memberreview_set.all()
    chamberData.numReviews = len(reviews)
    chamberData.save()
    return Response('Review Removed')


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def memberPlan(request,pk):
    user = request.user
    data = request.data
    member = Chamber.objects.get(member=pk)
    if user == member.member and (member.lexerati or member.firm or member.elite_firm):
        return Response("You're on a plan already!")

    if user == member.member and member.is_lawyer and data['price'] == '30':
       member.lexerati = True
       member.save()
       PaymentPlan.objects.create(
           member = member,
           plan = "Lexerati"
       )
       PaymentPlanNotification.objects.create(
           member = member,
           plan = 'Lexerati',
           text = "you've been upgraded to the Lexerati plan"
       ) 
       return Response('LEXERATI PLAN SUCCESSFUL')

    if user == member.member and member.is_lawfirm and data['price'] == '50':
        member.firm = True
        member.save()
        PaymentPlan.objects.create(
           member = member,
           plan = "Firm"
           )
        PaymentPlanNotification.objects.create(
            member = member,
            plan = 'Firm',
            text = "you've been upgraded to the Firm plan"

        )
        return Response('FIRM PLAN SUCCESSFUL')

    if user == member.member and member.is_lawfirm and data['price'] == '150':
        member.elite_firm = True
        member.save()
        PaymentPlan.objects.create(
           member = member,
           plan = "Elitefirm"
           )
        PaymentPlanNotification.objects.create(
            member = member,
            plan = 'Elitefirm',
            text = "you've been upgraded to the Elitefirm plan"

        )
        return Response('ELITEFIRM PLAN SUCCESSFUL')

    else:
        return Response('Thank you for using this service :)')



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkPlan(request,pk):
    user = request.user
    member = PaymentPlan.objects.filter(member=pk).order_by("-_id")[0]
    print(member)
    print('i love')
    print('YOU')
 
    chamberMember = Chamber.objects.get(member=user)
    print(chamberMember, datetime.today(), member.paidAt)
    if str(user) == str(member.member): 
        purchaseDate = member.paidAt
        convertedFormat = datetime.strptime(str(datetime.date(purchaseDate)), "%Y-%m-%d").date()
        today = datetime.today().date()
        diff =  (today - convertedFormat).days

        if diff > 30 and chamberMember.lexerati:
            chamberMember.lexerati = False
            chamberMember.save()

            PaymentPlanNotification.objects.create(
            member = member.member,
            plan = 'Lexerati',
            text = "Your Lexerati plan has expired please purchase another plan to continue using this feature."   

        )

        if diff > 30 and chamberMember.firm:
            chamberMember.firm = False
            chamberMember.save()

            PaymentPlanNotification.objects.create(
            member = member.member,
            plan = 'Firm',
            text = "🤯Your Firm plan has expired please purchase another plan to continue using this feature."   

        )
        

        if diff > 30 and chamberMember.elite_firm:
            chamberMember.elite_firm = False
            chamberMember.save()

            PaymentPlanNotification.objects.create(
            member = member.member,
            plan = 'Elitefirm',
            text = "Your Elitefirm plan has expired please purchase another plan to continue using this feature."   

        )
            
        return Response([convertedFormat,  diff])
            
    else:
        return Response('No')


       


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def memberVerification(request):
    user = request.user
    data = request.data
    member = Chamber.objects.get(member=user)
    scanFile = str(data['file']).split(".")   
    if scanFile[1] == "pdf" or scanFile[1] == "doc":
        member.file = data['file']
        member.save()
        serializer = ChamberSerializer(member, many=False)
        return Response(serializer.data)
    else:
        return Response({"details": "File type not supported!"})