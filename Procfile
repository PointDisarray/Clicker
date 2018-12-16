web: cd clickerApp; gunicorn clickerApp.wsgi
worker: python consumer_socket.py
web: python clickerApp/manage.py runworker channels -v2