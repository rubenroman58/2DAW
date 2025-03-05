from django.db import models

class Author (models.Model):

    name = models.CharField(verbose_name='Nombre',  # etiqueta dentro de la tabla
                            max_length=100,
                            default=''
                            )
    last_name = models.CharField(verbose_name='Apellido',
                                 max_length=150,
                                 default='')
    age = models.PositiveSmallIntegerField(verbose_name='Edad',
                                           )


    def __str__(self):
        return f'{self.name} {self.last_name} {self.age}'


class Book (models.Model):

    title = models.CharField('Título del libro', max_length=255, unique=True)

    cod = models.CharField('Codigo', max_length=15, unique=True)
    author = models.ManyToManyField(Author)
    def __str__(self):
            return f'{self.title} {self.cod}'
