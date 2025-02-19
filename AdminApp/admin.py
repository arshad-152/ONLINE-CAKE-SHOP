from django.contrib import admin
from AdminApp.models import Category,Cake,Payment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname')

class CakeAdmin(admin.ModelAdmin):
    list_display = ('id','cake_name','price','description','image_url','category')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('card_no','cvv','expiry' , 'balance')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Cake,CakeAdmin)
admin.site.register(Payment,PaymentAdmin)
