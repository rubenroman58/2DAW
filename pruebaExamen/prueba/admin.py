from django.contrib import admin

from prueba.models import Author,Book #Modelo añadido a posteriori.
#Forma de registrar la tabla Author
admin.site.register(Author)
#Registramos las tabla Book
admin.site.register(Book)
