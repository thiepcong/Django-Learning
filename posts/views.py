from django.shortcuts import render
from django.http import HttpRequest,JsonResponse

# Create your views here.
def homepage(requests:HttpRequest):
    response={"message":"Hello Would"}
    return JsonResponse(data=response)