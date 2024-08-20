from django.shortcuts import render
from django.http import Http404

from rest_framework import generics, status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserSignUpAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'token': user.tokens(),
            'user':UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    
class UserUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        id = self.kwargs.get('id')
        user = User.objects.filter(id=id).first()
        if user is None:
            raise Http404("User not found.")
        return user
