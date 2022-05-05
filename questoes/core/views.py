
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render

from core.models import *

# Create your views here.


def index(request):
    context = {'questoes': Questao.objects.all()}
    return render(request, "index.html", context)


def disciplina(request, disciplina):
    context = {'questoes': Questao.objects.filter(
        disciplines__name__icontains=disciplina)}
    return render(request, "index.html", context)


def busca(request, page):
    field_search = request.GET.get("termo")
    settings.BOLD = field_search

    if field_search is not None:
        searchResult = Questao.objects.filter(
            Q(disciplines__name__icontains=field_search)
            | Q(theme__icontains=field_search)
            | Q(grade__icontains=field_search)
            | Q(statement__icontains=field_search)
        ).order_by("-modified_at")

    result_obj_blog, qnt, intervalo = paginator(page, searchResult)

    total_qnt = (
        0 + qnt
    )
    total_intervalo = joinRange(
        intervalo, intervalo, total_qnt
    )

    total_qnt = qnt_page(total_qnt, qnt)
    total_intervalo = joinRange(total_intervalo, intervalo, total_qnt)

    if page > 4:
        total_intervalo = range(total_intervalo[0], total_intervalo[-1] + 2)

    if page < 4 and total_intervalo[-1] == total_qnt:
        total_intervalo = range(total_intervalo[0], total_qnt + (1))

    elif total_intervalo[-1] == total_qnt:
        total_intervalo = range(total_intervalo[0], total_intervalo[-1])

    if (searchResult):
        context = {
            "questoes": searchResult,
            "pag": page,
            "search": field_search,
            "status": "sucesso",
            "total": total_qnt,
            "rng": total_intervalo,
        }

        return render(request, "core.search.html", context)
    else:
        context = {
            "status": "atenção",
            "msg": "Nenhum resultado encontrado para a busca!",
        }

        return render(request, "core.search.html", context)


def paginator(page, all_objects):

    num_obj = len(all_objects)

    if num_obj <= 5:
        num_pag = 1
    else:
        num_pag = int(num_obj / 5)
        if num_obj % 5 != 0:
            num_pag = int(num_obj / 5) + 1

    if page <= 4 and num_pag < page + 3:
        inter = range(1, num_pag + 1)

    elif page <= 4 and num_pag > page + 3:
        inter = range(1, page + 3)

    else:
        if page + 3 >= num_pag:
            inter = range(page - 2, num_pag)

        else:
            inter = range(page - 2, page + 2)

    result_page = all_objects[((page - 1) * 5): ((page) * 5)]

    return result_page, num_pag, inter


def joinRange(rng1, rng2, qnt_page):
    # total_intervalo = joinRange(total_intervalo, intervalo, total_qnt)

    if rng2 != range(1, 1) and rng1 != range(1, 1):

        if rng1[0] <= rng2[0]:
            rng = rng1

        else:
            rng = rng2

        if rng1[-1] >= rng2[-1]:
            rng = range(rng[0], rng1[-1] + 1)
        else:
            rng = range(rng[0], rng2[-1] + 1)

        return rng
    else:

        if rng1 == range(1, 1):

            return rng2
        elif rng2 == range(1, 1):

            return rng1


# retorna a quantidade de pagina total, quando uma for maior que a outra
def qnt_page(qnt_ant, qnt_pos):

    if qnt_ant > qnt_pos:
        return qnt_ant
    else:
        return qnt_pos
