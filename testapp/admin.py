from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'employee_id')
    readonly_fields = ('login_count',)
    fieldsets = (
        ("Ilexius tasks", {'fields': ('employee_id', 'login_count')}),
    ) + UserAdmin.fieldsets

    # Makes the employee id field editable only if the user is not active
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.is_active:
            return self.readonly_fields + ('employee_id',)
        return self.readonly_fields
