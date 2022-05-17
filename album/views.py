from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

from album.models import Fotos
from django.http import HttpResponse

@csrf_exempt 
def Upload (request): 

    print("veamos el metodo")
    print(request)
    if request.method == 'POST': 
        cantidad_imagenes=int (request.POST.get("cantidad"))
        print("****************************************")
        print("vemos la cantidad de imagenes que llego: ")
        print(cantidad_imagenes)
        print("****************************************")

        if (cantidad_imagenes==1):

            print("****************************************")
            print("vemos la cantidad de filas de imagenes: ")
            print(len(Fotos.objects.all()))
            print("****************************************")

            foto=request.POST.get("imagen0")
            descripcion=request.POST.get("descripcion")
            new=Fotos()
            new.numero=(len(Fotos.objects.all()))+1
            new.foto=foto
            #new.descripcion=descripcion
            new.save()
            return HttpResponse("ok") 
            
        else:

            print("****************************************")
            print("vemos la cantidad de filas de imagenes: ")
            print(len(Fotos.objects.all()))
            print("****************************************")

            for i in range(0, cantidad_imagenes):
                
                #descripcion=request.POST.get("descripcion")
                foto=request.POST.get("imagen"+str(i))
                new=Fotos()
                new.numero=len(Fotos.objects.all())+1
                new.foto=foto
                new.save()
                #new.descripcion=descripcion
                
            return HttpResponse("ok") 
    else:
        return HttpResponse("bad") 

def DownloadAll(request):
    print("veamos el metodo")
    print(request)
    if request.method == 'GET':
        print("llego a GET mi pana")
        return HttpResponse ("ok")
    else: 
        return HttpResponse("bad")  
        