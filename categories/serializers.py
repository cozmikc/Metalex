from rest_framework import serializers
from django.db.models import fields
from .models import *



class CategorySerializer(serializers.ModelSerializer):
    names = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = "__all__"

    def get_names(self, obj):
        names = obj.categoryname_set.all()
        serializer = CategoryNameSerializer(names, many=True)
        return serializer.data

class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryName
        fields = "__all__"