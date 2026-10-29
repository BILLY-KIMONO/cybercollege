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

The local development setup uses SQLite and Django's session authentication. For production, configure a persistent PostgreSQL database and set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0`, and `DATABASE_URL`; SQLite files are not durable on serverless hosts.

## Deploy to Vercel

Vercel detects this Django project from `manage.py` and uses the configured ASGI application. It runs `collectstatic` and serves the files from `staticfiles/` through its CDN.

1. Import this repository into Vercel.
2. Add a PostgreSQL database integration or provider and set `DATABASE_URL` in the Vercel project environment variables.
3. Set `DJANGO_SECRET_KEY` to a new, long random value and set `DJANGO_DEBUG` to `0`.
4. Set `DJANGO_ALLOWED_HOSTS` to include the Vercel hostname and any custom domains, separated by commas. Vercel's `VERCEL_URL` is also allowed automatically.
5. Set `DJANGO_CSRF_TRUSTED_ORIGINS` to the corresponding HTTPS origins, separated by commas (for example, `https://your-app.vercel.app`).
6. Link the project with the Vercel CLI and run `vercel env pull .env.local`. Then run `python manage.py migrate` and, if desired, `python manage.py seed_demo` from the project directory.
7. Deploy. Vercel loads the Django app and serves its collected static files.

The `.env.example` file lists the required settings. Do not commit real credentials. The app loads a local `.env.local` file for management commands; it is ignored by Git. Database migrations are not run automatically during builds, and SQLite is only used for local development.

## Learning and labs

Learners can browse courses, enroll, complete lessons, and track their progress and badges on the dashboard. Course content and lesson challenges are managed in Django Admin. Lab activities are fixed, server-graded scenarios: they do not execute commands, connect to external systems, or run exploit code.

The frontend uses Django templates and responsive CSS so the project runs without a JavaScript build toolchain. React, a separate REST API, and cloud deployment are not part of this MVP.

## Diploma-style curriculum

Run `python manage.py seed_demo` to add or refresh the four foundation courses and a 24-module learning pathway arranged across four semesters. The pathway covers security fundamentals and professional practice; systems, networks, programming, governance, cryptography, and identity; security operations, incident response, digital forensics, secure development, application security, and cloud; and threat intelligence, authorized assessment, audit, resilience, emerging technologies, and a supervised capstone. Each diploma-style module includes eight five-hour guided lessons, for 40 planned learning hours: seven articles and a fixed, defensive scenario. Every lesson includes learning outcomes, lesson notes, guided and independent activities, a knowledge check, assessment guidance, and an explicit time allocation. The work is a structured study plan, not a promise of 40 hours of instructor contact or an accredited qualification.

This learning pathway is an educational outline, not an accredited Kenyan diploma, a qualification, or a substitute for review against the current requirements of an authorized examining body. It does not teach or authorize testing of real third-party systems.
