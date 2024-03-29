from urllib import response
from rest_framework import generics, filters, status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from .models import LawBook, Review
from .serializers import LawBookSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from chamber.models import Chamber



# Create your views here.



class LawbookRoute(generics.ListAPIView):
    queryset = LawBook.objects.all().order_by('-_id')
    serializer_class = LawBookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'category', 'author', 'description','country', 'language']
    search_fields = ['title', 'category', 'author', 'description','country', 'language']
    # pagination_class = Lawbookpagination.BookResultsSetPagination
   



@api_view(['GET'])
def getbookcontentRoute(request,pk,category):
    book = LawBook.objects.get(_id=pk, category=category)
    serializer = LawBookSerializer(book, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def addLawBook(request):
    user = request.user
    data = request.data
    member = Chamber.objects.get(member=user)
    scanFile = str(data['file']).split('.')
    scanImage = str(data['coverImage']).split('.')

    if data['file'] == '':
        return Response({'detail':'No book added'},  status=status.HTTP_400_BAD_REQUEST)

    elif data['coverImage'] == '':
        return Response({'detail':'No coverimage added'},  status=status.HTTP_400_BAD_REQUEST)

    
    elif scanFile[1] not in ['pdf', 'doc']:
        return Response({'detail':'File type not supported!'}, status=status.HTTP_400_BAD_REQUEST)
    
    elif scanImage[1] not in ['png', 'jpg']:
        return Response({'detail':'Image type not supported!'}, status=status.HTTP_400_BAD_REQUEST)


    elif member.lexerati  or member.firm or member.elite_firm:
        userBook = LawBook.objects.create(
            user = user,
            title = data['title'],
            coverImage = data['coverImage'],
            file = data['file'],
            description = data['description'],
            category = data['category'],
            country = data['country'],
            language = data['language'],
            author = data['author'],
            price = data['price']
            )    
        serializer = LawBookSerializer(userBook, many=False)
        return Response(serializer.data)

    else:
        return Response ({'detail':'Permission denied!'})

    
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addReview(request,pk):
    user = request.user
    book = LawBook.objects.get(_id=pk)
    data = request.data
    
    alreadyExists = book.review_set.filter(user=user).exists()

    if alreadyExists:
        content = {'detail':'Book already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif int(data['rating']) <= 0 or int(data['rating']) > 5:
        content = {'detail':'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif user == book.user:
        return Response({'detail':'Permission denied!'})
    
    else:
        Review.objects.create(
            user = user,
            book = book,
            name = user.name,
            rating = data['rating'],
            comment = data['comment']
    )

    reviews = book.review_set.all()
    book.numReviews = len(reviews)

    total = 0
    for i in reviews:
        total += i.rating
    book.rating = total / len(reviews)
    book.save()

    return Response('Review Added')




@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateBookReview(request,pk,sk):
    user = request.user
    data = request.data
    book = LawBook.objects.get(_id=sk)
    reviewData = Review.objects.get(_id=pk)

    alreadyExists = book.review_set.filter(user=user).exists()

    if int(data['rating']) <= 0 or int(data['rating']) > 5:
        content = {'detail':'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    elif user == book.user:
        return Response({'detail':'Permission denied!'})

    elif alreadyExists:
        reviewData.comment = data['comment']
        reviewData.rating = data['rating']
        reviewData.save()

        return Response('Review Added')



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeBookReview(request,pk,sk):
    user = request.user
    data = request.data
    book = LawBook.objects.get(_id=sk)
    reviewData = Review.objects.get(_id=pk)

    alreadyExists = book.review_set.filter(user=user).exists()

    if user == book.user:
        return Response({'detail':'Permission denied!'})

    elif alreadyExists:
        reviewData.delete()

    reviews = book.review_set.all()
    book.numReviews = len(reviews)
    book.save()
    return Response('Review Removed')


# @api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
# def BookmarkBook(request,pk):
#     user = request.user
#     data = request.data
#     book  = LawBook.objects.get(_id=pk)

#     if user == book.user:
#         return Response({'detail':'Permission denied!'})
#     else:
#         newBook = book.isBookmarked = data['bookmark']
#         newBook.save()
#         serializer = LawBookSerializer(newBook, many=False)
#         return response(serializer.data)



    