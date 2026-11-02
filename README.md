# Portfolio-SDGKU

A Django-based personal portfolio web application built for FSDI 117 at SDGKU. It showcases projects and the skills used to build them, with an admin-friendly way to add new entries.

## Features

- **Projects** — list, detail view, featured flag, GitHub and live URLs, image uploads
- **Skills** — categorized (frontend, backend, database, tools, other) with icons, linked to projects via a many-to-many relationship
- **Add Project** form directly from the UI
- Django admin for managing content
- Media uploads for project images and skill icons

## Tech Stack

- Python 3 / Django 6.1
- SQLite (default dev database)
- Pillow for image handling
- HTML templates (Django template language)

## Project Structure

```
Portfolio Project/
├── config/           # Django project settings, URLs, WSGI/ASGI
├── portfolio/        # Main app: models, views, forms, urls
├── templates/        # base.html, navbar.html, portfolioTemplates/
├── static/           # Static assets
├── media/            # Uploaded images (gitignored)
├── manage.py
└── requirements.txt
```

## Installation

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd "Portfolio Project"
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (to access the admin)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit:

- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Usage

1. Log into the admin to add Skills (with optional icons) and Projects.
2. Browse the project list from the home page.
3. Click a project to view details and the skills it uses.
4. Use **Add Project** in the nav to create a project from the UI.

## URLs

| Path | View |
|------|------|
| `/` | Project list |
| `/project/<id>/` | Project detail |
| `/project/add/` | Add a new project |
| `/skills/` | Skill list |
| `/admin/` | Django admin |

## License

Educational project — SDGKU FSDI 117.
