from django.urls import path
from .views import *
#Create URL's here
urlpatterns=[
    path('email/',EmailView.as_view()),
    path('email/<str:pk>/',EmailRetrieveView.as_view()),
    path('mobile_number/',MobileNumberView.as_view()),
    path('mobile_number/<str:pk>/',MobileNumberRetrieveView.as_view()),
    path('aadhar/',AadharView.as_view()),
    path('aadhar/<str:pk>/',AadharRetrieveView.as_view()),
    path('address/',AddressView.as_view()),
    path('address/<str:pk>/',AddressRetrieveView.as_view()),
    path('qualification/',QualficationView.as_view()),
    path('qualification/<str:pk>/',QualficationRetrieveView.as_view()),
    path('bank/',BankView.as_view()),
    path('bank/<str:pk>/',BankRetrieveView.as_view()),
    path('personal_details/',PersonalDetailsView.as_view()),
    path('personal_details/<str:pk>/',PersonalDetailsRetrieveView.as_view()),
    path('past_job_experience/',PastJobExperienceView.as_view()),
    path('past_job_experience/<str:pk>/',PastJobExperienceRetrieveView.as_view())
]