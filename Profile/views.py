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


class IndiviadualUserDetailsView(APIView):

    def get_object(self, user_id):
        try:
            return IndiviadualUserModel.objects.get(id=user_id);
        except IndiviadualUserModel.DoesNotExist:
            return None

    def get(self, request, user_id, *args, **kwargs):
        profile_instance = self.get_object(user_id)
        if not profile_instance:
            return Response(
                {'response': 'Error'}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = IndiviadualUserSerializer(profile_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, *args, **kwargs):
        profile_instance = self.get_object(user_id)
        if not profile_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'address': request.data.get('address')
        }
        serializer = IndiviadualUserSerializer(instance=profile_instance,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, *args, **kwargs):
        profile_instance = self.get_object(user_id)
        if not profile_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        profile_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

