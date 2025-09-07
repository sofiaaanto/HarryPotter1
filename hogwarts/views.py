from django.shortcuts import render

def home(request):
    return render(request, "hogwarts/home.html")

def libros(request):
    return render(request, "hogwarts/libros.html")

def peliculas(request):
    return render(request, "hogwarts/peliculas.html")

def personajes(request):
    return render(request, "hogwarts/personajes.html")

