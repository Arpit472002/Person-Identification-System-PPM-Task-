from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.
class EmailView(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class MobileNumberView(generics.ListCreateAPIView):
    queryset = MobileNumber.objects.all()
    serializer_class = MobileNumberSerializer

class MobileNumberRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MobileNumber.objects.all()
    serializer_class = MobileNumberSerializer

class AadharView(generics.ListCreateAPIView):
    queryset = Aadhar.objects.all()
    serializer_class = AadharSerializer

class AadharRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aadhar.objects.all()
    serializer_class = AadharSerializer

class AddressView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class QualficationView(generics.ListCreateAPIView):
    queryset = Qualfication.objects.all()
    serializer_class = QualficationSerializer

class QualficationRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Qualfication.objects.all()
    serializer_class = QualficationSerializer

class BankView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class PersonalDetailsView(generics.ListCreateAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

class PersonalDetailsRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

class PastJobExperienceView(generics.ListCreateAPIView):
    queryset = PastJobExperience.objects.all()
    serializer_class = PastJobExperienceSerializer

class PastJobExperienceRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastJobExperience.objects.all()
    serializer_class = PastJobExperienceSerializer