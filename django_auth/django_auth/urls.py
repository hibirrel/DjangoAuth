from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('users.urls')),  # важно: внутри path() — только include(...)
    path('accounts/', include('django.contrib.auth.urls')),
]