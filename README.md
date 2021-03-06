# ๐ ๊ฒ์ํ CRUD API ๊ตฌํ 
## ๋ชฉ์ฐจ
- ###  [How to Implement](https://github.com/heejung-gjt/board/tree/develop#how-to-implement-1)  
- ### [Build Environment](https://github.com/heejung-gjt/board/tree/develop#build-environment-1)    
- ### [Endpoint Call](https://github.com/heejung-gjt/board/tree/develop#endpoint-call-1)   
- ### [API Documentation](https://github.com/heejung-gjt/board/tree/develop#api-documentation-1)   
- ### [Unit Test](https://github.com/heejung-gjt/board/tree/develop#api-documentation-1)    

<br>


## How to Implement

- Client-Server๊ฐ ๋ฐ์ดํฐ ์ฐ๋์ json ํฌ๋งท์ผ๋ก ์งํํ์ต๋๋ค.      
  
- DRF๋์ ์ JsonResponse๋ฅผ ์ฌ์ฉํ์ฌ ๊ฒ์ํ CRUD API ๊ฐ๋ฐ์ ์งํํ์ต๋๋ค. ์ฅ๊ณ ์ ๊ธฐ๋ณธ๊ธฐ๋ฅ์ธ ํด๋์คํ๋ทฐ์ JsonResponse๋ฅผ ์ฌ์ฉํ๋ ๋ฐฉ์์ผ๋ก๋ ์ถฉ๋ถํ ๊ตฌํ์ด ๊ฐ๋ฅํ๋ค๊ณ  ์๊ฐํ๊ณ  ์ด๋ฌํ ๋ฐฉ์์ผ๋ก JWTํ ํฐ ์ธ์ฆ๋ฐฉ์ ๊ณผ์ ์ ๊ตฌํํด๋ณด๊ณ  ์ถ์์ต๋๋ค.     

- signin ์๋ํฌ์ธํธ์์ JWT์ธ์ฆ ํ ํฐ์ ๋ฐ๊ธ ๋ฐ์์ต๋๋ค.       

- ํ์๊ฐ์์ id์ password์ ๋ํ ์ ํจ์ฑ ๊ฒ์ฆ์ ์ํด validator๋ผ๋ ํ์ผ์ ๋ง๋ค์์ต๋๋ค. view๋จ์์ import๋ฐ์ ์ฌ์ฉํ๋ ๋ฐฉ์์ด ๋ ํจ์จ์ ์ด๋ผ๊ณ  ์๊ฐํ์ต๋๋ค.   

- app์์ ์๋ testํ์ผ์ unit test๋ฅผ ๊ตฌํํ์ต๋๋ค. ๊ฐ๋๋ง ์๊ณ ์์๋ ๊ธฐ๋ฅ์ผ๋ก์จ ์ด๋ฒ ๊ธฐํ์ ์ง์  ์ค์ตํด๋ณด๊ณ  ์ถ์์ต๋๋ค.  

(ํ์คํธ ๊ณผ์ ์ unit test์ ํจ๊ป postman์ ์ฌ์ฉํ์ต๋๋ค) 


<br>

## Build Environment
```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install django
$ pip install -r requirements.txt
```
<details>
    <summary>SECRET KEY(์ญ์ ์์ )</summary>
<ul><li>django-insecure-*v2nfp5dla=1wo@w5h9et6(^s-tel#q(h1(3)74m2d0*_2@)yh</li></ul>

</details>

<br>

## Endpoint Call
(postman์ ์ฌ์ฉํด ํ์คํธ ํ์ต๋๋ค)
> __ํ์๊ฐ์__   

- id์ password๋ฅผ body์ ๋ด์ ์๋ฒ์ POST์์ฒญ์ ํ๋ค      
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ id์ password์ ๋ํ ์ ํจ์ฑ ๊ฒ์ฆ์ ํ๋ค  
- ์ ํจ์ฑ ๊ฒ์ฆ์ด ๋๋ ํ ์ ์ ๋ฅผ ์์ฑํ๊ณ  ์ ์์ ์ผ๋ก ์ ์ ๊ฐ ์์ฑ ๋์๋ค๋ ๋ฉ์์ง๋ฅผ responseํ๋ค       

|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |
|----|----|----|
|POST|127.0.0.1:8000/user/signup|์๋ก์ด ์ ์  ์์ฑ    

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. body์ id์ pwd๋ฅผ ๋ด๋๋ค
{
    "userid": "test2",
    "password": "test2"
}

# 2. post์์ฒญ์ผ๋ก ์๋ฒ์ ๋ฐ์ดํฐ๋ฅผ ๋ณด๋ธ๋ค
127.0.0.1:8000/user/signup/

# 3. ์๋ฒ์์ ๋ฐ์ดํฐ์ ๋ํ ์ ํจ์ฑ ๊ฒ์ฆ๊ณผ ์๋ฌ์ฒ๋ฆฌ๋ฅผ ํ ํ ์ ์ ๊ฐ ์์ฑ๋์๋ค๋ ๋ฉ์์ง๋ฅผ Responseํ๋ค
return JsonResponse({'message':'Success'}, status=200)

# ์๋ต๋ ๋ฐ์ดํฐ
{
    "message": "Success"
}

```

<br>

> __๋ก๊ทธ์ธ__   

-  ๋ก๊ทธ์ธ ํ  id์ password๋ฅผ body์ ๋ด์ ์๋ฒ์ POST์์ฒญ์ ํ๋ค      
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ id์ password์ ๋ํ ์ ํจ์ฑ ๊ฒ์ฆ์ ํ๋ค  
  - id๊ฐ DB์ ์กด์ฌํ๋์ง์ ๋ํ ๊ฒ์ฆ
  - pwd๊ฐ id์ ํด์๋ password์ ๊ฐ์์ง์ ๋ํ ๊ฒ์ฆ    
- ์ ํจ์ฑ ๊ฒ์ฆ์ด ๋๋ ํ ํด๋น ์ ์ ์ ๋ํ ์ธ์ฆ์ ์ํด jwt token์ ๋ฐ๊ธํ์ฌ jsonํํ๋ก responseํ๋ค    

|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |
|----|----|----|
|POST|127.0.0.1:8000/user/signin|์ ์ ๋ก ๋ก๊ทธ์ธ    

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. body์ id์ pwd๋ฅผ ๋ด๋๋ค
{
    "userid": "test1",
    "password": "test1"
}

# 2. post์์ฒญ์ผ๋ก ์๋ฒ์ ๋ฐ์ดํฐ๋ฅผ ๋ณด๋ธ๋ค
127.0.0.1:8000/user/signin/

# 3. ์๋ฒ์์ ๋ฐ์ดํฐ์ ๋ํ ์ ํจ์ฑ ๊ฒ์ฆ๊ณผ ์๋ฌ์ฒ๋ฆฌ๋ฅผ ํ ํ ์ ์ ์ ๋ํ token์ ๋ฐ๊ธํ์ฌ ํจ๊ป responseํ๋ค
return JsonResponse({'token':token}, status=200)

# ์๋ต๋ ๋ฐ์ดํฐ
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}
```

<br>


> __๊ฒ์๊ธ ์์ฑ__   

- ๊ธ ์์ฑ์ ์ํ POST์์ฒญ์ ๋ณด๋ด๊ธฐ ์ ์ ๋ก๊ทธ์ธ ํ  ๋ ๋ฐ๊ธ ๋ฐ์๋ ํ ํฐ์ header์ ๋ด๋๋ค
- ์์ฑํ ๋ด์ฉ์ body์ ๋ด์ header์ ๋ด๊ฒจ์ ธ ์๋ ํ ํฐ๊ณผ ํจ๊ป ์๋ฒ์ POST์์ฒญ์ ํ๋ค   
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ ํ ํฐ์ด ์๋์ง ์ ์์ ์ธ ํ ํฐ์ธ์ง์ ๋ํด ๊ฒ์ฆ์ ํ์ฌ ์ ์ ๋ฅผ ์ธ๊ฐํ๋ค     
- ๊ฒ์ฆ์ด ๋๋ ํ body์ ๋ด๊ฒจ์ ธ ์๋ ์ ์ ๊ฐ ์์ฑํ ๊ธ์ ๊ฒ์๊ธ๋ก ์์ฑํ๋ค
- ์ ์์ ์ผ๋ก ๊ฒ์๊ธ์ด ์์ฑ๋์๋ค๋ ๋ฉ์์ง๋ฅผ responseํ๋ค   
  

|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |
|----|----|----|
|POST|127.0.0.1:8000/post/create|ํน์  ์ ์ ์ ๊ฒ์๊ธ ์์ฑ

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. ์ ์ ์ ํ ํฐ์ header์ ๋ด๋๋ค
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}

# 2. ์์ฑํ  ๊ธ์ body์ ๋ด๋๋ค
{
    "title": "test ํ์ดํ ์๋๋ค",
    "content": "test content ์๋๋ค"
}

# 3. post์์ฒญ์ผ๋ก ์๋ฒ์ ๋ฐ์ดํฐ๋ฅผ ๋ณด๋ธ๋ค
127.0.0.1:8000/post/create/

# 4. ํ ํฐ๊ณผ ๋ฐ์ดํฐ๋ฅผ ๋ฐ์ ์๋ฒ๋ ํ ํฐ์ ๋ํ ์ ๋ณด๋ฅผ ํ์ธ ํ ๊ฒ์๊ธ์ ์์ฑํ๋ค. ์ดํ ๊ธ์ด ์์ฑ๋์๋ค๋ ๋ฉ์์ง๋ฅผ responseํ๋ค
return JsonResponse({'message':'Success'}, status=200)

# ์๋ต๋ ๋ฐ์ดํฐ
{
    "message": "Success"
}

```

<br>

> __๊ฒ์๊ธ ๋ฆฌ์คํธ__     

- ์์ฑ๋ ๊ฒ์๊ธ์ ๊ฐ์์ ๋ฒ์๋ฅผ ์ฟผ๋ฆฌ์คํธ๋ง์ผ๋ก url์ ํจ๊ป ๋ด์ ์๋ฒ์ GET์์ฒญ์ ํ๋ค
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ ํ๋ฉด์ ๋ ๋๋ง ๋  ๊ฒ์๊ธ์ ๊ฐ์์ ๋ฒ์๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ฐ์ดํฐ๋ฅผ splitํ๋ค
  - ๊ฒ์๊ธ์ ๋ํ ํ์ํ ๋ฐ์ดํฐ๋ง responseํ๋ค
  - ๋ฒ์์ ๊ฐ์๊ฐ ์ ํด์ง ๊ฒ์๊ธ์ ์ด ๊ฐ์๋ฅผ responseํ๋ค
  

|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |
|----|----|----|
|GET|127.0.0.1:8000/post?limit=2&offset=1| paging๋ ๊ฒ์๊ธ ์์ฒญ  

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. ์ฟผ๋ฆฌ์คํธ๋ง์ผ๋ก ๋ณด์ฌ์ง ๊ฒ์๊ธ์ ๊ฐ์์ ๋ฒ์๋ฅผ ๋ด์ GET์์ฒญ์ ํ๋ค
127.0.0.1:8000/post?limit=2&offset=1

# 2. ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ ์ด์ ๋ง๊ฒ ๊ฒ์๊ธ์ ํ์ด์ง ์ฒ๋ฆฌํ์ฌ ํ์ํ ๋ฐ์ดํฐ๋ฅผ responseํ๋ค  
limit = int(request.GET.get('limit', 10))
offset = int(request.GET.get('offset', 0))
posts = Post.objects.values('title', 'writer__userid', 'created_at', 'id')[offset:offset + limit] 
return JsonResponse({'count': posts.count(), 'data': list(posts)}, status=200)

# ์๋ต๋ ๋ฐ์ดํฐ
{
    "count": 2,
    "data": [
        {
            "title": "1๋ฒ์ ๊ฒ์๊ธ์ ์์ ํ์ต๋๋ค",
            "writer__userid": "test2",
            "created_at": "1634728232.7316754",
            "id": 3
        },
        {
            "title": "1๋ฒ์ ๊ฒ์๊ธ์ ์์ ํ์ต๋๋ค",
            "writer__userid": "test1",
            "created_at": "1634728232.7316754",
            "id": 4
        }
    ]
}
```

<br>

> __์ธ๋ถ ๊ฒ์๊ธ__   

- ํน์  ๊ฒ์๊ธ์ id์ ํจ๊ป GET์์ฒญ์ ํ๋ค   
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ id์ ๋ํ post์ ๋ฐ์ดํฐ๋ฅผ responseํ๋ค     
  - ์กด์ฌํ์ง ์๋ ๊ธ ์ผ ๊ฒฝ์ฐ error๋ฉ์์ง๋ฅผ responseํ๋ค     

|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |
|----|----|----|
|GET|127.0.0.1:8000/post/2|ํน์  ๊ฒ์๊ธ์ ๋ํ  GET์์ฒญ   

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. id์ ํจ๊ป GET์์ฒญ์ ํ๋ค
127.0.0.1:8000/post/2/  # 2๋ฒ ๊ฒ์๊ธ์ ๋ํ GET์์ฒญ  

# 2. ์๋ฒ๋ id์ ํด๋นํ๋ ๊ฒ์๊ธ์ filterํ์ฌ responseํ๋ค
post = Post.objects.get(id = kwargs['id'])
post = {
    'author': post.writer.userid,
    'title': post.title,
    'content': post.content,
    'created_at': post.created_at,
    'updated_at': post.updated_at
}
return JsonResponse({'post':post}, status=200)

# ์๋ต๋ ๋ฐ์ดํฐ
{
    "post": {
        "author": "test2",
        "title": "test2์ ํ์ดํ ์๋๋ค",
        "content": "test2์ content ์๋๋ค. ์๋ํ์ธ์",
        "created_at": "1634728232.7316754",
        "updated_at": ""
    }
}

```

<br>


> __๊ฒ์๊ธ ์์ __   
(์ฅ๊ณ ์๋ PUT์ด ์ ๊ณต๋์ง ์์ GET๊ณผ POST๋ฅผ ์ด์ฉํด ๊ตฌํ)   

- ์ ์ ์ ์ธ์ฆ์ ์ํด ํ ํฐ์ header์ ๋ด์ ์์ ํ  ๊ฒ์๊ธ์ GET์์ฒญํ๋ค
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ ํ ํฐ์ด ์๋์ง ์ ์์ ์ธ ํ ํฐ์ธ์ง์ ๋ํด ๊ฒ์ฆ์ ํ์ฌ ์ ์ ๋ฅผ ์ธ๊ฐํ๋ค  
- ํด๋น ๊ฒ์๊ธ์ ์ ๊ทผ ๊ถํ์ด ์๋ ์ ์ ์ธ์ง ๊ฒ์ฆํ๋ค      
- ๊ฒ์ฆ์ด ๋๋ ํ ํด๋น ๊ฒ์๊ธ์ ์์ ํ๊ธฐ ์ํด responseํ๋ค     
 
|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |  
|----|----|----|
|GET|127.0.0.1:8000/post/4/update|ํน์  ๊ฒ์๊ธ์ ๋ํ ๋ฐ์ดํฐ GET์์ฒญ|
|POST|127.0.0.1:8000/post/4/update| ๋ฐ์ดํฐ ์์ ์ ๋ํ POST์์ฒญ|

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. ์ ์ ์ ํ ํฐ์ header์ ๋ด๋๋ค
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}

# 2. ์ ์ ์ ํ ํฐ๊ณผ ํจ๊ป ์์ ํ  ํน์  ๊ฒ์๊ธ์ GET์์ฒญํ๋ค
127.0.0.1:8000/post/4/update/

# 3. ํ ํฐ์ ๋ํ ๊ฒ์ฆ์ ํ ํ ํด๋น ๊ฒ์๊ธ์ ์ ๊ทผ ๊ถํ์ด ์๋ ์ ์ ์ธ์ง ๊ฒ์ฆํ๋ค   
if Post.objects.get(id = kwargs['id']).writer.userid != User.objects.get(id = request.user.id).userid:
   return JsonResponse({'message':'์์  ๊ถํ ์์'}, status=400)    
   
# ํด๋น ๊ธ์ ์์ฑํ ์ธ์ฆ๋ ์ ์ ์์ ๊ฒ์ฆํ ์๋ฒ๋ ์์ ํ  ๊ธ์ responseํ๋ค
post = list(Post.objects.filter(id = kwargs['id']).values('title', 'content'))

# ์๋ต๋ ๋ฐ์ดํฐ 
{
    "post": [
        {
            "title": "test1์ด ์ด๋ฒ์๋ ์์ฑํ์ด๋ ",
            "content": "test1์๋๋น ํํํฃํํํ"
        }
    ]
}

# 4. ์์ ํ  ๊ธ์ ์์ฑํ์ฌ body์ ๋ด์ POST ์์ฒญํ๋ค  
127.0.0.1:8000/post/4/update/

{
    "title": "1๋ฒ์ ๊ฒ์๊ธ์ ์์ ํ์ต๋๋ค",
    "content": "๋ฐฉ๊ธ ์ ๊ฐ ์์ ํ๋๋ฐ์ ?"
}

# 5. ์๋ฒ๋ body์ ๋ด๊ธด ๋ฐ์ดํฐ๋ฅผ ๊ฐ์ง๊ณ  ํน์  ๊ฒ์๊ธ์ ์์ ํ๋ค. ์์ ์ด ๋๋ํ ์๋ฃ๋์๋ค๋ ๋ฉ์์ง๋ฅผ responseํ๋ค
{
    "message": "post ์์  ์ฑ๊ณต"
}

```

<br>

> __๊ฒ์๊ธ ์ญ์ __   

- ์ ์ ์ ์ธ์ฆ์ ์ํด ํ ํฐ์ header์ ๋ด์ ์ญ์ ํ  ๊ฒ์๊ธ์ id์ ํจ๊ป POST์์ฒญ์ ํ๋ค
- ์์ฒญ์ ๋ฐ์ ์๋ฒ๋ ํ ํฐ์ด ์๋์ง ์ ์์ ์ธ ํ ํฐ์ธ์ง์ ๋ํด ๊ฒ์ฆ์ ํ์ฌ ์ ์ ๋ฅผ ์ธ๊ฐํ๋ค   
- ์ธ์ฆ๋ ์ ์ ๊ฐ ํน์  ๊ฒ์๊ธ์ ์ ๊ทผ ๊ถํ์ด ์๋์ง ๊ฒ์ฆํ๋ค
- ๊ฒ์ฆ์ด ๋๋ํ ํด๋น ๊ฒ์๊ธ์ deleteํ ํ ์ญ์ ๊ฐ ์๋ฃ๋์๋ค๋ ๋ฉ์์ง๋ฅผ responseํ๋ค   
 
|HTTP๋ฉ์๋|URL(์์)|Endpoint ์ญํ |  
|----|----|----|
|POST|127.0.0.1:8000/post/1/delete/|ํน์  ๊ฒ์๊ธ์ ์ญ์ ์ ๋ํ POST์์ฒญ|   

__ํธ์ถ ๋ฐฉ๋ฒ__       
```python
# 1. ์ ์ ์ ํ ํฐ์ header์ ๋ด๋๋ค
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxfQ.bqw5oIGa5LN3CcOWO2KRtZXTzSZZ2npF7rGya_uoTn4"
}

# 2. ์ ์ ์ ํ ํฐ๊ณผ ํจ๊ป ์ญ์ ํ  ํน์  ๊ฒ์๊ธid์ POST์์ฒญ์ ํ๋ค
127.0.0.1:8000/post/1/delete/

# 3. ํ ํฐ์ ๋ํ ๊ฒ์ฆ์ ํ ํ ํด๋น ๊ฒ์๊ธ์ ์ ๊ทผ ๊ถํ์ด ์๋ ์ ์ ์ธ์ง ๊ฒ์ฆํ๋ค   
if Post.objects.get(id = kwargs['id']).writer.userid != User.objects.get(id = request.user.id).userid:
   return JsonResponse({'message':'์ญ์  ๊ถํ ์์'}, status=400)  

# 4. ๊ฒ์ฆ์ด ๋๋ํ ํด๋น ๊ฒ์๊ธ์ ์ญ์ ํ ํ ์๋ฃ ๋ฉ์์ง๋ฅผ responseํ๋ค

# ์๋ต๋ ๋ฐ์ดํฐ 
{
    "message": "post ์ญ์  ์ฑ๊ณต"
}

```

<br>

### __httpie๋ก HTTP ํธ์ถํ๋ ๋ฐฉ๋ฒ__   

1. ์๋ฒ์ ์์ฒญ์ ๋ณด๋ผ ๋ก์ปฌ์ชฝ์์(ํฐ๋ฏธ๋๋ฑ) pip install httpie ๋ฅผ ์ค์นํ๋ค.   
2. python manage.py runserver๋ก ์๋ฒ๋ฅผ ์ผ๋๋๋ค.   

```
ํ์๊ฐ์ : http -v POST 127.0.0.1:8000/user/signup/ userid='test10' password='test10'

๋ก๊ทธ์ธ : http -v POST 127.0.0.1:8000/user/signin/

๊ฒ์๊ธ ์์ฑ : http -v POST 127.0.0.1:8000/post/create/ title="hi" content="oh hi!"  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"

๊ฒ์๊ธ ๋ฆฌ์คํธ : http -v GET 127.0.0.1:8000/post/ limit==1 offset==2

์ธ๋ถ ๊ฒ์๊ธ :http -v GET 127.0.0.1:8000/post/2/

๊ฒ์๊ธ ์์ (GET) : http -v GET 127.0.0.1:8000/post/3/update/  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"

๊ฒ์๊ธ ์์ (POST) : http -v POST 127.0.0.1:8000/post/3/update/ title="hi" content="oh hi!"  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"

๊ฒ์๊ธ ์ญ์  : http -v POST 127.0.0.1:8000/post/3/delete/  "Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozfQ.vXT-8KCRPdlfFqsH6JaHK9TVaadCh9Ev0ZT2DrZ-DAE"
```

<br>

## API Documentation
### [API ๋ช์ธ ๋ณด๋ฌ๊ฐ๊ธฐ](https://documenter.getpostman.com/view/16088238/UVC6h6M5)   

<br>

postman ์๋จ์ LANGUAGE -> HTTP๋ก ๋ณ๊ฒฝํ์   
![postman](https://user-images.githubusercontent.com/64240637/139027954-1ee45ea6-d148-44b9-8bce-af0ea5955c64.png)


<br>

## Unit Test
[WIKI ์์ฑ](https://github.com/heejung-gjt/board/wiki/User-App---Unit-Test)
