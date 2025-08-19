from django.contrib import admin
from .models import Author, Book, Library, Librarian

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
admin.site.register(Book, BookAdmin)

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Library, LibraryAdmin)

class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
admin.site.register(Librarian, LibrarianAdmin)