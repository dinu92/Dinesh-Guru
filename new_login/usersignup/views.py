from django.shortcuts import render
from .models import Register

def register(request):
     if request.method=="POST":
         New_user={"register":Register}
         date=Register.objects.create(First_name=request.POST.get("First_Name"),Last_name=request.POST.get("Last_Name"),Photo=request.POST.get("Profile_pic"),City=request.POST.get("City"),State=request.POST.get("State"),Pin_code=request.POST.get("Pin_Code"),Sex=request.POST.get("Sex"),date_of_birth=request.POST.get("Date_of_birth"),Mobile=request.POST.get("Mobile_Number"),Mail_ID=request.POST.get("Email"),password=request.POST.get("password"),Confirm_password=request.POST.get("Confirm_Password"))
         date.save()
     return render(request,'register.html')