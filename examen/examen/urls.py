"""
URL configuration for examen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from academia.views import home,estudiante_list,estudiante_create,estudiante_update,estudiante_delete,inscripciones_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('estudiantes/', estudiante_list),
    path('new-estudiante/', estudiante_create),
    path('editar_estudiante/<int:pk>', estudiante_update),
    path('eliminar_estudiante/<int:pk>', estudiante_delete),
    path('inscripciones/',inscripciones_list)

   
]
