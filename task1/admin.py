from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User

    list_display = (
        'user_id','Name', 'Email_Address', 'DateofBirth', 'Phone_number')
    fieldsets = (
        ('User', {'fields': (
            'Name', 'Email_Address', 'DateofBirth', 'Phone_number'
        )}),
    )

admin.site.register(User, UserAdmin)
