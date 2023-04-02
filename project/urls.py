from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social-auth/', include('allauth.urls')),
    path('', include("accounts.urls"))
]
