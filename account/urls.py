from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)




urlpatterns = [

    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("logout-member/<str:pk>/", views.loggedOutMember, name="logout-member"),
    path('users/register/', views.registerUser, name='create-user'),
    path('user/profile/', views.getUserProfile, name='user-profile'),
    path('delete/user/<str:pk>/', views.deleteUserProfile, name='user-delete'),
    path('profile/update/', views.updateUserProfile, name='user-profile-update'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]