from django.db import models
class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    program=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    year=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    regdate=models.CharField(max_length=30)

class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=30)
    confirmpassword=models.CharField(max_length=30)
    usertype=models.CharField(max_length=50)
    status=models.CharField(max_length=10)

class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=30)
    
# _________________this is for forgot password / reset password token
from django.db import models
from django.utils import timezone
from datetime import timedelta

class PasswordResetToken(models.Model):
    userid = models.CharField(max_length=50)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    
    def is_expired(self):
        expiry_time = self.created_at + timedelta(hours=1)  # 1 hour expiry
        return timezone.now() > expiry_time
    
    def __str__(self):
        return f"Reset token for {self.userid}"    
    