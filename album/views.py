from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from album.models import Fotos
from django.http import HttpResponse
from django.http import JsonResponse
import base64

@csrf_exempt 
def Upload (request): 

    if request.method == 'POST': 
        cantidad_imagenes=int (request.POST.get("cantidad"))

        if (cantidad_imagenes==1):

            foto=request.FILES.get("imagen0")
            descripcion=request.POST.get("descripcion")
            new=Fotos()
            new.numero=len(Fotos.objects.all())+1
            new.categoria="genérica"
            new.descripcion="descripción genérica"
            new.foto=foto
            new.save()
            return HttpResponse("ok") 
            
        else:

            for i in range(0, cantidad_imagenes): 
                #descripcion=request.POST.get("descripcion")
                foto=request.FILES.get("imagen"+str(i))
                new=Fotos()
                new.numero=len(Fotos.objects.all())+1
                new.categoria="genérica"
                new.descripcion="descripción genérica"
                new.foto=foto
                new.save()
                #new.descripcion=descripcion
                
            return HttpResponse("ok") 
    else:
        return HttpResponse("bad") 

def DownloadAll(request):
    if request.method == 'GET':
        album= Fotos.objects.filter(numero__lte=100) #que busque todas las fotos hasta la 100        
        if album:
            array=[]
            for data in album:
                if data.foto:
                    foto={"numero":data.numero,"foto":"data:image/png;base64,"+base64.b64encode(data.foto.read()).decode('ascii'), "descripcion:":data.descripcion} 
                    array.append(foto)
            if len(array)>0: 
                return JsonResponse(array, safe=False)
            else: 
                return HttpResponse("sin fotos")

        else: 
            return HttpResponse ("bad")
    else: 
        return HttpResponse("bad")  
        