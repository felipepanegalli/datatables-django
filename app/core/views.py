from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from faker import Faker
from .models import Usuario
from django.db.models import Q
import uuid


# Create your views here.


def index(request):
    search = request.GET.get('search') or ''
    usuarios = Usuario.objects.filter(Q(nome__contains=search) | Q(endereco__icontains=search)
                                      ).values('nome', 'endereco').order_by('nome')
    # Paginação
    usuarios_paginator = Paginator(usuarios, 50)
    usuarios_page = request.GET.get('page')
    usuarios = usuarios_paginator.get_page(usuarios_page)
    return render(request, 'index.html', {'usuarios': usuarios})


def faker_user(request, id):
    fake = Faker('pt-BR')
    for _ in range(id):
        Usuario.objects.create(
            id=uuid.uuid4(),
            nome=fake.name(),
            endereco=fake.address(),
        )
    return redirect('/')


def user_all(request):
    usuarios = Usuario.objects.all().values('nome', 'endereco', 'id')

    for usuario in usuarios:
        usuario['acoes'] = (
                '<div class="btn-group" role="group">'
                    '<a href="/user/view/' + str(usuario['id']) + '" class="btn btn-primary">Visualizar</a>'
                    '<a href="/user/edit/' + str(usuario['id']) + '" class="btn btn-warning">Editar</a>'
                    '<a href="/user/delete/' + str(usuario['id']) + '" class="btn btn-danger">Excluir</a>'
                '<div>'
        )

    # Paginação
    # usuarios_paginator = Paginator(usuarios, 50)
    # usuarios_page = request.GET.get('page')
    # usuarios = usuarios_paginator.get_page(usuarios_page)

    return JsonResponse(list(usuarios), safe=False)