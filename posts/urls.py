from . import views
from django.urls import path

# urlpatterns = [
#     path("homepage/",views.homepage,name="posts_home"),
#     path("",views.PostListCreateView.as_view(),name="list_posts"),
#     path("<int:post_id>",views.post_detail,name="post_detail"),
#     path("update/<int:post_id>/",views.update_post,name="update_post"),
#     path("delete/<int:post_id>/",views.delete_post,name="delete_post")
# ]

urlpatterns = [
    path("homepage/",views.homepage,name="posts_home"),
    path("",views.PostListCreateView.as_view(),name="list_posts"),
    path("<int:pk>",
        views.PostRetrieceUpdateDeleteView.as_view(),
        name="post_detail",
    ),
    path('current_user/',views.get_posts_for_current_user,name="current_user")
]