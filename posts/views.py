# from django.shortcuts import render
# from django.http import HttpRequest,JsonResponse

# # Create your views here.
# def homepage(requests:HttpRequest):
#     response={"message":"Hello Would"}
#     return JsonResponse(data=response)

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

posts = [
    {
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    },{
        "glossary": {
            "title": "example glossary",
            "GlossDiv": {
                "title": "S",
                "GlossList": {
                    "GlossEntry": {
                        "ID": "SGML",
                        "SortAs": "SGML",
                        "GlossTerm": "Standard Generalized Markup Language",
                        "Acronym": "SGML",
                        "Abbrev": "ISO 8879:1986",
                        "GlossDef": {
                            "para": "A meta-markup language, used to create markup languages such as DocBook.",
                            "GlossSeeAlso": ["GML", "XML"]
                        },
                        "GlossSee": "markup"
                    }
                }
            }
        }
    }
]

@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        
        response = {"Message":"Hello Would","data":data}

        return Response(data=response,status=status.HTTP_201_CREATED)
    response = {"Message":"Hello Would"}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names="GET")
def list_posts(request:Request):
    return Response(data=posts,status=status.HTTP_200_OK)

@api_view(http_method_names="GET")
def post_details(request:Request,post_index:int):
    post = posts[post_index]
    if post:
        return Response(data=post,status=status.HTTP_200_OK)
    return Response(data={"error":"Not found"},status=status.HTTP_400_BAD_REQUEST)