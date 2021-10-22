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

- /api/v1/posts//comments/

