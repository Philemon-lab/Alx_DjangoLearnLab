from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'added_by')

# LibraryProject/bookshelf/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Implement your create logic
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Implement your edit logic
    return render(request, 'bookshelf/edit_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Implement your delete logic
    return redirect('view_books')
