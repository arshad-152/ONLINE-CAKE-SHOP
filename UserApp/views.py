from django.shortcuts import render,redirect
from AdminApp.models import Category,Cake,Payment
from UserApp.models import UserInfo,MyCart
from django.http import HttpResponse
# Create your views here.

def Home(request):
    cats = Category.objects.all()
    cakes = Cake.objects.all()
    return render(request,'Home.html',{'cats':cats,'cakes':cakes})

def ViewCakes(request,id):
    cats = Category.objects.all()
    cat = Category.objects.get(id=id)
    cakes = Cake.objects.filter(category=cat)
    return render(request,'Home.html',{"cakes":cakes,'cats':cats})

def ViewDetails(request,id):
    if request.method == "GET":
        cake = Cake.objects.get(id=id)
        cats = Category.objects.all()
        return render(request,'viewDetails.html',{'cake':cake,'cats':cats})
    else:
        #check if user has logged in
        if "uname" in request.session:
            #Cake,User,Qty
            cake_id = request.POST["cake_id"]
            qty = request.POST["qty"]
            uname = request.session["uname"]

            cake = Cake.objects.get(id=cake_id)
            user = UserInfo.objects.get(username=uname)

            
            cart = MyCart.objects.filter(cake=cake,user=user,qty=qty)

            if cart.exists():
                 return HttpResponse("User Already Exist")
            else: 
                cart = MyCart(cake=cake,user=user,qty=qty)
                cart.save()
                return redirect(ShowCart)
            
        else:
            return redirect(Login)
        
def SignUp(request):
    if request.method == "GET":
        return render(request,"signup.html",{})
    else:
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]

        try:
            u1 = UserInfo.objects.get(username=uname)
        except:
                u1 = UserInfo(uname,pwd)
                u1.save()
        else:
                return HttpResponse("User Already Exist..!!")

        return redirect(Home)


def Login(request):
    if request.method == "GET":
         return render(request,"login.html",{})
    else:
         uname = request.POST["uname"]
         pwd = request.POST["pwd"]

         try:
              user = UserInfo.objects.get(username=uname,password=pwd)
         except:
              return redirect(Login)
         else:
              #Add user to session
              request.session["uname"]=uname
              return redirect(Home)
         

def LogOut(request):
     request.session.clear()
     return redirect(Home)


def ShowCart(request):
    cats = Category.objects.all()
    user = UserInfo.objects.get(username = request.session["uname"])
    items = MyCart.objects.filter(user=user)
    if request.method == "GET":
        total = 0
        for item in items:
            total+=item.cake.price * item.qty
        request.session["total"]=total
    else:
          action = request.POST["action"]
          cart_id = request.POST["cart_id"]
          item = MyCart.objects.get(id=cart_id)
          if action == "delete":
               item.delete()
          else:
               qty = request.POST["qty"]
               item.qty = qty
               item.save()

    return render(request,"Cart.html",{"items":items,"cats":cats})


def MakePayment(request):
     if request.method == "GET":
          return render(request,"payment.html",{})
     else:
          card_no = request.POST["card_no"]
          cvv = request.POST["cvv"]
          expiry = request.POST["expiry"]

          try:
             buyer = Payment.objects.get(card_no=card_no,cvv=cvv,expiry=expiry)
          except:
               return redirect(MakePayment)
          else:
               total = request.session["total"]
               if buyer.balance > total:
                    #proceed to make payment
                    owner = Payment.objects.get(card_no = '222', cvv = '222', expiry = '12/2030')
                    buyer.balance -= total
                    owner.balance += total
                    buyer.save()
                    owner.save()
               else:
                    return HttpResponse("Insufficient Balance")
               
        
               


            

