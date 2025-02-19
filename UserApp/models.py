from django.db import models
from AdminApp.models import Cake
 
# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    cake = models.ForeignKey(Cake,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True)
    qty = models.IntegerField(default=20)

    class Meta:
        db_table = "MyCart"