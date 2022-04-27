from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Book, BooksCutomUser

@admin.register(BooksCutomUser)
class UserAdmin(DefaultUserAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at']

