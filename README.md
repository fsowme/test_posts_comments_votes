## Test votes

### Запуск

```
git clone git@github.com:fsowme/test_posts_comments_votes.git
cd test_posts_comments_votes
touch .env
```
- .env:  
    ```
    SECRET_KEY="secret_key"
    DB_ENGINE="django.db.backends.postgresql"
    DB_HOST="db"
    DP_PORT="5432"
    POSTGRES_DB="db_name"
    POSTGRES_USER="postgres"
    POSTGRES_PASSWORD="postgres"
    ```
```
docker-compose up -d
docker exec -it <id контейнера c приложением> bash
python manage.py migrate
```

## Использование
- /api/v1/posts/<**post_title**>/votes
    ```
    - список плюсов и минусов к посту
    - GET для всех, остальные для авторизованных
    - фильтр по плюсам и минусам через параметр запроса: ?vote_type=<upvote или downvote>
    ```
- /api/v1/posts/<**post_title**>/votes/count
    ```
    - общее количество плюсов и минусов к посту
    - количество только плюсов или только минусов через параметр запроса: ?vote_type=<upvote или downvote>
    ```
- posts/<**post_title**>/comments/<**comment_id**>/votes
    ```
    - как и с постами, только для комментариев
    ```
- posts/<**post_title**>/comments/<**comment_id**>/votes/count
    ```
    - как и с постами, только для комментариев
    ```
- /api/v1/posts/<**post_title**>/comments/ 
    ```
    - список комментариев к посту со списком плюсов/минусов
    - для всех только GET
    ```

### Технологии
[Django](https://www.djangoproject.com/)

[Django REST framework](https://www.django-rest-framework.org/)
