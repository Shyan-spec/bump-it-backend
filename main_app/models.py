from django.db import models
from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Import the User
from django.contrib.auth.models import User

RPS_CHOICES = (
    ('R', 'Rock'),
    ('P', 'Paper'),
    ('S', 'Scissors')
)


class Profile(models.Model):
    name = models.CharField(max_length=50, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=250, default='')
    
    def __str__(self):
        return f"{self.name}"
    
class BumpEvent(models.Model):
    phone_time_stamp= models.DateTimeField()
    server_time_stamp= models.DateTimeField()
    choice= models.CharField(max_length=100, choices=RPS_CHOICES)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.choice}"
    
class MatchHistory(models.Model):
    time_stamp= models.DateTimeField(auto_now_add=True)
    player_one= models.ForeignKey(User, 
                            related_name= 'player_one_matches',
                            on_delete=models.CASCADE)
    player_two= models.ForeignKey(User, 
                            related_name= 'player_two_matches',
                            on_delete=models.CASCADE)
    
    username_1= models.CharField(max_length=50, blank=True)
    username_2= models.CharField(max_length=50, blank=True)
    
    def save(self, *args, **kwargs):
        # Set username_1 to the user's username before saving
        if not self.username_1 :  # Check if username_1 is not already set
            self.username_1 = self.user.username
        if not self.username_2:  # Check if username_2 is not already set
            self.username_2 = self.player_two.username
        super(MatchHistory, self).save(*args, **kwargs)
        

