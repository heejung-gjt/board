from django.urls import path, include
from post.views import PostListView

urlpatterns = [
    path('user/', include('user.urls')),
    path('post/', include('post.urls')),
]
