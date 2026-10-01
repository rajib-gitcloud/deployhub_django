# Deployment Guide: Django on DeployHub

This guide details deploying `deployhub_django` with automated CI/CD and zero-downtime health probing.

## ⚙️ Configuration Manifest

```json
{
  "name": "deployhub_django",
  "framework": "Django",
  "runtime": "python",
  "port": 8000,
  "buildCommand": "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate",
  "startCommand": "gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3",
  "healthCheck": {
    "path": "/api/health/",
    "expectedStatus": 200,
    "timeoutSeconds": 10
  }
}
```

## 🔐 Environment Variables

| Variable | Required | Default | Description |
| :--- | :-: | :--- | :--- |
| `SECRET_KEY` | Yes | Generated | Django cryptographic signing key |
| `DEBUG` | No | `False` | Debug mode toggle |
| `ALLOWED_HOSTS` | Yes | `*` | Comma-separated list of allowed host domains |
| `PORT` | No | `8000` | HTTP listening port |
