from django.http import HttpResponse #Necesario para poder responder al cliente
#con httpresponse, podemos responder con texto plano o con html
#forma de responder al cliente cuando hace un http
def index (request): # El request captura las peticiones de los clientes
 return HttpResponse ("<h1>hola mundo</h1>")