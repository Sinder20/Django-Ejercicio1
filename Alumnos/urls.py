"""Alumnos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Alumno.views import FormularioAlumnoView
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),
    path('registro/', HomeView.registro, name='formularioAlumno'),
    path('registrarAlumno/', FormularioAlumnoView.index, name='registrarAlumno'),
    path('guardarAlumno/', FormularioAlumnoView.procesar_formulario, name='guardarAlumno'),
    path('listarAlumno/', FormularioAlumnoView.listar_alumnos, name='listarAlumnos'),
    path('editarAlumnos/<int:id_alumno>', FormularioAlumnoView.edit, name='editarAlumnos'),
    path('actualizarAlumnos/<int:id_alumno>', FormularioAlumnoView.actualizar_alumno, name='actualizarAlumno'),
    path('eliminarAlumnos/<int:id_alumno>', FormularioAlumnoView.delete, name='eliminarAlumno'),
]