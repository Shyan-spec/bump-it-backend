from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, BumpEvent, MatchHistory, Profile
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, BumpEventSerializer, MatchHistorySerializer, ProfileViewSerializer,ProfileDetailsViewSerializer
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading
from django.shortcuts import get_object_or_404


# user registration
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = User.objects.get(username=response.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
            }, status=status.HTTP_201_CREATED)
        return response

class LoginUserView(APIView):
  permission_classes = [permissions.AllowAny]
  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })
    
class BumpEventView(generics.ListCreateAPIView):
    queryset = BumpEvent.objects.all()
    serializer_class = BumpEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
      # This associates the newly created cat with the logged-in user
      serializer.save(user=self.request.user)
    
    
    
    def deleteSoon():
        print("This message is displayed after a delay.")

    print("Delay starts.")
    timer = threading.Timer(5, deleteSoon)  # Delay for 5 seconds
    timer.start()

    print("This prints immediately, without waiting for the delay.")
      
      
    
class MatchHistoryView(generics.ListCreateAPIView):
    queryset = MatchHistory.objects.all()
    serializer_class = MatchHistorySerializer
    
    
class MatchHistoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = MatchHistorySerializer
  lookup_field = 'resultId'
  
  def get_object(self):
        resultId = self.kwargs.get('resultId')
        return get_object_or_404(MatchHistory, id=resultId)
      

class ProfileView(generics.ListCreateAPIView):
      serializer_class = ProfileViewSerializer
      permission_classes = [permissions.IsAuthenticated]
      
      def get_queryset(self):
       user = self.request.user
       return Profile.objects.filter(user=user)
      
  

class ProfileDetailsView(generics.RetrieveUpdateDestroyAPIView):
  
      serializer_class = ProfileDetailsViewSerializer
      lookup_field = 'userId'
      
      def get_object(self):
        userId = self.kwargs.get('userId')
        return get_object_or_404(Profile, id=userId) 
    
@receiver(post_save, sender=BumpEvent)
def print_bump_event(sender, instance, created, **kwargs):
    if created:  # Check if a new instance was created
        print(f'New BumpEvent Created: {instance}')
        bump_events = BumpEvent.objects.all().order_by('-phone_time_stamp')[0:2]
        print(bump_events)
        
        if len(bump_events) < 2:
          return
        
        match = MatchHistory(
          player_one=bump_events[0].user,
          player_two=bump_events[1].user,
          userchoice_1=bump_events[0].choice,
          userchoice_2=bump_events[1].choice
        )

        match.save()  # Save the match instance to the database
        
        BumpEvent.objects.all().delete()
        
        
        # Use this logic to validate bump request
        # 1 second refresh, need to ensure both users to recieve a signal if a match is created or if the request failed
