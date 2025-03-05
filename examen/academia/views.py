from django.shortcuts import render,redirect
from academia.models import Curso
from academia.models import Estudiante
from academia.models import Inscripcion
from academia.forms import AutorForm
from django.contrib import messages

# Create your views here.

def home(request):

    # return render(request,'index.html',{'authors':autor})
    return render(request, 'index.html')

def estudiante_list(request):
    autor = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'authors': autor})

def inscripciones_list(request):
    autor = Inscripcion.objects.all()
    inscripcion2=Curso.objects.all()
    return render(request, 'inscripciones.html', {'authors': autor,'inscripcion': inscripcion2})

def estudiante_create(request):
    if request.method == 'GET':
        return render(request, 'crear_estudiante.html', {'autor_form': AutorForm})

    if request.method == 'POST':
        form = AutorForm(data=request.POST)
    if form.is_valid:
        form.save()
        return redirect('/estudiantes/')
    else:
        form = AutorForm(data=request.POST)
        return render(request, 'crear_estudiante.html', {'autor_form': AutorForm})


def estudiante_update (request, pk=None):
    autor=Estudiante.objects.get(pk=pk) 
    if request.method == 'GET':
        author_form=AutorForm(instance=autor) 
        return render (request,'editar_estudiante.html',{'author':autor,'author_form':author_form}) 

    if request.method == 'POST':
        author_form=AutorForm(data=request.POST, instance=autor) 


    if author_form.is_valid():
        author_form.save()
        return redirect ('/estudiantes/')
    else: 
        author_form=AutorForm(data=request.POST, instance=autor)
        return render (request,'editar_estudiante.html',{'author':autor,'author_form':author_form})
    
    
def estudiante_delete (request, pk=None):
    Estudiante.objects.filter(pk=pk).delete()
    
    return redirect ('/estudiantes/')