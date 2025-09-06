from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'course')  
    search_fields = ('name', 'email', 'course')              
    list_filter = ('course', 'age')  
    ordering = ('name',)
