from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import IndiviadualUserModel
from .serializers import IndiviadualUserSerializer


class IndiviadualUserView(APIView):

    def get(self, request, *args, **kwargs):
        allProfile = IndiviadualUserModel.objects.all()
        serializer = IndiviadualUserSerializer(allProfile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'address': request.data.get('address')
        }
        serializer = IndiviadualUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
