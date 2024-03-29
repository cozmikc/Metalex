from django.urls import path
from . import views



urlpatterns = [
    path('category/', views.categoryRoute.as_view(), name='category-routes')
]