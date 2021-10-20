import json
import time
from django.http.response import JsonResponse
from django.views.generic import DetailView, ListView, View
from post.models import Post
from post.utils import login_check
from user.models import User


class PostListView(ListView):
    model = Post
    
    def render_to_response(self, context,  **response_kwargs):
        posts = list(context['post_list'].values()) # values는 딕셔너리 형태로 풀어준다
        return JsonResponse({'posts':posts}, safe=False, status=200)


class PostCreateView(View):
    @login_check
    def post(self, request):
        data = json.loads(request.body)
        Post.objects.create(
            title = data['title'],
            content = data['content'],
            writer = User.objects.filter(id = request.user.id).first()
        )
        return JsonResponse({'message':'Success'}, status=200)


class PostUpdateView(View):
    @login_check
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(id = kwargs['id'])
        return JsonResponse({'post':list(post.values())}, status=200)
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        title = data['title']
        content = data['content']
        updated_at = time.time()
        Post.objects.filter(id = kwargs['id']).update(
            title = title,
            content = content,
            updated_at = updated_at,
        )
        return JsonResponse({'message':'post 수정 성공'}, status=200)


class PostDeleteView(View):
    @login_check
    def get(self, request, *args, **kwargs):
        Post.objects.get(id = kwargs['id']).delete()
        return JsonResponse({'message':'post 삭제 성공'}, status=200)


class PostDetailView(DetailView):
    model = Post
    
    def post_detail_view(request, pk):
        post = Post.objects.get(pk = pk)
        return JsonResponse({'post':post}, safe=False, status=200)

