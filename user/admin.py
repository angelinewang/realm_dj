from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm  # This is the edit form
    model = CustomUser
    list_display = [
        "created_at",
        "updated_at",
        "email",
        "name",
        "password",
        "gender",
        "birthdate",
        "department",
        "profile_picture",
        "role",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("created_at",
                                                          "updated_at",
                                                          "name",
                                                          "gender",
                                                          "birthdate",
                                                          "department",
                                                          "profile_picture",
                                                          "role")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("created_at",
                                                                  "updated_at",
                                                                  "name",
                                                                  "gender",
                                                                  "birthdate",
                                                                  "department",
                                                                  "profile_picture",
                                                                  "role")}),)


admin.site.register(CustomUser, CustomUserAdmin)
