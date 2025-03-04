from django.db import models

# Create your models here.

class Author (models.Model):

    first_name = models.CharField(verbose_name='Nombre',  # etiqueta dentro de la tabla
                            max_length=100,
                            default=''
                            )
    last_name = models.CharField(verbose_name='Apellido',
                                 max_length=150,
                                 default='')
    birth_date= models.DateField(verbose_name='Edad',
                                           )


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date}'
    

class Publisher (models.Model):

    name = models.CharField(verbose_name='Nombre',  # etiqueta dentro de la tabla
                            max_length=100,
                            default=''
                            )
    address = models.CharField(verbose_name='Direccion',
                                 max_length=150,
                                 default='')
    city= models.CharField(verbose_name='Ciudad',
                                 max_length=150,
                                 default='')
    
    state_province= models.CharField(verbose_name='Provincia',
                                 max_length=150,
                                 default='')
    country= models.CharField(verbose_name='Pais',
                                 max_length=150,
                                 default='')
    
    website= models.URLField(verbose_name='Url',
                                 max_length=150,
                                 default='')

    def __str__(self):
        return f'{self.name} {self.address} {self.city} {self.state_province}{self.country}{self.website}'


class Book(models.Model):
    title = models.CharField(max_length=255)  # Título del libro
    authors = models.ManyToManyField(Author)  # Relación de muchos a muchos con Author
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # Relación de muchos a uno con Publisher
    publication_date = models.DateField()  # Fecha de publicación

    def __str__(self):
        return self.title
    
class Loan(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)  # Relación con Book
    borrower = models.CharField(max_length=100)  # Nombre del prestatario
    loan_date = models.DateField()  # Fecha de préstamo
    return_date = models.DateField()  # Fecha de devolución

    def __str__(self):
        return f" {self.book}  {self.borrower}"

