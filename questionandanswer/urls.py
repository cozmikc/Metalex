from django.urls import path
from . import views



urlpatterns = [
    path('questions/', views.getQuestions.as_view(), name='user-questions'),
    path('unansweredquestions/', views.getUnansweredQuestions.as_view(), name='user-questions'),
    path('topquestions/', views.getTopQuestions.as_view(), name='user-questions'),
    path('recentquestions/', views.getRecentQuestions.as_view(), name='user-questions'),
    path('createquestion/', views.addQuestion, name='users-question'),
    path('<str:pk>/updatequestion/', views.updateQuestion, name='update-question'),
    path('<str:pk>/removequestion/', views.removeQuestion, name='remove-question'),
    path('<str:pk>/createanswer/', views.addAnswer, name='users-answer'),
    path('<str:pk>/updateanswer/', views.updateAnswer, name='update-answer'),
    path('<str:pk>/removeanswer/', views.removeAnswer, name='remove-answer'),
    path('addupvote/<str:qpk>/<str:pk>/', views.addUpvote, name='add-upvote'),
    path('adddownvote/<str:qpk>/<str:pk>/', views.addDownvote, name='add-downvote'),
    path('addcomment/<str:qpk>/<str:pk>/', views.addComment, name='add-comment'),
    path('updatecomment/<str:pk>/', views.updateComment, name='update-comment'),
    path('<str:pk>/removecomment/', views.removeComment, name='remove-comment'),
    path('tags/', views.getTags, name='all-tags'),
    
]
