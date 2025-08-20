from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library, Book, UserProfile
from .forms import RegisterForm


# =========================
# Library Views
# =========================

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"


def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# =========================
# Authentication Views
# =========================

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list_books")
        else:
            return HttpResponse("Invalid credentials")
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


# =========================
# Role-Based Access Control Views
# =========================

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"


def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"


def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")
