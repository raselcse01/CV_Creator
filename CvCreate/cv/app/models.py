from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    objects = None
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    pro_pic=models.ImageField(default='default_pic.jpg', upload_to="ProfilePic")
    gender=models.CharField(max_length=20)
    date_of_birth=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    blood=models.CharField(max_length=15)

    present_address=models.TextField(max_length=200)
    permanent_address=models.TextField(max_length=200)

    SSC_Roll= models.IntegerField(default=0)
    SSC_Reg= models.IntegerField(default=0)
    SSC_passing_y=models.CharField(max_length=10)
    SSC_Result= models.FloatField(default=0)

    HSC_Roll = models.IntegerField(default=0)
    HSC_Reg = models.IntegerField(default=0)
    HSC_passing_y = models.CharField(max_length=10)
    HSC_Result = models.FloatField(default=0)

    BSc_Department= models.CharField(max_length=150)
    BSc_University= models.CharField(max_length=150)
    BSc_Roll= models.CharField(max_length=100)
    BSc_passing_y = models.CharField(max_length=10)
    BSc_Result = models.FloatField(default=0)

    MSc_Department = models.CharField(max_length=150)
    MSc_University = models.CharField(max_length=150)
    MSc_Roll = models.CharField(max_length=100)
    MSc_passing_y = models.CharField(max_length=10)
    MSc_Result = models.FloatField(default=0)

    Language_Skill = models.TextField(max_length=300)
    Computer_Literature = models.TextField(max_length=300)
    Programing_Laguage = models.TextField(max_length=300)
    Training_Topic = models.TextField(max_length=300)

    def __str__(self):
        return str(self.user)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)