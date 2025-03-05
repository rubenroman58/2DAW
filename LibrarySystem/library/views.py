from django.shortcuts import render,redirect,get_object_or_404
from library.models import Author
from library.forms import AutorForm
from django.contrib import messages

# Create your views here.

def autor_list(request):
    autor = Author.objects.all()
    return render(request, 'autores.html', {'authors': autor})

def home (request):  
 return render(request,'index.html')  


def autor_create(request):
    if request.method == 'GET':
        return render(request, 'create_autor.html', {'autor_form': AutorForm})

    if request.method == 'POST':
        form = AutorForm(data=request.POST)
    if form.is_valid:
        form.save()
        return redirect('/autores/')
    else:
        form = AutorForm(data=request.POST)
        return render(request, 'create_autor.html', {'autor_form': AutorForm})
    
    
def autor_datos(request, pk):
   
    autor = get_object_or_404(Author, pk=pk)
    
    return render(request, 'author_detail.html', {'autor': autor})

def autor_delete (request, pk=None):

    Author.objects.filter(pk=pk).delete()
    messages.success(request, 'El autor ha sido eliminado')

    return redirect ('/autores/')

def autor_update (request, pk=None):
    autor=Author.objects.get(pk=pk) 
    if request.method == 'GET':
        author_form=AutorForm(instance=autor) 
        return render (request,'update_autor.html',{'author':autor,'author_form':author_form}) 

    if request.method == 'POST':
        author_form=AutorForm(data=request.POST, instance=autor) 


    if author_form.is_valid():
        author_form.save()
        return redirect ('/autores/')
    else: 
        author_form=AutorForm(data=request.POST, instance=autor)
        return render (request,'update_autor.html',{'author':autor,'author_form':author_form})
    