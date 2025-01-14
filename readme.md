docker compose up --build
docker compose run django-web python manage.py migrate
https://www.docker.com/blog/how-to-dockerize-django-app/