from event.models import Batch, Circular, Club, Department, Event,Faculty, Student
from django.contrib import admin
from django.contrib.admin import ModelAdmin
    


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user','department','reg_no','batch','mobile_no']
    list_filter = ['department','batch']
    search_fields = ['user','email']

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_name','faculty_id','department','designation' ]
    list_filter = ['department','designation']
    search_fields = ['faculty_name','faculty_id']

class CircularAdmin(admin.ModelAdmin):
    list_display = ['title','batch','circular_by' ]
    list_filter = ['batch','circular_by']
    search_fields = ['title',]   

class ClubAdmin(admin.ModelAdmin):
    list_display = ['club_name','club_id','incharge' ]
    list_filter = ['incharge']
    search_fields = ['club_name']     

admin.site.register(Student,StudentAdmin)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Department)
admin.site.register(Batch)
admin.site.register(Club,ClubAdmin)
admin.site.register(Circular,CircularAdmin)
admin.site.register(Event)