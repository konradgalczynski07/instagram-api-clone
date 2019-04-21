# instagram-rest-api

REST API with all basic features real Instagram has.

Take a look at the [frontend](https://github.com/konradgalczynski07/react-instagram) for this project as well.

## Features:

-   registering and logging to user account
-   posting photos
-   commenting and liking photos
-   following system
-   all CRUD operations on posts, comments, follows and likes with relevant permissions

## Technology Stack:

-   Python
-   Django and Django Rest Framework
-   PostgreSQL
-   Docker
-   TravisCI

## Default urls:

- localhost:8000/api/user/register/
- localhost:8000/api/user/login/
- localhost:8000/api/user/me/
- localhost:8000/api/user/<username>/
- localhost:8000/api/user/<username>/follow/
- localhost:8000/api/user/<username>/get-followers/
- localhost:8000/api/user/<username>get-following/
- localhost:8000/api/post/
- localhost:8000/api/post/feed/
- localhost:8000/api/post/<post_id>/
- localhost:8000/api/post/comment/<post_id>/
- localhost:8000/api/post/comment/<comment_id>/
- localhost:8000/api/post/like/<post_id>/
- localhost:8000/api/post/<id>/get_likers/
  
## Instalation
1. Clone Git repository
2. Run `docker-compose up`



Sample response

![screen1](https://scontent-waw1-1.xx.fbcdn.net/v/t1.15752-0/p480x480/51495564_728276204221344_982331429448843264_n.png?_nc_cat=100&_nc_ht=scontent-waw1-1.xx&oh=07b5f711452945557fc6a40959a1f912&oe=5CEE15D7)
