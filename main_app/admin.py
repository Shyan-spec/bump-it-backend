from django.contrib import admin
from .models import Profile, BumpEvent, MatchHistory
# Register your models here.

admin.site.register(Profile)
admin.site.register(BumpEvent)
admin.site.register(MatchHistory)