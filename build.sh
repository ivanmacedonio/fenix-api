#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('gonzalo', 'gonzalo@gmail.com', 'fenix123')" | python manage.py shell
