from django.urls import path
from .views import CreateUserView, LoginUserView, VerifyUserView, BumpEventView, MatchHistoryView, MatchHistoryDetailsView, ProfileView, ProfileDetailsView

urlpatterns = [
    path('users/login/', LoginUserView.as_view(), name='login'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/profile/', ProfileView.as_view(), name='profile'),
    path('users/profile/<int:userId>', ProfileDetailsView.as_view(), name='profile-details'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('game/bump', BumpEventView.as_view(), name='bump-event'),
    path('game/result', MatchHistoryView.as_view(), name='match'),
    path('game/result/<int:resultId>', MatchHistoryDetailsView.as_view(), name='match-details')
]