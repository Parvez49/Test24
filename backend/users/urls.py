from django.urls import path
from . import views

urlpatterns = [
    path('/sign-up', views.UserSignUpAPIView.as_view(), name='user-register'),
    path('/list',views.UserListAPIView.as_view(),name='user-list')
]
