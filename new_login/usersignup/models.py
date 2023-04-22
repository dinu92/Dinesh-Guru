from django.db import models

# Create your models here.
class Register(models.Model):
    First_name=models.CharField(max_length=25)
    Last_name=models.CharField(max_length=25)
    Photo=models.ImageField()
    City=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Pin_code=models.IntegerField()
    Sex=models.CharField(max_length=10)
    date_of_birth=models.DateField()
    Mobile=models.IntegerField()
    Mail_ID=models.EmailField()
    password=models.CharField(max_length=25)
    Confirm_password=models.CharField(max_length=25)

class Meta:
    db_table='Register'