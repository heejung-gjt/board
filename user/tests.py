import json
import bcrypt
import jwt
from config.settings import SECRET_KEY
from django.test import TestCase, Client
from .models import User


class SignUpTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_post_success(self):
        client = Client()
        signup_data = {"userid": "test13", "password": "123456"}
        response = client.post('/user/signup/', json.dumps(signup_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_signup_fail(self):
        client = Client()
        signup_data = {"userid": "te", "password": "34"}
        response=client.post('/user/signup/',json.dumps(signup_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message" : "아이디 형식 에러"})        


class SignInTest(TestCase):

    def setUp(self):
        self.password = bcrypt.hashpw('test9'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        User.objects.create(id = 9, userid = 'test9', password = self.password)

    def tearDown(self):
        User.objects.all().delete()

    def test_signin_post_success(self):
        client = Client()
        signin_data = {"userid": "test9", "password": 'test9'}
        response = client.post('/user/signin/', json.dumps(signin_data), content_type='application/json')

        if bcrypt.checkpw(signin_data['password'].encode('utf-8'), self.password.encode('utf-8')):
            self.token = jwt.encode({'user_id':9}, SECRET_KEY, algorithm='HS256').decode('utf-8')
            
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'token':self.token})


    def test_signin_post_fail(self):
        client = Client()
        signin_data = {"userid": "test9", "password": 'test99'}
        response = client.post('/user/signin/', json.dumps(signin_data), content_type='application/json')

        if bcrypt.checkpw(signin_data['password'].encode('utf-8'), self.password.encode('utf-8')):
            self.token = jwt.encode({'user_id':9}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {"message" : "error"}) 