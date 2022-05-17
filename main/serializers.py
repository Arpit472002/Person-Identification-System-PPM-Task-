from rest_framework import serializers
from .models import *

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields=['email_id']

class MobileNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=MobileNumber
        fields=['phone_number']

class AadharSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aadhar
        fields=('__all__')
    
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields=('__all__')

class QualficationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Qualfication
        fields=('__all__')

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields=('__all__')

class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalDetails
        fields=('__all__')
    
class PastJobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=PastJobExperience
        fields=('__all__')