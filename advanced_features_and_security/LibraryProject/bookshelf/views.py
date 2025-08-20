from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
from .forms import ExampleForm
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
from django.contrib.auth.decorators import login_required
from .forms import BookSearchForm

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
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
@login_required
def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    if form.is_valid():
        query = form.cleaned_data['query']
        books = books.filter(title__icontains=query)  # Safe ORM query
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})
def book_list(request):
    # Example book list view (assuming Book model exists)
    books = Book.objects.all()  # Make sure you import Book if used
    return render(request, 'bookshelf/book_list.html', {'books': books})

# New view for ExampleForm
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., save to DB or print)
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            published_date = form.cleaned_data['published_date']
            # Example: just printing to console
            print(f"Received Book: {title} by {author}, published on {published_date}")
            return redirect('example_form')  # Redirect after POST
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})