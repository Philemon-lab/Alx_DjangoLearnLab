from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Existing views (list_books, library_detail, role-based views, etc.)
# ...

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
