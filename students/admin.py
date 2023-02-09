from django.contrib import admin
from .models import Student, Student_info


# from apps.students import models as student_admin

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    model = Student

    list_display = (
        'Student_id','Name', 'DateofBirth', 'Branch', 'Email_address', 'Phone_number')
    fieldsets = (
        ('Student', {'fields': (
            'Name', 'DateofBirth', 'Branch', 'Email_address', 'Phone_number'
        )}),
    )


class StudentInfo(admin.ModelAdmin):
    model = Student_info

    list_display = (
        'Stu_id','Stu_name', 'Course', 'HOD', 'class_teacher')
    fieldsets = (
        ('Student_info', {'fields': ('Stu_id',
            'Stu_name', 'Course', 'HOD', 'class_teacher'
        )}),
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(Student_info, StudentInfo)
