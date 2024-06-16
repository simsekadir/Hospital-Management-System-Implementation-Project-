from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Appointment, Medicine, Prescription

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'address', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Appointment)
admin.site.register(Medicine)
admin.site.register(Prescription)
