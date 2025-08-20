from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # We’ll create a form shortly

# List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# Add a new book
@permission_required('bookshelf.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

# Edit an existing book
@permission_required('bookshelf.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

# Delete a book
@permission_required('bookshelf.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
