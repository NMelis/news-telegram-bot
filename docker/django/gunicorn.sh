#!/usr/bin/env sh

set -o errexit
set -o nounset

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:
export DJANGO_ENV

# Run python specific scripts:
# Running migrations in startup script might not be the best option, see:
# docs/_pages/template/going-to-production.rst
python /code/manage.py migrate --noinput
#python /code/manage.py collectstatic --noinput
#python /code/manage.py compilemessages
#
#python3 manage.py celery worker &
#python3 manage.py celery beat --pidfile /tmp/celerybeat.pid &
#python3 manage.py celery -A server flower --port=5555 &

# Start gunicorn with 4 workers:
/usr/local/bin/gunicorn server.wsgi -w 4 -b 0.0.0.0:8000 --chdir=/code --reload
