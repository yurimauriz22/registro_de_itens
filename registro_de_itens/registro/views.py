from django.http import HttpResponse


def index(request):
    return HttpResponse("Começando o projeto de registro de itens")