from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import *


class ChamberSerializer(serializers.ModelSerializer):
    practiceareas = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)       
    class Meta:
        model = Chamber
        fields = "__all__"


    def get_practiceareas(self,obj):
        practiceareas = obj.practicearea_set.all()
        serializer = PracticeAreaSerializer(practiceareas, many=True)
        return serializer.data

    def get_reviews(self,obj):
        reviews = obj.memberreview_set.all()
        serializer = MemberReviewSerializer(reviews, many=True)
        return serializer.data


class PracticeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeArea
        fields = "__all__"


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class MemberReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MemberReview
        fields = "__all__"





