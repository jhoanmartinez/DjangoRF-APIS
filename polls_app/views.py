from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

# Create your views here.

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {
        "results": list
                        (polls.values(
                            #mismos nombres del modelo
                            "question", 
                            "created_by",
                            "pub_date")
                        )
                        }

    return JsonResponse(data)

def polls_detail(request, pk):
    pass