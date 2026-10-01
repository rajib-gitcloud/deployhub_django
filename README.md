# DeployHub Django Backend

[![DeployHub Compatible](https://img.shields.io/badge/DeployHub-Ready-brightgreen.svg)](https://deployhub.dev)
[![Framework](https://img.shields.io/badge/Framework-Django%205.x-darkgreen.svg)](https://djangoproject.com)
[![Language](https://img.shields.io/badge/Language-Python%203.11+-blue.svg)]()
[![REST API](https://img.shields.io/badge/API-Django%20REST%20Framework-red.svg)]()

Production-ready Django 5.x REST API starter template engineered for automated deployment on DeployHub and containerized cloud environments.

---

## 🚀 Quick Reference

- **Language / Runtime**: Python 3.11+
- **Framework**: Django 5.x + Django REST Framework
- **WSGI Server**: Gunicorn
- **Default Port**: `8000`
- **Health Check**: `GET /api/health/`

---

## 📁 Project Structure

```text
deployhub_django/
├── api/
│   ├── apps.py
│   ├── urls.py
│   └── views.py             # Health, Info, and Item API views
├── config/
│   ├── asgi.py
│   ├── settings.py          # CORS, DRF, Whitenoise, and DB setup
│   ├── urls.py
│   └── wsgi.py
├── deployhub.json           # Automated deployment specification
├── DEPLOYMENT.md            # Detailed cloud deployment runbook
├── Dockerfile               # Production multi-worker container
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🛠 Local Setup & Running

```bash
# 1. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations and collect static files
python manage.py migrate
python manage.py collectstatic --noinput

# 4. Run development server
python manage.py runserver 0.0.0.0:8000
```

---

## 🐳 Docker Execution

```bash
# Build container image
docker build -t deployhub-django:latest .

# Run container
docker run -d -p 8000:8000 --name django_backend deployhub-django:latest
```

Visit: `http://localhost:8000/api/health/`
