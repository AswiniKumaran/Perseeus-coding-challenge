from django.db import models
# Create your models here.

class User(models.Model):
    id=models.PositiveIntegerField(primary_key=True)
    lastName=models.CharField(max_length=20,null=False)
    firstName=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.firstName+" "+self.lastName


class Email(models.Model):
    user=models.ForeignKey(User,models.SET_NULL,related_name='user_email',null=True,blank=True)
    id=models.PositiveIntegerField(primary_key=True)
    mail=models.EmailField(unique=True)
    def __str__(self):
        return self.mail

class PhoneNumber(models.Model):
    user=models.ForeignKey(User,models.SET_NULL,related_name='user_mobile',null=True,blank=True)
    id=models.PositiveIntegerField(primary_key=True)
    number=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return str(self.number)
