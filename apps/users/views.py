from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import UserModel
from .serializers import UserSerialazer
class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        serialazer = UserSerialazer(instance=users, many=True)
        return Response(serialazer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        # user = UserModel(name='Max', age=18, status=True)
        # user.save()
        # # запишемо в 1 стрічку
        # UserModel.objects.create(name='Ira', age=25, status=False)
        data = self.request.data
        serializer = UserSerialazer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response (serializer.data, status.HTTP_201_CREATED)
    
class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.get(pk=pk)

        serialazer = UserSerialazer(user)
        return Response(serialazer.data, status.HTTP_200_OK)
        
    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = UserModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.get(pk=pk)
        serialazer = UserSerialazer(user, data)

        if not serialazer.is_valid():
            return Response(serialazer.errors, status.HTTP_400_BAD_REQUEST)

        serialazer.save()
        return Response(serialazer.data, status.HTTP_200_OK)
    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = UserModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.get(pk=pk)
        serialazer = UserSerialazer(user, data, partial=True)

        if not serialazer.is_valid():
            return Response(serialazer.errors, status.HTTP_400_BAD_REQUEST)

        serialazer.save()
        return Response(serialazer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not Found', status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

