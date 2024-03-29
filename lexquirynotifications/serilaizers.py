from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import *



class LawyerNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerNotification
        fields = "__all__"


class PaymentPlanNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentPlanNotification
        fields = "__all__"

class QuestionNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionNotification
        fields = "__all__"


class RecentQuestionNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentQuestionNotification
        fields = "__all__"