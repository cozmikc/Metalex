from django.urls import path
from . import views


urlpatterns = [
    path('addbookmark-book/<str:pk>/', views.addBookmarkBook, name='add-book'),
    path('getbookmark-books/', views.getBookmarkBooks, name='get-book'),
    path('removebookmark-book/<str:pk>/', views.removeBookmarkBook, name='remove-book'),
    path('addbookmark-lawyer/<str:pk>/', views.addBookmarkLawyer, name='add-lawyer'),
    path('getbookmark-lawyers/', views.getBookmarkLawyers, name='get-lawyer'),
    path('removebookmark-lawyer/<str:pk>/', views.removeBookmarkLawyer, name='remove-lawyer'),
]


