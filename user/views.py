from django.http.response import JsonResponse
from django.views.generic import View

from config.settings import SECRET_KEY
from .models import User
import json
import jwt
import bcrypt


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(userid = data['userid']).exists():
                return JsonResponse({'message':'Failed'}, status=400)

            hashed_pwd = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                userid = data['userid'],
                password = hashed_pwd
            )
            return JsonResponse({'message':'Success'}, status=200)
        
        except KeyError:
            return JsonResponse({'message': 'Invalid Keys'}, status=400)


class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(userid=data['userid']).exists():
                user = User.objects.get(userid=data['userid'])

            if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'user_id':user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                return JsonResponse({'token':token}, status=200)
            return JsonResponse({'message':'error'}, status=401)
        
        except KeyError:
            return JsonResponse({'message': 'Invalid Keys'}, status=400)