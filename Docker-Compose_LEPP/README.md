# Docker-Compose_LEPP  
Nginx, Gunicorn, Django, PostgreSQL 스택을 사용하는 웹 사이트를 Docker Compose로 구현  


## 초기설정  
1. `pip install -r settings/requirements.txt`  
2. `django-admin startproject project`  
3. `mkdir project/static`  
4. `mkdir database`  
5. `project/project/settings` 수정  
```python
import os
...
SECRET_KEY = os.environ.get("SECRET_KEY")
...
DEBUG = False
...
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
...
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqplite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
...
STATIC_ROOT = '/project/static'
```  
위 다섯 단계를 진행하면 아래의 구조를 갖는다.  
<pre>
.
├── README.md
├── database
├── docker-compose.yml
├── project
│   ├── manage.py
│   ├── project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── static
└── settings
    ├── env
    │   ├── postgresql.env
    │   └── python.env
    ├── nginx
    │   └── nginx.conf
    └── python
        ├── Dockerfile
        └── requirements.txt
</pre>  


## 배포  
1. `cd project`  
2. `python manage.py collectstatic`  
3. `python manage.py makemigrations <app-name>`  
4. `cd ../`  
5. `APP_NAME=이름 docker-compose up -d`  
