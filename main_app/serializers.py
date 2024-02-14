from rest_framework import serializers
from .models import Profile, BumpEvent, MatchHistory
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile_name = serializers.CharField(source='profile.name')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile_name']
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile', {})
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, **profile_data)
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
        
class BumpEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BumpEvent
        fields = '__all__' 
    
    server_time_stamp = serializers.DateTimeField(required=False)
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
        
class MatchHistorySerializer(serializers.ModelSerializer):
     class Meta:
        model = MatchHistory
        fields = '__all__' 


class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


    
class ProfileDetailsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'