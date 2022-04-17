from django.urls import path
from .views import postList, postDetail, postCreate, postUpdate, postDelete

urlpatterns = [
    path('post_list/', postList, name='post_list'),
    path('post_detail/<int:pk>', postDetail, name='post_detail'),
    path('post_create/', postCreate, name='post_create'),
    path('post_update/<int:pk>', postUpdate, name='post_update'),
    path('post_delete/<int:pk>', postDelete, name='post_delete'),
]
