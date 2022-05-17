from django.urls import path
from .views import *
#Create URL's here
urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegistrationView.as_view(),name='register'),
]