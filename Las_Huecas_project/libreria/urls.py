from django.urls import path #para acceder a las vistas
from . import views #para tener acceso a las vistas
#¿cual solicitud se va hacer y a q vista vamos a entrar?
from django.conf import settings
from django.contrib.staticfiles.urls import static
#Rutas para Acceder a la vista
urlpatterns = [ 
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('libros/', views.libros, name='libros'),
    path('libros/crear/', views.crear_libro, name='crear'),
    path('libros/editar/', views.editar_libro, name='editar'),
    path('eliminar/<int:id>', views.eliminar_libro, name='eliminar'),
    path('libros/editar<int:id>', views.editar_libro, name='editar'),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
