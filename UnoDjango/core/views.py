from django.shortcuts import render, redirect
# importamos los modelos a utilizar
from core.models import Author
from core.models import Book
from core.forms import AutorForm


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


def autor_update(request, pk=None):
    autor = Author.objects.get(pk=pk)
    return render(request, 'update_autor.html', {'author': autor})
