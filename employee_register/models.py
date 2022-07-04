from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
    
SOURCE=(
    ('DILPURA','DILPURA'),
    ('BANAR',"BANAR"),
    ('NAURANGPUR','NAURANGPUR')
)
DESTINATION=(
    ('JAIPUR','JAIPUR'),
    ('AHEMADABAD','AHMEDABAD'),
    ('DELHI','DELHI')
)
class addTrip(models.Model):
    transporter_name=models.CharField(max_length=100, null=True, blank=True)
    vehicle = models.CharField(max_length=100, blank=True)
    source=models.CharField(choices=SOURCE, max_length=50, blank=True,null=True)
    # created=models.DateTimeField(auto_now_add=True)
    destination=models.CharField(choices=DESTINATION, max_length=50, blank=True,null=True)
    approx_distance=models.PositiveIntegerField(blank=True, null=True)
    Fixed_amount_btw_s_d=models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.transporter_name ) 


