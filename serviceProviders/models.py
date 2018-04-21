from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class ServiceProviders(User):
    GENDER=(
        ('male','male'),
        ( 'female','female')

    )
    RATES=(
        ('nonStar','nonStar'),
        ('firstStar','firstStar'),
        ('secondStart','secondStar'),
        ('thirdStar','thirdStar'),
        ('fourthStart','fourthStart'),
        ('fifthStart','fifthStar')
    )



    gender=models.CharField(choices=GENDER,max_length=40)
    personal_descriptions=models.TextField()
    address=models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+255?\d{9}$',
                                 message="Phone number must be entered in the format: '+255******'. Up to 9 character is allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)

    rates=models.CharField(choices=RATES,max_length=50,default='nonStar'),

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name_plural = 'serviceProviders'
class VideoComments(models.Model):
    comments=models.TextField()
    def __str__(self):
        return  self.comments
    class Meta:
        verbose_name_plural='videoComments'


class Videos(models.Model):
    url=models.FileField(upload_to='serviceProvidersVideos/%Y/%m/%d')
    likes=models.IntegerField()
    dislikes=models.IntegerField()
    comments=models.ForeignKey(VideoComments,on_delete=models.CASCADE)
    descriptions=models.TextField()
    service_proviser=models.ForeignKey(ServiceProviders ,on_delete=models.CASCADE)
    def __str__(self):
        return self.descriptions
    class Meta:
        verbose_name_plural = 'Videos'
class ImageComments(models.Model):
    comments=models.TextField()
    def __str__(self):
        return self.comments
    class Meta:
        verbose_name_plural = 'ImageCommments'
class Images(models.Model):
    url=models.FileField(upload_to='serviceProvidersImages/%Y/%m/%d')
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    comments = models.ForeignKey(ImageComments,on_delete=models.CASCADE)
    descriptions = models.TextField()
    service_proviser = models.ForeignKey(ServiceProviders, on_delete=models.CASCADE)
    def __str__(self):
        return self.descriptions
    class Meta:
        verbose_name_plural = 'Images'

class ServiceName(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self):
         return self.name

     class Meta:
         verbose_name_plural = 'ServiceNames'
class Services(models.Model):
    CURRENCY=(
        ('sh','sh'),
        ('$','$')
    )
    name=models.ForeignKey(ServiceName,on_delete=models.CASCADE)
    price=models.IntegerField()
    currency=models.CharField(choices=CURRENCY,max_length=40)
    discriptions=models.TextField()
    service_provider=models.ForeignKey(ServiceProviders,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Services'









