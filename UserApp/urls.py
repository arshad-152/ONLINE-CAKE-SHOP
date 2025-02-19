from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('viewCakes/<id>/',views.ViewCakes),
    path('viewDetails/<id>/',views.ViewDetails),
    path('SignUp/',views.SignUp),
    path('Login/',views.Login),
    path('Logout/',views.LogOut),
    path('Cart/',views.ShowCart),
    path('makepayment/',views.MakePayment),
]