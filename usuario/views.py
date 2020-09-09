from django.shortcuts import render


def editarPerfil(request):
    return render(request, 'usuario/EditarPerfil.html', {
    })


def favoritos(request):
    return render(request, 'usuario/favoritos.html', {
    })


def cadastro_usuario1(request):
    return render(request, 'usuario/usuario_cadastro_parte_1.html', {
    })


def cadastro_usuario2(request):
    return render(request, 'usuario/usuario_cadastro_parte_2.html', {
    })
