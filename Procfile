web: cd clickerApp; gunicorn clickerApp.wsgi
worker: python consumer_socket.py
web: python manage.py runworker channels -v2