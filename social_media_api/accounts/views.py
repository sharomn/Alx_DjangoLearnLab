from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from django.http import JsonResponse
from rest_framework import  permissions
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def home(request):
        return JsonResponse({"message": "Welcome to the Social Media API"})


User = get_user_model()

CustomUser = get_user_model()


class FollowUserView(generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = CustomUser.objects.get(id=user_id)
            request.user.following.add(target_user)
            return Response({'message': f'You are now following {target_user.username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target_user = CustomUser.objects.get(id=user_id)
            request.user.following.remove(target_user)
            return Response({'message': f'You have unfollowed {target_user.username}'})
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
