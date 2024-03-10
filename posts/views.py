# from django.shortcuts import render
# from django.http import HttpRequest,JsonResponse

# # Create your views here.
# def homepage(requests:HttpRequest):
#     response={"message":"Hello Would"}
#     return JsonResponse(data=response)

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAuthenticatedOrReadOnly,IsAdminUser
from rest_framework import status,generics,mixins
from rest_framework.decorators import api_view,APIView,permission_classes
from .models import Post
from .serializes import PostSerializer
from django.shortcuts import get_object_or_404
from accounts.serializers import CurrentUserPostsSerializer
from .permissions import ReadOnly,AuthorOrReadOnly

@api_view(http_method_names=["GET","POST"])
@permission_classes([AllowAny])
def homepage(request:Request):
    if request.method == "POST":
        data = request.data
        
        response = {"Message":"Hello Would","data":data}

        return Response(data=response,status=status.HTTP_201_CREATED)
    response = {"Message":"Hello Would"}
    return Response(data=response,status=status.HTTP_200_OK)


# @api_view(http_method_names=["GET","POST"])
# def list_posts(request:Request):
#     posts = Post.objects.all()

#     if request.method=="POST":
#         data = request.data

#         serializer = PostSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {
#                 "message": "Post is created",
#                 "data": serializer.data
#             }

#             return Response(data=response,status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.error,status=status.HTTP_400_BAD_REQUEST)

#     serializer  = PostSerializer(instance=posts,many=True)

#     response = {
#         "message": "posts",
#         "data": serializer.data,
#     }

#     return Response(data=response,status=status.HTTP_200_OK)
# class PostListCreateView(APIView):
#     """
#         a view for creating and listing posts
#     """
#     serializer_class = PostSerializer

#     def get(self,request:Request,*args,**kwargs):
#         posts = Post.objects.all()

#         serializer = self.serializer_class(instance=posts,many=True)

#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     def post(self,request:Request,*args,**kwargs):
#         data = request.data

#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {
#                 "message": "Post Created",
#                 "data": serializer.data
#             }

#             return Response(data =response, status=status.HTTP_201_CREATED )



# class PostRetrieceUpdateDeleteView(APIView):
#     serializer_class = PostSerializer

#     def get(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)

#         serializer = self.serializer_class(instance=post)

#         return Response(data=serializer.data,status=status.HTTP_200_OK)

#     def put(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)

#         data = request.data

#         serializer = self.serializer_class(instance=post,data=data)

#         if serializer.is_valid():
#             serializer.save()

#             response = {
#                 "message": "Post is updated successfully",
#                 "data": serializer.data
#             }

#             return Response(data=response,status=status.HTTP_200_OK)
        
#         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request:Request,post_id:int):
#         post = get_object_or_404(Post,pk=post_id)
    
#         post.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)
class PostListCreateView(
        generics.GenericAPIView,
        mixins.ListModelMixin,
        mixins.CreateModelMixin
    ):
    """
        a view for creating and listing posts
    """

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)

    def get(self,request:Request,*args,**kwargs):
        return self.list(self,*args,**kwargs)

    def post(self,request:Request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class PostRetrieceUpdateDeleteView(
        generics.GenericAPIView,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
    ):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self,request:Request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request:Request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request:Request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request:Request):
    user = request.user

    serializer = CurrentUserPostsSerializer(instance=user,context={"request":request})

    return Response(data=serializer.data,status=status.HTTP_200_OK)

# @api_view(http_method_names=["GET"])
# def post_detail(request:Request,post_id:int):
#     post = get_object_or_404(Post,pk=post_id)

#     serializer = PostSerializer(instance=post)

#     response = {
#         "message": "post",
#         "date": serializer.data
#     }

#     return Response(data=response,status=status.HTTP_200_OK)

# @api_view(http_method_names=["GET"])
# def get_post_by_id(request:Request,post_id:int):
#     pass

# @api_view(http_method_names=["PUT"])
# def update_post(request:Request,post_id:int):
#     post = get_object_or_404(Post,pk=post_id)

#     data = request.data

#     serializer = PostSerializer(instance=post,data=data)

#     if serializer.is_valid():
#         serializer.save()

#         response = {
#             "message": "Post is updated successfully",
#             "data": serializer.data
#         }

#         return Response(data=response,status=status.HTTP_200_OK)
    
#     return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=["DELETE"])
# def delete_post(request:Request,post_id:int):
#     post = get_object_or_404(Post,pk=post_id)
    
#     post.delete()

#     return Response(status=status.HTTP_204_NO_CONTENT)
