from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, BumpEvent, Match
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import UserSerializer, BumpEventSerializer, MatchHistorySerializer

# Create your views here.
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
    
class MatchHistoryView(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchHistorySerializer