from django.urls import path
from . import views

app_name='usuarios'

#URL DE APP USUARIOS - vista de clase, para cargarla se coloca .as_view()
urlpatterns = [
    path('registro/', views.Registro.as_view(), name="registro"), 
]
