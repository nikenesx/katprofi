from django.contrib import admin
from main.models import ServiceRequest


@admin.register(ServiceRequest)
class AuthorAdmin(admin.ModelAdmin):
    pass
