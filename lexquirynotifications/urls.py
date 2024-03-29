from django.urls import path
from . import views


urlpatterns = [
    path('lawyer-notify/', views.getLawyerNotifications, name="lawyer-notifications"),
    path('question-notify/<str:pk>/', views.getQuestionNotifications, name="question-notifications"),
    path('recentquestion-notify/<str:pk>/', views.getRecentQuestionNotifications, name="recentquestion-notifications"),
    path('removequestion-notify/<str:pk>/', views.removeQuestionNotifications, name="removequestion-notifications"),
    path('removerecentquestion-notify/<str:pk>/', views.removeRecentQuestionNotifications, name="removerecentquestion-notifications"),
    path('removelawyer-notify/', views.removeLawyerNotifications, name="removelawyer-notifications"),
    path('plan-notify/', views.getPlanNotifications, name="plan-notifications"),
    path('removeplan-notify/', views.removePlanNotifications, name="removeplan-notifications"),
]
