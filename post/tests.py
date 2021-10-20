import bcrypt
import jwt
import json
import time
from django.test import TestCase, Client
from post.models import Post
from user.models import User
from config.settings import SECRET_KEY


class PostsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            userid = 'test9',
            password = bcrypt.hashpw('test9'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.created_at = time.time()
        Post.objects.create(
            title = '테스트 글입니돠',
            content = '테스트 하는 글입니다. 세부내용입니다.',
            writer = self.user,
            created_at = self.created_at
        )

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()

    def test_get_posts_success(self):
        client = Client()
        response = client.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),{
            "count": 1,
            "data": [
                {
                "title": "테스트 글입니돠",
                "writer__userid": "test9",
                "created_at": str(self.created_at),
                "id": 1
                }]})

    def test_get_posts_fail(self):
        pass


class PostsCreateTest(TestCase):
    '''
    post create test code
    '''
    def setUp(self):
        User.objects.create(
            userid = 'test9',
            password = bcrypt.hashpw('test9'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        User.objects.create(
            userid = 'test8',
            password = bcrypt.hashpw('test8'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        self.test8_token = jwt.encode({'user_id': 2}, SECRET_KEY, algorithm='HS256').decode('utf-8')

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()


    def test_post_create_success(self):
        client = Client()
        header = {"HTTP_Authorization" : self.token}
        post = {
            'title' : 'test용 제목입니다',
            'content' : 'test용 내용입니다',
        }
        response = client.post('/post/create/', json.dumps(post) , **header, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "Success"})   

    def test_post_create_fail(self):
        client = Client()
        post = {
            'title' : 'test용 제목입니다',
            'content' : 'test용 내용입니다',
        }
        response = client.post('/post/create/', json.dumps(post) ,content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message" : "Token Error"})   


class PostsUpdateTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            userid = 'test8',
            password = bcrypt.hashpw('test9'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.user2 = User.objects.create(
            userid = 'test9',
            password = bcrypt.hashpw('test8'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.test8_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        self.test9_token = jwt.encode({'user_id': 2}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        self.created_at = time.time()

        Post.objects.create(
            title = '테스트 글입니돠',
            content = '테스트 하는 글입니다. 세부내용입니다.',
            writer = self.user1,
            created_at = self.created_at
        )
    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()


    def test_get_update_success(self):
        client = Client()
        header = {"HTTP_Authorization" : self.test8_token}
        response = client.get('/post/1/update/',  **header, content_type='application/json')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(),{
            "post": [
                {
                "content": "테스트 하는 글입니다. 세부내용입니다.",
                "title": "테스트 글입니돠"
                }]})

    def test_get_update_user_fail(self):
        '''
        권한없는 유저가 수정하는 케이스
        '''
        client = Client()
        header = {"HTTP_Authorization" : self.test9_token}
        response = client.get('/post/1/update/',  **header, content_type='application/json')
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response.json(), {'message': '수정 권한 없음'})

    def test_get_update_post_fail(self):
        '''
        존재하지 않는 게시글 케이스
        '''
        client = Client()
        header = {"HTTP_Authorization" : self.test9_token}
        response = client.get('/post/3/update/',  **header, content_type='application/json')
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response.json(), {'message': 'no post'})

    def test_post_update_success(self):
        client = Client()

        post = {
            'title' : 'test용 제목입니다 -> 변경한 제목입니다',
            'content' : 'test용 내용입니다 -> 변경한 내용입니다',
        }
        response = client.post('/post/1/update/', json.dumps(post), content_type='application/json')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(),{'message': 'post 수정 성공'})


class PostsDeleteTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
            userid = 'test8',
            password = bcrypt.hashpw('test9'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.user2 = User.objects.create(
            userid = 'test9',
            password = bcrypt.hashpw('test8'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        )
        self.test8_token = jwt.encode({'user_id': 1}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        self.test9_token = jwt.encode({'user_id': 2}, SECRET_KEY, algorithm='HS256').decode('utf-8')
        self.created_at = time.time()

        Post.objects.create(
            title = '테스트 글입니돠',
            content = '테스트 하는 글입니다. 세부내용입니다.',
            writer = self.user1,
            created_at = self.created_at
        )

    def tearDown(self):
        User.objects.all().delete()
        Post.objects.all().delete()
        
    def test_post_delete_success(self):

        client = Client()
        header = {"HTTP_Authorization" : self.test8_token}
        response = client.post('/post/1/delete/',  **header, content_type='application/json')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.json(), {'message': 'post 삭제 성공'})        

    def test_post_delete_user_fail(self):
        '''
        권한없는 유저가 삭제하는 케이스
        '''
        client = Client()
        header = {"HTTP_Authorization" : self.test9_token}
        response = client.post('/post/1/delete/',  **header, content_type='application/json')
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response.json(), {'message': '삭제 권한 없음'})

    def test_post_delete_post_fail(self):
        '''
        존재하지 않는 게시글 케이스
        '''
        client = Client()
        header = {"HTTP_Authorization" : self.test9_token}
        response = client.post('/post/11/delete/',  **header, content_type='application/json')
        self.assertEqual(response.status_code, 400) 
        self.assertEqual(response.json(), {'message': '해당 post 없음'})