from django.urls import path
from . import views



urlpatterns = [
    path('lawbooks/', views.LawbookRoute.as_view(), name='lawbooks'),
    path('addbook/', views.addLawBook, name='add-lawbook'),
    path('bookdetails/<str:pk>/<str:category>/', views.getbookcontentRoute, name='bookcontent'),
    path('<str:pk>/addreview/', views.addReview, name='add-review'),
    path('<str:pk>/<str:sk>/updatereview/', views.updateBookReview, name='update-review'),
    path('<str:pk>/<str:sk>/removereview/', views.removeBookReview, name='remove-review'),


]
