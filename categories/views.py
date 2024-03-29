from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

# # Create your views here.


class categoryRoute(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
