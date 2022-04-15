
from urllib.parse import urlparse
from django.urls import path
from . views import *
urlpatterns = [
    path('',index,name="index"),
    path('login',LoginView.as_view(),name="login"),
    path('signup',SignUpView.as_view(),name="signup"),
]

