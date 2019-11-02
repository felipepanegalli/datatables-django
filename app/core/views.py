from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from faker import Faker
from core.models import Usuario


# Create your views here.


def index(request):
    usuarios = Usuario.objects.all().values('nome', 'endereco')
    # Paginação
    usuarios_paginator = Paginator(usuarios, 50)
    usuarios_page = request.GET.get('page')
    usuarios = usuarios_paginator.get_page(usuarios_page)
    return render(request, 'index.html', {'usuarios': usuarios})


def faker_user(request):
    fake = Faker()
    for _ in range(10000):
        Usuario.objects.create(
            nome=fake.name(),
            endereco=fake.address(),
        )


def user_all(request):
    usuarios = Usuario.objects.all().values('nome', 'endereco')
    # Paginação
    usuarios_paginator = Paginator(usuarios, 50)
    usuarios_page = request.GET.get('page')
    usuarios = usuarios_paginator.get_page(usuarios_page)

    return JsonResponse(list(usuarios), safe=False)
