from django.urls import path
from . import views



urlpatterns = [
    path("members-listing/", views.searchMembersRoute.as_view(), name="members-listing"),
    path("memberdetails/<str:pk>/<str:category>/", views.getMemberDetails, name="member-details"),
    path("relatedmembers-listing/<str:pk>/<str:category>/", views.getRelatedMembers, name="relatedmembers-listing"),
    path("member-practicearea/<str:pk>/", views.getMemberPracticeArea, name="member-practicearea"),
    path("add-practicearea/<str:pk>/", views.addMemberPracticeArea, name="add-practicearea"),
    path("remove-practicearea/<str:pk>/<str:sk>/", views.removeMemberPracticeArea, name="remove-practicearea"),
    path("member-qualification/<str:pk>/", views.getMemberQualification, name="member-qualification"),
    path("addmember-qualification/<str:pk>/", views.addMemberQualification, name="addmember-qualification"),
    path("updatemember-qualification/<str:pk>/<str:sk>/", views.updateMemberQualification, name="updatemember-qualification"),
    path("updatemember-description/<str:pk>/", views.updateMemberDescription, name="updatemember-description"),
    path("member-contact/<str:pk>/", views.getMemberContact, name="member-contact"),
    path("updatemember-contact/<str:pk>/<str:sk>/", views.updateMemberContact, name="updatemember-contact"),
    path("addmember-review/<str:pk>/", views.addMemberReview, name="addmember-review"),  
    path("updatemember-review/<str:pk>/<str:sk>/", views.updateMemberReview, name="updatemember-review"),  
    path("removemember-review/<str:pk>/<str:sk>/", views.removeMemberReview, name="removemember-review"),
    path("update-dp/<str:pk>/", views.updateProfileImage, name="update-dp"),
    path("updatebanner-details/<str:pk>/", views.updateBannerDetails, name="updatebanner-details"),
    path("premium-member/<str:pk>/", views.memberPlan, name="premium-member"),
    path("plan-status/<str:pk>/", views.checkPlan, name="plan-status"),
    path('verify-member/', views.memberVerification, name='verify-member')
   

]
