# Sneeds booklet using django
>Django implementation of booklet download service.


This is implementation of new part of sneeeds.ir website using python and Django framework .

test
## Usage 

_This python project will be used in booklet part of  <a href="http://sneeds.ir/" target="_blank">**sneeds**</a> website._


## Release History

* 0.1.0
    * This is in initial release. 
    * CHANGE: Made from `scratch!`.


## Meta

Arya Khaligh - bartararya@gmail.com 

Distributed under the Arya license.


## 🍴Contributing

1. Fork it (<https://github.com/aryabartar/sneeds-django/fork>)
2. Create your feature branch (`git checkout -b sneeds-django/yourBar`)
3. Commit your changes (`git commit -am 'Add some yourBar'`)
4. Push to the branch (`git push origin sneeds-django/yourBar`)
5. Create a new Pull Request

## Documentation
```
LOGIN PAGE: http://193.176.243.12:8000/admin

-- blog -- 
http://hostname/blog/ => Retrieve all blog posts
http://hostname/blog/?limit=2 => Retrieve post with Pagination(limit determines number of posts)
http://hostname/blog/?limit=2&offset=4 => Retrieve post with Pagination(offset stands for current page,current page in this example is 5)

http://hostname/blog/topics-list/ => Retrieve all topics (Pagination is not implemented yet because topics number is limited)

http://hostname/blog/post/test-topic-1/ => Retrieve all posts with topic that it's slug is "test-topic-1"
http://hostname/blog/post/test-topic-1/?limit=2 => Retrieve with pagination (page limit is 2)
http://hostname/blog/post/test-topic-1/?limit=2&offset=4  => Retrieve with pagination(page limit is 2 and current page is 5)

http://hostname/blog/post/usa/is-amirkabir-good/ => Retrieve post which its topic's slug is "usa" and post slug is "is-amirkabir-good"
This endpoint also returns post comments and also admin reply to that comment.
http://hostname/blog/post/usa/is-amirkabir-good/ => Post request to add comment to this post.
sample Post request:
        {
            "user": 2,
            "content": "THIS POST IS GREAT!",
            "post": 3
        }


-- booklet --
http://127.0.0.1:8000/booklet/ => Retrieve all fields + topics associated with that fields (No Pagination)
http://127.0.0.1:8000/booklet/computer-engineering/ => Retrieve field with "computer-engineering" slug (This page includes that field topics and posts)
http://127.0.0.1:8000/booklet/computer-engineering/advanced-programming/ => Retrieve a topic which it's field's slug is 'computer-engineering' and it's slug is 'advanced-programming'

http://127.0.0.1:8000/booklet/computer-engineering/advanced-programming/deitel-java/ => Retrieve a booklet with 'deitel' slug. Also checks field and topic slug to be true!
http://127.0.0.1:8000/booklet/computer-engineering/advanced-programming/deitel-java/?like=true => Increments number of likes (I will implement session validation later)

http://127.0.0.1:8000/booklet/tags/ => Retrieve all tags list.
http://127.0.0.1:8000/booklet/tags/best-booklet/ => Retrieve a tag with slug="best-booklet"
http://127.0.0.1:8000/booklet/tags/best-booklet/posts/ => Retrieve all posts of a tag with slug="best-booklet" (pagination included!)

-- discount --
http://127.0.0.1:8000/cafe/cafes/ => Retrieve all cafes (No pagination included)
http://127.0.0.1:8000/cafe/cafes/ehsan-va-shoraka/ => Retrieves a cafe with "ehsan-va-shoraka" slug
http://127.0.0.1:8000/cafe/cafes/ehsan-va-shoraka/discounts => Retrieves all discounts of "ehsan-va-shoraka" cafe

http://127.0.0.1:8000/cafe/discounts/ => Retrieve and Post. Retrieve all discounts.
  Post format:
    {
        "discount_percent": 35,
        "discount_info": "Only on main course."
    }
    Note: Only cafe admin have post permission.

http://127.0.0.1:8000/cafe/discounts/119 => Retrieve and Delete.
  Retrieves discount with 119 id.
  Deletes discount with 119 id.

http://127.0.0.1:8000/cafe/user-discounts/ => Retrieve and Post.
  Retrieve is different for 3 type of users:
    1) Super Admin can retrieve all user-discounts.
    2) Cafe Admin can retrieve all user-discounts of a cafe.
    3) Simple User retrieve its own data.

  Post format:
    {
        "discount": 12
    }
    Note: This will create a user-discount instance for logged in user.

http://127.0.0.1:8000/cafe/user-discounts/125 => Retrieve and Delete.
  Retrieves user-discount with 125 id.
  Deletes user-discount with 125 id.

-- account --
This is a technical guideline:
Register:
  register endpoint: http://127.0.0.1:8000/account/jwt/register/
  Sample post request:
    {
        "username": "ali",
        "email": "ali@gmail.com",
        "first_name": "arya",
        "last_name": "bartar",
        "phone": "09011353909",
        "password": "sneeds@203040",
        "password2": "sneeds@203040"
    }
  Returns this json data:
    {
        "username": "ali",
        "email": "ali@gmail.com",
        "first_name": "arya",
        "last_name": "bartar",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozOSwidXNlcm5hbWUiOiJhbGkxMSIsImV4cCI6MTU1MDc3NzQxNywiZW1haWwiOiJhbGkxMUBnbWFpbC5jb20iLCJvcmlnX2lhdCI6MTU1MDc3NzExN30.hCjGTB_9D0DvewMhgc6t5C5Xr8flFizCBPTk4SF5PHA",
        "token_expires": "2019-03-08T19:21:57.551613Z",
        "message": "Success!"
    }

Login:
  login endpoint: http://127.0.0.1:8000/account/jwt/login/
  User can login with either username or email. (I prefer email)
    {
       "username_or_email" : "ali",
       "password" : "sneeds@203040"
    }
  or
    {
       "username_or_email" : "ali@gmail.com",
       "password" : "sneeds@203040"
    }

  will return:
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMiwidXNlcm5hbWUiOiJhbGkiLCJleHAiOjE1NTA4MTQ1NjMsImVtYWlsIjoiYWxpQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTUwODE0MjYzfQ.lexMBgJbescCWSj0LsETSY0KzjCNsYwTeaNgNnosa94",
        "username": "ali",
        "expires": "2019-03-09T05:41:03.892883Z"
    }

Refresh token:
  Refresh token endpoint: http://127.0.0.1:8000/account/jwt/refresh/

  Post old token to:
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMiwidXNlcm5hbWUiOiJhbGkiLCJleHAiOjE1NTA4MTUwMTQsImVtYWlsIjoiYWxpQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTUwODE0NzA1fQ.3Pnpau1yfIVSjbgfEgBT202Wjb0C4pYHX-0mtJiq4Vc"
    }

  will return:
    {
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMiwidXNlcm5hbWUiOiJhbGkiLCJleHAiOjE1NTA4MTUwNDgsImVtYWlsIjoiYWxpQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTUwODE0NzA1fQ.xDCkbhXbNii7mcpVRGVgk_QBP7Dg05nC7nPxKzimqU0",
        "username": "ali",
        "expires": "2019-03-09T05:49:08.756955Z"
    }
  which token is your new token.
```