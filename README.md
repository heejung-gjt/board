# 📋 게시판 CRUD API 구현 
## 목차
- ###  [How to Implement](https://github.com/heejung-gjt/board/tree/develop#how-to-implement-1)  
- ### [Build Environment](https://github.com/heejung-gjt/board/tree/develop#build-environment-1)    
- ### [Endpoint Call](https://github.com/heejung-gjt/board/tree/develop#endpoint-call-1)   
- ### [API Documentation](https://github.com/heejung-gjt/board/tree/develop#api-documentation-1)   
- ### [Unit Test](https://github.com/heejung-gjt/board/tree/develop#api-documentation-1)    

<br>


## How to Implement

- Client-Server간 데이터 연동은 json 포맷으로 진행했습니다.      
  
- DRF대신에 JsonResponse를 사용하여 게시판 CRUD API 개발을 진행했습니다. 장고의 기본기능인 클래스형뷰와 JsonResponse를 사용하는 방식으로도 충분히 구현이 가능하다고 생각했고 이러한 방식으로 JWT토큰 인증방식 과정을 구현해보고 싶었습니다.     

- signin 엔드포인트에서 JWT인증 토큰을 발급 받았습니다.       

- 회원가입시 id와 password에 대한 유효성 검증을 위해 validator라는 파일을 만들었습니다. view단에서 import받아 사용하는 방식이 더 효율적이라고 생각했습니다.   

- app안에 있는 test파일에 unit test를 구현했습니다. 개념만 알고있었던 기능으로써 이번 기회에 직접 실습해보고 싶었습니다.  

(테스트 과정은 unit test와 함께 postman을 사용했습니다) 


<br>

## Build Environment
```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install django
$ pip install -r requirements.txt
```
<details>
    <summary>SECRET KEY(삭제예정)</summary>
<ul><li>django-insecure-*v2nfp5dla=1wo@w5h9et6(^s-tel#q(h1(3)74m2d0*_2@)yh</li></ul>

</details>

<br>

## Endpoint Call
(postman을 사용해 테스트 했습니다)
> __회원가입__   

- id와 password를 body에 담아 서버에 POST요청을 한다      
- 요청을 받은 서버는 id와 password에 대한 유효성 검증을 한다  
- 유효성 검증이 끝난 후 유저를 생성하고 정상적으로 유저가 생성 되었다는 메시지를 response한다       

|HTTP메소드|URL(자원)|Endpoint 역할|
|----|----|----|
|POST|127.0.0.1:8000/user/signup|새로운 유저 생성    

__호출 방법__       
```python
# 1. body에 id와 pwd를 담는다
{
    "userid": "test2",
    "password": "test2"
}

# 2. post요청으로 서버에 데이터를 보낸다
127.0.0.1:8000/user/signup/

# 3. 서버에서 데이터에 대한 유효성 검증과 에러처리를 한 후 유저가 생성되었다는 메시지를 Response한다
return JsonResponse({'message':'Success'}, status=200)

# 응답된 데이터
{
    "message": "Success"
}

```

<br>

> __로그인__   

-  로그인 할 id와 password를 body에 담아 서버에 POST요청을 한다      
- 요청을 받은 서버는 id와 password에 대한 유효성 검증을 한다  
  - id가 DB에 존재하는지에 대한 검증
  - pwd가 id의 해시된 password와 같은지에 대한 검증    
- 유효성 검증이 끝난 후 해당 유저에 대한 인증을 위해 jwt token을 발급하여 json형태로 response한다    

|HTTP메소드|URL(자원)|Endpoint 역할|
|----|----|----|
|POST|127.0.0.1:8000/user/signin|유저로 로그인    

__호출 방법__       
```python
# 1. body에 id와 pwd를 담는다
{
    "userid": "test1",
    "password": "test1"
}

# 2. post요청으로 서버에 데이터를 보낸다
127.0.0.1:8000/user/signin/

# 3. 서버에서 데이터에 대한 유효성 검증과 에러처리를 한 후 유저에 대한 token을 발급하여 함께 response한다
return JsonResponse({'token':token}, status=200)

# 응답된 데이터
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}
```

<br>


> __게시글 생성__   

- 글 생성을 위한 POST요청을 보내기 전에 로그인 할 때 발급 받았던 토큰을 header에 담는다
- 작성한 내용을 body에 담아 header에 담겨져 있는 토큰과 함께 서버에 POST요청을 한다   
- 요청을 받은 서버는 토큰이 있는지 정상적인 토큰인지에 대해 검증을 하여 유저를 인가한다     
- 검증이 끝난 후 body에 담겨져 있는 유저가 작성한 글을 게시글로 생성한다
- 정상적으로 게시글이 생성되었다는 메시지를 response한다   
  

|HTTP메소드|URL(자원)|Endpoint 역할|
|----|----|----|
|POST|127.0.0.1:8000/post/create|특정 유저의 게시글 생성

__호출 방법__       
```python
# 1. 유저의 토큰을 header에 담는다
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}

# 2. 작성할 글을 body에 담는다
{
    "title": "test 타이틀 입니다",
    "content": "test content 입니다"
}

# 3. post요청으로 서버에 데이터를 보낸다
127.0.0.1:8000/post/create/

# 4. 토큰과 데이터를 받은 서버는 토큰에 대한 정보를 확인 후 게시글을 생성한다. 이후 글이 생성되었다는 메시지를 response한다
return JsonResponse({'message':'Success'}, status=200)

# 응답된 데이터
{
    "message": "Success"
}

```

<br>

> __게시글 리스트__     

- 작성된 게시글의 개수와 범위를 쿼리스트링으로 url에 함께 담아 서버에 GET요청을 한다
- 요청을 받은 서버는 화면에 렌더링 될 게시글의 개수와 범위를 기준으로 데이터를 split한다
  - 게시글에 대한 필요한 데이터만 response한다
  - 범위와 개수가 정해진 게시글의 총 개수를 response한다
  

|HTTP메소드|URL(자원)|Endpoint 역할|
|----|----|----|
|GET|127.0.0.1:8000/post?limit=2&offset=1| paging된 게시글 요청  

__호출 방법__       
```python
# 1. 쿼리스트링으로 보여질 게시글의 개수와 범위를 담아 GET요청을 한다
127.0.0.1:8000/post?limit=2&offset=1

# 2. 요청을 받은 서버는 이에 맞게 게시글을 페이징 처리하여 필요한 데이터를 response한다  
limit = int(request.GET.get('limit', 10))
offset = int(request.GET.get('offset', 0))
posts = Post.objects.values('title', 'writer__userid', 'created_at', 'id')[offset:offset + limit] 
return JsonResponse({'count': posts.count(), 'data': list(posts)}, status=200)

# 응답된 데이터
{
    "count": 2,
    "data": [
        {
            "title": "1번의 게시글을 수정했습니다",
            "writer__userid": "test2",
            "created_at": "1634728232.7316754",
            "id": 3
        },
        {
            "title": "1번의 게시글을 수정했습니다",
            "writer__userid": "test1",
            "created_at": "1634728232.7316754",
            "id": 4
        }
    ]
}
```

<br>

> __세부 게시글__   

- 특정 게시글의 id와 함께 GET요청을 한다   
- 요청을 받은 서버는 id에 대한 post의 데이터를 response한다     
  - 존재하지 않는 글 일 경우 error메시지를 response한다     

|HTTP메소드|URL(자원)|Endpoint 역할|
|----|----|----|
|GET|127.0.0.1:8000/post/2|특정 게시글에 대한  GET요청   

__호출 방법__       
```python
# 1. id와 함께 GET요청을 한다
127.0.0.1:8000/post/2/  # 2번 게시글에 대한 GET요청  

# 2. 서버는 id에 해당하는 게시글을 filter하여 response한다
post = Post.objects.get(id = kwargs['id'])
post = {
    'author': post.writer.userid,
    'title': post.title,
    'content': post.content,
    'created_at': post.created_at,
    'updated_at': post.updated_at
}
return JsonResponse({'post':post}, status=200)

# 응답된 데이터
{
    "post": {
        "author": "test2",
        "title": "test2의 타이틀 입니다",
        "content": "test2의 content 입니다. 안녕하세요",
        "created_at": "1634728232.7316754",
        "updated_at": ""
    }
}

```

<br>


> __게시글 수정__   
(장고에는 PUT이 제공되지 않아 GET과 POST를 이용해 구현)   

- 유저의 인증을 위해 토큰을 header에 담아 수정할 게시글을 GET요청한다
- 요청을 받은 서버는 토큰이 있는지 정상적인 토큰인지에 대해 검증을 하여 유저를 인가한다  
- 해당 게시글에 접근 권한이 있는 유저인지 검증한다      
- 검증이 끝난 후 해당 게시글을 수정하기 위해 response한다     
 
|HTTP메소드|URL(자원)|Endpoint 역할|  
|----|----|----|
|GET|127.0.0.1:8000/post/4/update|특정 게시글에 대한 데이터 GET요청|
|POST|127.0.0.1:8000/post/4/update| 데이터 수정에 대한 POST요청|

__호출 방법__       
```python
# 1. 유저의 토큰을 header에 담는다
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}

# 2. 유저의 토큰과 함께 수정할 특정 게시글을 GET요청한다
127.0.0.1:8000/post/4/update/

# 3. 토큰에 대한 검증을 한 후 해당 게시글에 접근 권한이 있는 유저인지 검증한다   
if Post.objects.get(id = kwargs['id']).writer.userid != User.objects.get(id = request.user.id).userid:
   return JsonResponse({'message':'수정 권한 없음'}, status=400)    
   
# 해당 글을 작성한 인증된 유저임을 검증한 서버는 수정할 글을 response한다
post = list(Post.objects.filter(id = kwargs['id']).values('title', 'content'))

# 응답된 데이터 
{
    "post": [
        {
            "title": "test1이 이번에는 작성했슴돠",
            "content": "test1입니당 허허헣허허허"
        }
    ]
}

# 4. 수정할 글을 작성하여 body에 담아 POST 요청한다  
127.0.0.1:8000/post/4/update/

{
    "title": "1번의 게시글을 수정했습니다",
    "content": "방금 제가 수정했는데요 ?"
}

# 5. 서버는 body에 담긴 데이터를 가지고 특정 게시글을 수정한다. 수정이 끝난후 완료되었다는 메시지를 response한다
{
    "message": "post 수정 성공"
}

```

<br>

> __게시글 삭제__   

- 유저의 인증을 위해 토큰을 header에 담아 삭제할 게시글의 id와 함께 POST요청을 한다
- 요청을 받은 서버는 토큰이 있는지 정상적인 토큰인지에 대해 검증을 하여 유저를 인가한다   
- 인증된 유저가 특정 게시글에 접근 권한이 있는지 검증한다
- 검증이 끝난후 해당 게시글을 delete한 후 삭제가 완료되었다는 메시지를 response한다   
 
|HTTP메소드|URL(자원)|Endpoint 역할|  
|----|----|----|
|POST|127.0.0.1:8000/post/1/delete/|특정 게시글의 삭제에 대한 POST요청|   

__호출 방법__       
```python
# 1. 유저의 토큰을 header에 담는다
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}

# 2. 유저의 토큰과 함께 삭제할 특정 게시글id와 POST요청을 한다
127.0.0.1:8000/post/1/delete/

# 3. 토큰에 대한 검증을 한 후 해당 게시글에 접근 권한이 있는 유저인지 검증한다   
if Post.objects.get(id = kwargs['id']).writer.userid != User.objects.get(id = request.user.id).userid:
   return JsonResponse({'message':'삭제 권한 없음'}, status=400)  

# 4. 검증이 끝난후 해당 게시글을 삭제한 후 완료 메시지를 response한다

# 응답된 데이터 
{
    "message": "post 삭제 성공"
}

```

<br>

### __httpie로 HTTP 호출하는 방법__   

1. 서버에 요청을 보낼 로컬쪽에서(터미널등) pip install httpie 를 설치한다.   
2. python manage.py runserver로 서버를 켜놓는다.   

```
회원가입 : http -v POST 127.0.0.1:8000/user/signup/ userid='test10' password='test10'

로그인 : http -v POST 127.0.0.1:8000/user/signin/

게시글 생성 : http -v POST 127.0.0.1:8000/post/create/ title="hi" content="oh hi!"  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"

게시글 리스트 : http -v GET 127.0.0.1:8000/post/ limit==1 offset==2

세부 게시글 :http -v GET 127.0.0.1:8000/post/2/

게시글 수정(GET) : http -v GET 127.0.0.1:8000/post/3/update/  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"

게시글 수정(POST) : http -v POST 127.0.0.1:8000/post/3/update/ title="hi" content="oh hi!"  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"

게시글 삭제 : http -v POST 127.0.0.1:8000/post/3/delete/  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"
```

<br>

## API Documentation
### [API 명세 보러가기](https://documenter.getpostman.com/view/16088238/UV5ZAGHH)   

<br>

postman 상단에 LANGUAGE -> HTTP로 변경필요   
![postman](https://user-images.githubusercontent.com/64240637/139027954-1ee45ea6-d148-44b9-8bce-af0ea5955c64.png)


<br>

## Unit Test
[WIKI 작성](https://github.com/heejung-gjt/board/wiki/User-App---Unit-Test)
