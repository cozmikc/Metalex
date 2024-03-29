from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name="posts"),
    # path('recent-posts/', views.getRecentPosts, name="recent-posts"),
    path('addpost-comment/<str:pk>/', views.addPostComment, name="addpost-comment"),
    path('updatepost-comment/<str:pk>/', views.updatePostComment, name="updatepost-comment"),
    path('removepost-comment/<str:pk>/', views.removePostComment, name="removepost-comment")
]
