from django.contrib import admin
from library.models import Author,Book,Publisher,Loan #Modelo añadido a posteriori.
#Forma de registrar la tabla Author
admin.site.register(Author)
#Registramos las tabla Book
admin.site.register(Book)

admin.site.register(Publisher)
admin.site.register(Loan)