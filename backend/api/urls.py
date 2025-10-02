from rest_framework_simplejwt.views import (TokenObtainPairView, 
                                            TokenRefreshView,
                                            TokenVerifyView)
from django.urls import path
from .views import (CustomTokenObtainPairView, 
                    UserDetailView, 
                    UserView, 
                    SignView, 
                    VideoView)

urlpatterns = [
    path('auth/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='singular_user'),
    path('users/', UserView.as_view(), name='users'),
    path('signs/', SignView.as_view(), name='signs'),
    path('videos/', VideoView.as_view(), name='videos'),
]