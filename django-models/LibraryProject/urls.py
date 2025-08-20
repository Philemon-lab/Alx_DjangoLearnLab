from django.urls import path, include

urlpatterns = [
    path('relationship_app/', include('relationship_app.urls')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('relationship_app.urls')),  # authentication URLs
]
