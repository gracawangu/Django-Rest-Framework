from django.urls import path
from . import views 
from .views import PostListApi, PostCreateApi, PostDetailApi, PostUpdateApi, PostDeleteApi

app_name = 'links'

urlpatterns = [
    path('create/', views.PostCreateApi.as_view(), name='api_create'),
    path('update/<int:pk>', views.PostUpdateApi.as_view(), name='api_update'),
    path('delete/<int:pk>', views.PostDeleteApi.as_view(), name='api_delete'),
    path('', views.PostListApi.as_view(), name="api_list"),
    path('read/<int:pk>', views.PostDetailApi.as_view(), name='api_detail'),
]
