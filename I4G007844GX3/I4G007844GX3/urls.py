"""I4G007844GX3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from links import views
from links.views import PostListApi, PostCreateApi, PostDetailApi, PostUpdateApi, PostDeleteApi
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/links/', include('links.urls')),
    path('create/', views.PostCreateApi.as_view(), name='api_create'),
    path('update/<int:pk>', views.PostUpdateApi.as_view(), name='api_update'),
    path('delete/<int:pk>', views.PostDeleteApi.as_view(), name='api_delete'),
    path('', views.PostListApi.as_view(), name="api_list"),
    path('read/<int:pk>', views.PostDetailApi.as_view(), name='api_detail'),
]
