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

## Free demo hosting (Render + Neon)

The repository includes a Render Blueprint for a free web service. For a database that persists beyond Render's short-lived free database trial, create a free PostgreSQL project with [Neon](https://neon.tech/) and use its pooled connection string as `DATABASE_URL`. Make sure the connection string includes SSL mode (Neon includes it by default).

1. Push this repository to GitHub and create or sign in to a Render account.
2. In Render, choose **New → Blueprint**, select this GitHub repository, and confirm the `render.yaml` settings.
3. When prompted for `DATABASE_URL`, paste the connection string from your Neon project.
4. Deploy. Render installs dependencies, collects static assets, applies migrations, and seeds the original courses on startup.
5. Open the generated `*.onrender.com` URL. The first request after a quiet period can take about a minute while the free service wakes.

This is suitable for a preview or small learning demo, not a production school: free Render web services sleep when idle and have limited monthly usage. Free database quotas and terms can change; confirm them with the provider before relying on the service for learner records. Back up important data and never use this demo setup for sensitive information.

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

Learners can browse original learning paths, enroll, and move through room-style lessons with path maps, previous/next navigation, saved progress, and dashboard resume links. Course content and lesson challenges are managed in Django Admin. Lab activities are fixed, server-graded scenarios: they do not execute commands, connect to external systems, or run exploit code. This is a self-paced learning platform, not a live cyber range; practical work uses written exercises and safe simulations.

The frontend uses Django templates and responsive CSS so the project runs without a JavaScript build toolchain. React, a separate REST API, and cloud deployment are not part of this MVP.

## Diploma-style curriculum

Run `python manage.py seed_demo` to add or refresh the four foundation courses and a 24-module learning pathway arranged across four semesters. The pathway covers security fundamentals and professional practice; systems, networks, programming, governance, cryptography, and identity; security operations, incident response, digital forensics, secure development, application security, and cloud; and threat intelligence, authorized assessment, audit, resilience, emerging technologies, and a supervised capstone. Each diploma-style module includes eight five-hour guided lessons, for 40 planned learning hours: seven articles and a fixed, defensive scenario. Lessons include topic-specific teaching notes, worked examples, guided and independent study instructions, knowledge checks with model-answer guidance, an assessment rubric, submission checklist, and explicit time allocation. The work is a structured study plan, not a promise of 40 hours of instructor contact or an accredited qualification.

The same command also adds three four-hour specialist courses: practical phishing and email security, secure coding essentials, and cloud security fundamentals. Each includes four complete one-hour lessons with learning outcomes, detailed notes, guided and independent practice, knowledge checks, and review guidance. Each course includes one fixed, defensive scenario that does not connect to live systems.

For advanced learners, the seed command adds two 40-hour professional study tracks: Defensive Security Operations and Incident Response, and Authorized Offensive Security Assessment. Each track has eight complete five-hour lessons and a fixed tabletop capstone. The defensive track covers SOC workflow, telemetry, triage, detection quality, incident coordination, evidence handling, and recovery. The offensive track covers written authorization, scope, threat modeling, approved-record review, safe evidence assessment, design review, reporting, and remediation. Offensive work uses fictional materials only; it does not teach or authorize testing live or third-party systems. The existing CYB-406 supervised capstone provides a portfolio-oriented endpoint to the four-semester curriculum. These study paths are educational, not accredited qualifications or job guarantees.

This learning pathway is an educational outline, not an accredited Kenyan diploma, a qualification, or a substitute for review against the current requirements of an authorized examining body. It does not teach or authorize testing of real third-party systems.
