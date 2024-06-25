from django.contrib import admin
from .models import Contact

# Register your models here.


# Can see all the registered Contact instance in the DB
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'email')
