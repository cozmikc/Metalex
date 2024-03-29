from unicodedata import category
from .models import *
from lawbooks.models import LawBook
from chamber.models import Chamber
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import BookmarkedLawyerSerializer, BookmarkedBookSerializer



# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBookmarkBooks(request):
    user = request.user
    bookmarkBook = BookmarkedBook.objects.filter(user=user)
    serializer = BookmarkedBookSerializer(bookmarkBook, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBookmarkLawyers(request):
    user = request.user
    bookmarkLawyer = BookmarkedLawyer.objects.filter(user=user)
    serializer = BookmarkedLawyerSerializer(bookmarkLawyer, many=True)
    return Response(serializer.data)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBookmarkBook(request,pk):
    user = request.user
    book = LawBook.objects.get(_id=pk)
    if user == book.user:
        return Response({'Permission denied!'})
    if BookmarkedBook.objects.filter(book=book).exists():
        bookmarkedBook = BookmarkedBook.objects.get(book=book)
        bookmarkedBook.delete()
        return Response("Bookmark deleted")

    else:
        bookmarkBook = BookmarkedBook.objects.create(
            user = user,
            book = book,
            title = book.title,
            coverImage = book.coverImage,
            category = book.category
    )

    serializer = BookmarkedBookSerializer(bookmarkBook, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeBookmarkBook(request,pk):
    user = request.user
    book = BookmarkedBook.objects.get(_id=pk)
    if user == book.user:
        book.delete()

        return Response('Book was removed')



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBookmarkLawyer(request,pk):
    user = request.user
    lawyer = Chamber.objects.get(_id=pk)
    if user == lawyer.member:
        return Response({'Permission denied!'})
    if BookmarkedLawyer.objects.filter(member=lawyer).exists():
        bookmarkedLawyer = BookmarkedLawyer.objects.get(member=lawyer)
        bookmarkedLawyer.delete()
        return Response("Bookmark deleted")
    else:
        bookmarkLawyer = BookmarkedLawyer.objects.create(
            user = user,
            member = lawyer,
            name = lawyer.name,
            profile_image = lawyer.profile_image,
            category = lawyer.category
          
    )

    serializer = BookmarkedLawyerSerializer(bookmarkLawyer, many=False)
    return Response(serializer.data)
    


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeBookmarkLawyer(request,pk):
    user = request.user
    lawyer = BookmarkedLawyer.objects.get(_id=pk)
    if user == lawyer.user:
        lawyer.delete()

        return Response('Member was removed')



# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def removeBookmarkBook(request,pk):
#     user = request.user
#     data = request.data
#     book = BookmarkedBook.objects.get(_id=pk)
#     book.delete()

#     return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getBookmarkLawyer(request,pk):
    user = request.user
    lawyer = Chamber.objects.get(_id=pk)
    newLawyer = BookmarkedLawyer.objects.create(
        user = user,
        member = lawyer

    )
    serializer = BookmarkedLawyerSerializer(newLawyer, many=False)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def addBookmarkLawyer(request,pk):
#     user = request.user
#     data = request.data
#     newLawyer = BookmarkedLawyer.objects.create(
#         user = user,
#         book = data['member']
#     )
#     serializer = BookmarkedLawyerSerializer(newLawyer, many=False)
#     return Response(serializer.data)