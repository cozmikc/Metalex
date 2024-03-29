from rest_framework import serializers
from .models import Verifiable




class VerifiableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verifiable
        fields = "__all__"