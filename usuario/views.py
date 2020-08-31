from django.shortcuts import render


def editarPerfil(request):
    return render(request, 'usuario/EditarPerfil.html', {
        })
