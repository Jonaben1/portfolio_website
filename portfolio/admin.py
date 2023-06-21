from django.contrib import admin
from .models import Project, Contact
# Register your models here.


admin.site.register(Project)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
