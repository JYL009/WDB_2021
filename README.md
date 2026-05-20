# Hiseduplay

Hiseduplay is a Django project for presenting Korean history content, quizzes,
merchandise pages, and a Q&A board.

## Project Highlights

- Built as a personal college project to share Korean history content through a
  small Django site.
- Includes a home page, quiz page, merchandise page, member registration/login,
  and Q&A board.
- Uses a custom `Member` model backed by the legacy `MEMBER` table.
- Current private-maintenance branch has been cleaned for safer local
  development: secrets are environment-based, generated files are ignored, and
  the app has focused regression tests.

## Tech Stack

- Python 3.11
- Django 3.2
- SQLite for local development
- MySQL for deployment, if configured

## Recent Maintenance Improvements

- Removed committed secrets, local databases, bytecode, and obsolete project
  scaffolding.
- Added reproducible install/run instructions.
- Added password hashing for new registrations and automatic upgrade for legacy
  plain-text passwords when users log in.
- Fixed Q&A question/answer creation bugs and replaced broad exception handling
  with explicit object lookups and redirects.
- Added focused tests for authentication, Q&A behavior, and merch/quiz page
  rendering.

## Project Layout

```text
hiseduplay/
  manage.py
  config/
  member/
  merch/
  qna/
  static/
  templates/
```

## Local Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create local environment settings:

```powershell
Copy-Item hiseduplay\.env.example hiseduplay\.env.local
```

Run database migrations:

```powershell
Set-Location hiseduplay
python manage.py migrate
```

Start the development server:

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## MySQL Setup

For MySQL, install the optional dependency file:

```powershell
python -m pip install -r requirements-mysql.txt
```

Then update `hiseduplay/.env.local` with MySQL values:

```text
DJANGO_DB_ENGINE=django.db.backends.mysql
DJANGO_DB_NAME=hiseduplay
DJANGO_DB_USER=your-db-user
DJANGO_DB_PASSWORD=your-db-password
DJANGO_DB_HOST=localhost
DJANGO_DB_PORT=3306
```

## Environment Variables

`hiseduplay/config/settings.py` loads `hiseduplay/.env` first, then
`hiseduplay/.env.local` with override enabled. Real secret values must stay in
one of those ignored local files or in deployment environment variables.

Required:

- `DJANGO_SECRET_KEY`

Optional:

- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_DB_ENGINE`
- `DJANGO_DB_NAME`
- `DJANGO_DB_USER`
- `DJANGO_DB_PASSWORD`
- `DJANGO_DB_HOST`
- `DJANGO_DB_PORT`

## Verification

After installing dependencies:

```powershell
Set-Location hiseduplay
python manage.py check
python manage.py migrate
python manage.py test member qna merch
```
