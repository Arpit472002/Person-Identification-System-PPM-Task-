from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import MyUser
# Create your models here.
class Email(models.Model):
    email_id=models.EmailField(unique=True)
    def __str__(self):
        return self.email_id

class MobileNumber(models.Model):
    phone_number=PhoneNumberField(null=False,blank=False,unique=True)
    def __str__(self):
        return self.phone_number

class Aadhar(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    aadhar_number=models.CharField(max_length=12)
    is_active=models.BooleanField()
    def __str__(self):
        return self.user+' : '+self.aadhar_number

class Address(models.Model):
    user= models.ForeignKey(MyUser,on_delete=models.CASCADE)
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    postal_code=models.CharField(max_length=6)
    def __str__(self):
        return self.user+', '+self.street+', '+self.city+', '+self.state+', '+self.postal_code
    class Meta:
        verbose_name = 'Addresse'

class Qualfication(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    college_name=models.CharField(max_length=200)
    year_of_passing=models.IntegerField()
    percentage=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(0)])
    def __str__(self):
        return self.user+'-'+self.college_name+'-'+self.year_of_passing

class Bank(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    account_no=models.CharField(max_length=15)
    bank_name=models.CharField(max_length=100)
    ifsc_code=models.CharField(max_length=20)
    def __str__(self):
        return self.user+'-'+self.account_no


class PersonalDetails(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=200)
    dob=models.DateField(auto_now_add=False)
    blood_group=models.CharField(max_length=3)
    mobile_number=models.ManyToManyField(MobileNumber)
    email=models.ManyToManyField(Email)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name='Personal Detail'
        
class PastJobExperience(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=200)
    job_role=models.CharField(max_length=200)
    years_of_experience=models.IntegerField()
    def __str__(self):
        return self.user+'-'+self.company_name+'-'+self.job_role
