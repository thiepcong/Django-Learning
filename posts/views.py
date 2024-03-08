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
from .models import Post
from .serializes import PostSerializer
from django.shortcuts import get_object_or_404

@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        
        response = {"Message":"Hello Would","data":data}

        return Response(data=response,status=status.HTTP_201_CREATED)
    response = {"Message":"Hello Would"}
    return Response(data=response,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET","POST"])
def list_posts(request:Request):
    posts = Post.objects.all()

    if request.method=="POST":
        data = request.data

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "Post is created",
                "data": serializer.data
            }

            return Response(data=response,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)

    serializer  = PostSerializer(instance=posts,many=True)

    response = {
        "message": "posts",
        "data": serializer.data,
    }

    return Response(data=response,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)

    serializer = PostSerializer(instance=post)

    response = {
        "message": "post",
        "date": serializer.data
    }

    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def get_post_by_id(request:Request,post_id:int):
    pass

@api_view(http_method_names=["PUT"])
def update_post(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)

    data = request.data

    serializer = PostSerializer(instance=post,data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "message": "Post is updated successfully",
            "data": serializer.data
        }

        return Response(data=response,status=status.HTTP_200_OK)
    
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["DELETE"])
def delete_post(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    
    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
