from django.urls import path
from . import views

urlpatterns = [
    # --- Function-based view for listing books ---
    path('books/', views.list_books, name='list_books'),

    # --- Class-based view for Library details ---
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # --- Authentication views ---
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # --- Role-based access control views ---
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
