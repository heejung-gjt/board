import json
import time
from django.http.response import JsonResponse
from django.views.generic import View
from post.models import Post
from post.utils import login_check
from user.models import User


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


class PostListView(View):
    
    def get(self, request, *args, **kwargs):
        limit = int(request.GET.get('limit', 10))
        offset = int(request.GET.get('offset', 0))
        posts = Post.objects.values('title', 'writer__userid', 'created_at', 'id')[offset:offset + limit] 
        return JsonResponse({'count': posts.count(), 'data': list(posts)}, status=200)


class PostDetailView(View):
    
    def get(self, request, *args, **kwargs):
        post = Post.objects.get(id = kwargs['id'])
        post = {
            'author': post.writer.userid,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at,
            'updated_at': post.updated_at
        }
        return JsonResponse({'post':post}, status=200)


class PostUpdateView(View):

    @login_check
    def get(self, request, *args, **kwargs):
        if Post.objects.get(id = kwargs['id']).writer.userid != User.objects.get(id = request.user.id).userid:
                return JsonResponse({'message':'수정 권한 없음'}, status=400)

        post = list(Post.objects.filter(id = kwargs['id']).values('title', 'content'))
        return JsonResponse({'post': post}, status=200)
    
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            Post.objects.filter(id = kwargs['id']).update(
                title = data['title'],
                content = data['content'],
                updated_at = time.time(),
            )
            return JsonResponse({'message':'post 수정 성공'}, status=200)
        
        except:
            return JsonResponse({'message':'error'}, status=400)



class PostDeleteView(View):

    @login_check
    def post(self, request, *args, **kwargs):
        try:
            if Post.objects.get(id = kwargs['id']).writer.userid != User.objects.get(id = request.user.id).userid:
                return JsonResponse({'message':'삭제 권한 없음'}, status=400)
            
            Post.objects.get(id = kwargs['id']).delete()
            return JsonResponse({'message':'post 삭제 성공'}, status=200)
        
        except Post.DoesNotExist:
            return JsonResponse({'message':'해당 post 없음'}, status=400)


