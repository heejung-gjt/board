from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name= 'post_list'),
    path('<int:id>/', PostDetailView.as_view(), name= 'post'),
    path('create/', PostCreateView.as_view(), name= 'post_create'),
    path('<int:id>/update/', PostUpdateView.as_view(), name= 'post_update'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name= 'post_delete'),
]
