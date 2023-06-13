from django.http.response import JsonResponse # Para poder retornar un Json.
from django.utils.decorators import method_decorator # Para poder usar el decorador @method_decorator.
from django.views import View
from django.views.decorators.csrf import csrf_exempt # para poder saltarse el csrf_exempt.
from .models import Company
import json # Modulo json

# Create your views here.

class CompanyView(View):
    
    # Este es un metodo que se ejecuta cada vez que hacemos una peticion, es un metodo de view que se sobreescribe .
    @method_decorator(csrf_exempt) # Esto es para que nos salte esta restriccion.
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id=0):
        if (id > 0): # Si hacemos la busqueda de una sola.
            companies=list(Company.objects.filter(id=id).values()) # Filtramos para obtener uno mediante id y accedemos a values para que lo pueda convertir.
            if len(companies) > 0:
                company=companies[0]
                datos = {'message':"Success",'company':company}
            else:
                datos = {'message':"Company not found..."}
            return JsonResponse(datos)
                
        else: # Sino hacemos el listado de todas.
            companies = list(Company.objects.values()) # De esta manera se va a convertir en algo que python entienda para serializar a json.
            if len(companies) > 0: # Si la longitud de companies es mayor a 0.
                datos = {'message':"Success", 'companies':companies}
            else:
                datos = {'message':"Companies not found..."}
            return JsonResponse(datos) # Retornamos datos en forma de json.
            
            
    def post(self,request):
        #print(request.body)
        jd = json.loads(request.body) # Cargar un json a traves de request.body, lo convierte a diccionario de python para extraer los datos y poder utilizarlos.
        #print(jd)
        Company.objects.create(name=jd['name'],website=jd['website'], foundation=jd['foundation']) # Para crear un nuevo elementocon los datos extraidos de jd.
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
    
    def put(self,request,id):
        jd = json.loads(request.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id) # Get si no lo encuentra te va a lanzar una excepcion.
            # Vamos a actualizar los datos.
            company.name=jd['name']
            company.website=jd['website']
            company.foundation=jd['foundation']
            company.save() # Para guardar los cambios.
            datos = {'message':"Success"}
        else:
            datos = {'message':"Companies not found..."}
        return JsonResponse(datos)
    
            
    def delete(self,request,id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete() # Me permite eliminar.
            datos = {'message':"Success"}
        else:
            datos = {'message':"Companies not found..."}
        return JsonResponse(datos)
            
        
