from django.urls import path
from . import views



app_name='noticias'

#URL DE APP NOTICIAS
urlpatterns = [
    path('', views.inicio, name="inicio"),

    #url para el detalle de la noticia por pk
    path('detalle<int:pk>', views.Detalle_Noticias, name='detalle'),

    #url del formulario de contacto
    path('contacto', views.contacto, name='contacto'),

    #url comentario
    path('comentario', views.Comentar_Noticia, name='comentar')
]
