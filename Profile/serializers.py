from rest_framework import serializers
from .models import IndiviadualUserModel

class IndiviadualUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndiviadualUserModel
        fields = ['id','name','age','address']