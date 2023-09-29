from django.contrib import admin
from service.models import Employee

class EmployeeDetail(admin.ModelAdmin):
    list_display=("full_name","email_id","mob_num","state","mob_num","password")


admin.site.register(Employee,EmployeeDetail)  




# Register your models here.
