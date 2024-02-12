from django.urls import path
from .views import CreateUserView, LoginUserView, VerifyUserView, BumpEventView, MatchHistoryView, MatchHistoryDetailsView

urlpatterns = [
    path('users/login/', LoginUserView.as_view(), name='login'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('game/bump', BumpEventView.as_view(), name='bump-event'),
    path('game/result', MatchHistoryView.as_view(), name='match'),
    path('game/result/<int:resultId>', MatchHistoryDetailsView.as_view(), name='match-details')
]