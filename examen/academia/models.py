from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(verbose_name='nombre',
                                 max_length=150,
                                 default='')
    descripcion= models.TextField(verbose_name='descripcion',
                                           )


    def __str__(self):
        return f' {self.nombre} {self.descripcion}'
    
class Estudiante(models.Model):

   
    nombre = models.CharField(verbose_name='nombre',
                                 max_length=100,
                                 default='')
    email= models.EmailField(verbose_name='email',
                                           )


    def __str__(self):
        return f' {self.nombre} {self.email}'
    
class Inscripcion (models.Model):
                     
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    curso= models.ForeignKey('Curso', on_delete=models.CASCADE)
    fecha_inscripcion= models.DateField(auto_now_add=True) 


    def __str__(self):
        return f' {self.estudiante} {self.curso} {self.fecha_inscripcion}'
    

    
    

    
