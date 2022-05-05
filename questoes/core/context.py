
from core.models import *


def menuItens(request):
    mainItens = Disciplina.objects.all()

    return {"mainItens": mainItens}
