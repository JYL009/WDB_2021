# Hiseduplay

Hiseduplay is a Django project for presenting Korean history content, quizzes,
merchandise pages, and a Q&A board.

## Overview

This project was originally built as a personal college project to combine a
history major background with web development. The goal is to make Korean
history content easier to browse through a small website with quiz, product,
member, and Q&A features.

Original project period: 2021.11.22 - 2021.12.15.

## Project Highlights

- Built as a personal college project to share Korean history content through a
  small Django site.
- Includes a home page, quiz page, merchandise page, member registration/login,
  and Q&A board.
- Uses a custom `Member` model backed by the legacy `MEMBER` table.
- Current private-maintenance branch has been cleaned for safer local
  development: secrets are environment-based, generated files are ignored, and
  the app has focused regression tests.

## Feature Overview

### Home

The home page introduces the service, shows a daily history quiz preview, and
links to history-related cards and news content.

<img width="951" alt="Hiseduplay home page" src="docs/images/home.png">

### Merchandise

The merchandise page displays history-related products. Purchase actions are
intended to require login.

<img width="1002" alt="Hiseduplay merchandise page" src="docs/images/merchandise.png">

### Quiz

The quiz page presents Korean history questions and answers.

<img width="1011" alt="Hiseduplay quiz page" src="docs/images/quiz.png">

### Q&A

The Q&A feature lets users browse questions, write posts, open question detail
pages, and add answers.

<img width="969" alt="Hiseduplay Q&A list page" src="docs/images/qna-list.png">

<img width="969" alt="Hiseduplay Q&A write page" src="docs/images/qna-write.png">

### Member Flow

The project includes custom member login and registration pages. The maintained
version hashes newly registered passwords and upgrades legacy plain-text
passwords after successful login.

<img width="1124" alt="Hiseduplay login page" src="docs/images/login.png">

<img width="1024" alt="Hiseduplay sign-up page" src="docs/images/register.png">

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
