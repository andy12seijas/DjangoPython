from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from myapp.models import *
from myapp.forms import *
# Create your views here.
def artista_listar(request):
    artista=Artista.objects.all()
    
    for i in artista:
        print(i)
    return  render(request,'artista/artistalistar.html',{
        'artista':artista,
        
    }) 
# myapp/views.py
def cancion_listar(request):
    cancion=Cancion.objects.all()
    for i in cancion:
        print(i)
    return render(request,'artista/cancionlistar.html',{'cancion':cancion} )    
def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mostrar')  
    else:
        form = CancionForm()
    
    return render(request, 'artista/add2.html', {'form': form})
def listar_todo(request):
    artista = Artista.objects.all()
    cancion = Cancion.objects.all()
    
    return render(request, 'artista/listar_todo.html', {
        'artista': artista,
        'cancion': cancion,
    })                

def crear_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            
            return redirect('/mostrar')  
    else:
        form = ArtistaForm()

        
      
    return render(request, 'artista/add.html', {'form': form  })

def actualizar_artista(request, pk):
    print(f"PK recibido: {pk}")
    artista = get_object_or_404(Artista, pk=pk)
    print(f"Artista obtenido: {artista}")
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('Mostrar todo')
    else:
        form = ArtistaForm(instance=artista)
    return render(request, 'artista/actualizar_artista.html', {'form': form})
     
        
def actualizar_cancion(request, id):
    cancion = get_object_or_404(Cancion, id=id)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('Mostrar todo')
    else:
        form = CancionForm(instance=cancion)
    return render(request, 'artista/actualizar_cancion.html', {'form': form})
def eliminar_artista(request,id):
        
    artista=get_object_or_404(Artista,id=id)
    if not artista:
     return HttpResponse('Hola')
   
    if request.method=='POST':
        artista.delete()
        return redirect('Mostrar todo')
    return render(request,'artista/confirmar_artista.html',{'artista':artista})
def eliminar_cancion(request, id):
    cancion = get_object_or_404(Cancion, id=id)
    if request.method == 'POST':
        cancion.delete()
        return redirect('Mostrar todo')
    return render(request, 'artista/confirmar_eliminar.html', {'cancion': cancion})        
        