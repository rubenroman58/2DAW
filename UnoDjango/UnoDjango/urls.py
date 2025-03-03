"""
URL configuration for UnoDjango project.

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
#from core.views import home
from core.views import home,autor_list,book_create,libro_list,autor_create,autor_update,autor_delete
#from . import views 
urlpatterns = [
#path('hola/', views.index),



    path('', home), #quí no habría que meter la carpeta
    #path('otramas/', views.home),
    path('admin/', admin.site.urls),
    path('autor/',autor_list),
    path('libro/',libro_list),
    path('', home, name='index'),
    path ('new-autor/',autor_create), 
    path ('update-autor/<int:pk>',autor_update),
    path ('delete-autor/<int:pk>',autor_delete),
    path ('new-libro/',book_create)  
 ]