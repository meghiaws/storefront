## Storefront
Storefront is a RESTful Store build with Django and Django Rest Framework.

## Features
- Authentication with email using JWT
- Adding new Collection and Products to store by admin
- Viewing products by customers and add them to their cart
- Add new items to cart or update quantity of existing item
- Make an order by customers
- Automatically remove shopping cart after making order
- Ability to view and update user profiles for customers and admins
- Easy insatllation
- Production-ready configuration for Static Files, Database Settings, Gunicorn, Docker
- Cloud-native design using 12-factor methodology

## Technologies used
- [Python 3.9](https://www.python.org/) - Programming Language
- [Django](https://docs.djangoproject.com/en/3.2/releases/3.2/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - For Building RESTful APIs
- [Pytest](https://docs.pytest.org/en/7.0.x/) - Automated Testing
- [Docker](https://www.docker.com/) - Container Platform
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Git](https://git-scm.com/doc) - Version Control System
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server
- [Celery](https://github.com/celery/celery) - Task Queue
- [Flower](https://github.com/mher/flower) - Monitoring Celery Tasks
- [Locust](https://github.com/locustio/locust) - Performance Testing
- [Silk](https://github.com/jazzband/django-silk) - Profiling

## Installation
Clone the project
``` 
git clone https://github.com/meghiaws/storefront.git && cd storefront && poetry install 
```
⚠️ Please enter the required information in the .env and files before running the project.

Create docker networks
```
docker network create postgres_network
docker network create pgadmin_network
```
Create docker volumes
```
docker volume create postgresql_data
docker volume create pgadmin
docker volume create redisdata
```
Now you can run the project
```
docker-compose up -d -build
```
You currently have 7 containers running
- web
- db
- pgadmin
- redis
- celery
- celery-beat
- tests

You access to app from `0.0.0.0:8000` and access to pdadmin from `0.0.0.0:5050`



