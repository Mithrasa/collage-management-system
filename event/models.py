from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Batch(models.Model):
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=4)  
    def __str__(self):        
        return '%s - %s' % (self.start_year,self.end_year) 

class Student(models.Model):
    reg_no = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True)
    mobile_no = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField(null=True)
    


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=35)   
    faculty_id = models.CharField(max_length=10,unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    designation= models.CharField(max_length=35) 
    hod = models.BooleanField(default=False)
    def __str__(self):
        return self.faculty_name


class Club(models.Model):
    profile_photo=models.ImageField(blank=True,null=True,upload_to="profile_picture")
    club_id = models.CharField(max_length=10,unique=True)
    club_name = models.CharField(max_length=35)   
    incharge = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    description=models.TextField(null=True)
    def __str__(self):
        return self.club_name

class Event(models.Model):
    profile_photo=models.ImageField(blank=True,null=True,upload_to="profile_picture")
    event_name = models.CharField(max_length=35)
    start_date =  models.DateField()
    end_date =  models.DateField()
    post_date = models.DateTimeField(auto_now_add=True) 
    description =models.TextField(null=True) 
    organized_by =models.ForeignKey(Club,on_delete=models.CASCADE,null=True)
    organizer = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    def __str__(self):
        return self.event_name


class Circular(models.Model):
    profile_photo=models.ImageField(blank=True,null=True,upload_to="profile_picture")
    title = models.CharField(max_length=35)
    description =models.TextField(null=True) 
    department = models.ManyToManyField(Department,related_name='department')
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    circular_by = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    date=models.DateField()
    def __str__(self):
        return self.title








