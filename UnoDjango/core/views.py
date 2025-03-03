from django.shortcuts import render, redirect
# importamos los modelos a utilizar
from core.models import Author
from core.models import Book
from core.forms import AutorForm
from core.forms import BookForm
from django.contrib import messages


# def home (request):
# autor=Author.objects.all()

#   return render(request,'core/index.html',{'authors':autor})
def home(request):

    # return render(request,'index.html',{'authors':autor})
    return render(request, 'core/index.html', {'books': Book})


def autor_list(request):
    autor = Author.objects.all()
    return render(request, 'core/autor.html', {'authors': autor})


def libro_list(request):
    libro = Book.objects.all()
    return render(request, 'core/libro.html', {'books': libro})


def autor_create(request):
    if request.method == 'GET':
        return render(request, 'core/create_autor.html', {'autor_form': AutorForm})

    if request.method == 'POST':
        form = AutorForm(data=request.POST)
    if form.is_valid:
        form.save()
        print('tttttt')
        return redirect('/autor/')
    else:
        form = AutorForm(data=request.POST)
        return render(request, 'core/create_autor.html', {'autor_form': AutorForm})


def autor_update (request, pk=None):
    autor=Author.objects.get(pk=pk) 
    if request.method == 'GET':
        author_form=AutorForm(instance=autor) 
        return render (request,'core/update_autor.html',{'author':autor,'author_form':author_form}) 

    if request.method == 'POST':
        author_form=AutorForm(data=request.POST, instance=autor) 


    if author_form.is_valid():
        author_form.save()
        return redirect ('/autor/')
    else: 
        author_form=AutorForm(data=request.POST, instance=autor)
        return render (request,'core/update_autor.html',{'author':autor,'author_form':author_form})
    
def autor_delete (request, pk=None):

    Author.objects.filter(pk=pk).delete()
    messages.success(request, 'El autor ha sido eliminado')

    return redirect ('/autor/')

def book_create(request):
    if request.method == 'POST':
        # Creamos el formulario con los datos POST
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            # Guardamos el formulario si es válido
            book_form.save()
            messages.success(request, 'El libro ha sido registrado exitosamente.')
            return redirect('/libro/')  # Redirigir a la lista de libros
        else:
            # Si el formulario no es válido, lo mostramos con los errores
            messages.error(request, 'Hay un error en el formulario. Intenta nuevamente.')
    else:
        # Si es un GET, mostramos el formulario vacío
        book_form = BookForm()

    return render(request, 'core/create_libro.html', {'book_form': book_form})
