from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

# Create your views here.

def polls_home(request):
    welcome = {
        "saludo":"Bienvenido al homepage"
    }
    return JsonResponse(welcome)


# def polls_list(request):
#     MAX_OBJECTS = 20
#     polls = Poll.objects.all()[:MAX_OBJECTS]
#     data = {
#         "results": list
#                         (polls.values(
#                             #mismos nombres del modelo
#                             "id",
#                             "question", 
#                             "created_by",
#                             "pub_date")
#                         )
#             }
#     return JsonResponse(data)

# def polls_detail(request, pk):
#     poll = get_object_or_404(Poll, pk=pk)
#     data =  {"results": {
#                         "id":pk,
#                         "question":poll.question,
#                         "created_by":poll.created_by.username,
#                         "pub_date":poll.pub_date
#                         }}
#     return JsonResponse(data)
