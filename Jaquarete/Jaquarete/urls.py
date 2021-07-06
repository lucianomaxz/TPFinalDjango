from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Gestion_Productos/', include("Gestion_Productos.urls")),
]
