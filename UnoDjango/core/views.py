from django.shortcuts import render
#importamos los modelos a utilizar
from core.models import Author
from core.models import Book
#def home (request):
##   autor=Author.objects.all() 

 #   return render(request,'core/index.html',{'authors':autor}) 
def home (request):

    book=Book.objects.all()
    #return render(request,'index.html',{'authors':autor}) 

    return render(request,'core/index.html',{'books':book})