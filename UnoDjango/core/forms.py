from django import forms 
from core.models import Author 
from core.models import Book # importamos el modelo que nos hace falta, en este caso  necestimos insertar autores 
#Creamos nuestro primer Form 
class AutorForm (forms.ModelForm): #Vamos a crear un formulario de Django , basado en un  modelo, por eso hacemos la herencia  
 #Los forms de django tienen su clase meta, dónde indicamos el modelo al cual hacemos  referencia. 
 #Con estas dos clases lo que estamos diciendo es que Django debe crearnos un form que haga  referencia el modelo author 
 class Meta:  
    model=Author 
    fields='__all__' 
    
class BookForm (forms.ModelForm):  
   class Meta:  
      model=Book 
      fields='__all__' 
