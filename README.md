# Kenya School of Cyber Defense

A server-rendered Django learning platform MVP for cybersecurity courses, learner progress, and safe, simulated exercises.

## Run locally

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Create a learner account from **Get started**. To manage courses and lessons, create an administrator with `python manage.py createsuperuser` and visit `/admin/`.

The local development setup uses SQLite and Django's session authentication. Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, and `DJANGO_ALLOWED_HOSTS` before deploying; configure a production database, HTTPS, static-file hosting, and email delivery as part of deployment.

## Learning and labs

Learners can browse courses, enroll, complete lessons, and track their progress and badges on the dashboard. Course content and lesson challenges are managed in Django Admin. Lab activities are fixed, server-graded scenarios: they do not execute commands, connect to external systems, or run exploit code.

The frontend uses Django templates and responsive CSS so the project runs without a JavaScript build toolchain. React, a separate REST API, and cloud deployment are not part of this MVP.
