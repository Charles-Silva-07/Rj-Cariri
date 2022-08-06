release: python manage.py migrate --noinput
web: gunicorn rjcariri.wsgi --log-file -
worker: python salvar_db.py
