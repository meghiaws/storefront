release: python manage.py migrate
web: gunicorn storefront.wsgi
celery: celery -A storefront worker
