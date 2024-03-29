from django.urls import path
from . import views


urlpatterns = [
    path('verifiables/', views.getVerifiables, name='verifiables'),
    path('verify-member/<str:pk>/', views.memberVerification, name='verify-member'),
]
