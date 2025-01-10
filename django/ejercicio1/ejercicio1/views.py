from django.http import HttpResponse
def index (request): # El request captura las peticiones de los clientes
    return HttpResponse ("<h1>hola mundo</h1>")

