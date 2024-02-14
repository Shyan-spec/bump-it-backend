from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Import the User
from django.contrib.auth.models import User

RPS_CHOICES = (
    ('Rock', 'Rock'),
    ('Paper', 'Paper'),
    ('Scissors', 'Scissors')
)


class Profile(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return f"{self.name}"
    
class BumpEvent(models.Model):
    phone_time_stamp= models.DateTimeField()
    server_time_stamp= models.DateTimeField(auto_now_add=True)
    choice= models.CharField(max_length=100, choices=RPS_CHOICES)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.choice} - {self.user}"
    
class MatchHistory(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    player_one = models.ForeignKey(User, 
                                   related_name='player_one_matches',
                                   on_delete=models.CASCADE)
    player_two = models.ForeignKey(User, 
                                   related_name='player_two_matches',
                                   on_delete=models.CASCADE)
    
    userchoice_1 = models.CharField(max_length=50, default='')
    userchoice_2 = models.CharField(max_length=50, default='')
    

# Note: You'll need to implement the logic for determining which BumpEvent instances
# to assign to usermove_1 and usermove_2 based on your application's requirements.

  