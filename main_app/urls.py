from django.urls import path
from .views import CreateUserView, LoginUserView, VerifyUserView

urlpatterns = [
    path('users/login/', LoginUserView.as_view(), name='login'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh')
]