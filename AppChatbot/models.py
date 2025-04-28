from django.db import models


class Admin_Details(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Admin_Details'  

class User_Details(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Dob = models.CharField(max_length=50,default=None)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(default=None)
    Email = models.EmailField()
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)

        
    class Meta:
        db_table = 'User_Details'

      
class Hospital_Details(models.Model):
    Name = models.CharField(max_length=100,default=None)
    Address = models.CharField(max_length=100,default=None)
    Contact = models.CharField(max_length=100,default=None)
    EmergencyContact = models.CharField(max_length=100,default=None)
    BloodBank = models.CharField(max_length=100,default=None)
    AmbulanceService = models.CharField(max_length=100,default=None)
        
    class Meta:
        db_table = 'Hospital_Details'



class Doctor_Details(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    Phone = models.IntegerField(default=None)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Speciality = models.CharField(max_length=100,default=None)


    class Meta:
        db_table = 'Doctor_Details'


class Training_Data(models.Model):
    MainKeyword = models.CharField(max_length=200,default=None)
    Helping1 = models.CharField(max_length=200,default=None)
    Helping2 = models.CharField(max_length=200,default=None)
    Helping3 = models.CharField(max_length=200,default=None)
    Helping4 = models.CharField(max_length=200,default=None)
    Output = models.CharField(max_length=500,default=None)
    Score = models.IntegerField()

    class Meta:
        db_table = 'Training_Data'