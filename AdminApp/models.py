from django.db import models

# Create your models here.

class Category(models.Model):
    cname = models.CharField(max_length=20)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.cname
    
class Cake(models.Model):
    cake_name = models.CharField(max_length=20)
    price = models.IntegerField(default=300)
    description = models.CharField(max_length=100)
    image_url = models.ImageField(default='abc.jpg',upload_to='Images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table = "Cake"

    def __str__(self):
        return self.cake_name
    

class Payment(models.Model):
    card_no = models.CharField(max_length=10)
    cvv = models.CharField(max_length=10)
    expiry = models.CharField(max_length=10)
    balance = models.FloatField(default=1000)

    class Meta:
        db_table = "Payment"