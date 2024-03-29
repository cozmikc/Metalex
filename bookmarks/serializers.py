from pyexpat import model
from rest_framework import serializers
from .models import *



class BookmarkedLawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkedLawyer
        fields = "__all__"


class BookmarkedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkedBook
        fields = "__all__"