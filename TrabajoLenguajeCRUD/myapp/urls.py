from django.urls import path
from myapp.views import *
urlpatterns = [
    
    
    path('artista/add/',crear_artista,name="Crear Artista"),
  
    path('cancion/add2',crear_cancion,name="Crear cancion"),
    path('mostrar/',listar_todo,name="Mostrar todo"),
    path('cancion/actualizar/<int:id>/', actualizar_cancion, name='actualizar_cancion'),  
    path('cancion/eliminar/<int:id>/', eliminar_cancion, name='eliminar_cancion'),
    path('artista/eliminar/<int:id>/',eliminar_artista,name='eliminar_artista'),
    path('artista/actualizar/<int:pk>/',actualizar_artista,name='actualizar artista')
    
]
