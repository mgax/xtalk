from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    form = forms.ModelForm
    add_form = forms.ModelForm

    list_display = ["email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = add_fieldsets = [
        (None, {"fields": ["email"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
