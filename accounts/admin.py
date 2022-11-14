from django.contrib import admin
from .models import User, Team
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'role',
                    'mobile'
                )
            }
        )
    )


admin.site.register(User, UserAdmin)
admin.site.register(Team)
