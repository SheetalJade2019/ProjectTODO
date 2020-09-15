from django.contrib import admin
from .models import Todo
# Register your models here.

@admin.register
class TodoModelAdmin(admin.ModelAdmin):#to give action
     list_display = ['id','task']

admin.site.register(Todo)
