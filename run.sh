./.heroku/python/bin/poetry config virtualenvs.create false
./.heroku/python/bin/poetry install --no-dev
./.heroku/python/bin/python manage.py migrate
./.heroku/python/bin/gunicorn online_market.wsgi
