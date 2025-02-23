from django.urls import path
from rest_framework.routers import DefaultRouter
from user.views.signup_view import SignupViewSet
from user.views.signin_view import SigninViewSet
from user.views.user_view import UserViewSet

router = DefaultRouter()
router.register(r'signup', SignupViewSet, basename='signup')
router.register(r'signin', SigninViewSet, basename='signin')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls + [
    path('user/profile/<str:username>/', UserViewSet.as_view({'get': 'retrieve', 'patch': 'update'}), name='user-profile'),
]
