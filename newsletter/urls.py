from django.urls import path
from . import views


urlpatterns = [
    path("join-maillist/", views.addSubscriber, name="subscriber-list"),
    # path("sendmail/", views.sendEmail, name="mail-sendings"),
]
