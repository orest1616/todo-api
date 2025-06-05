# ✅ ToDo API

Simple RESTful API for managing personal tasks.  
Built with Django, DRF, JWT, and Docker.

---

## 🛠️ Requirements

### ✅ Install Docker

- **Windows & macOS**: [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Linux**: Follow the official guide → https://docs.docker.com/engine/install/

Verify Docker:

```bash
docker --version
docker compose version
```

### ✅ Install Git

Download Git: https://git-scm.com/downloads

Verify:

```bash
git --version
```

---

## 🚀 Project Setup (via Docker)

### 1. Clone the repository

```bash

```

### 2. Build and run containers

```bash
docker-compose up --build
```

### 3. Apply database migrations

```bash
docker-compose exec web python manage.py migrate
```

### 4. (Optional) Create superuser for Django Admin
#### A default superuser is automatically created with the following credentials Username: admin Password: admin
#### If you want to manually create a different superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 🧪 Running Tests

```bash
docker-compose exec web python manage.py test
```

---

## 🔐 Authentication

The API uses JWT (JSON Web Tokens).  
To obtain a token:

### ➤ POST `/api/token/`

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

You will receive:

```json
{
  "refresh": "...",
  "access": "..."
}
```

Use the `access` token in your headers for authenticated requests:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## 📮 API Endpoints

| Method | Endpoint           | Description               |
|--------|--------------------|---------------------------|
| POST   | `/api/tasks/`      | Create a new task         |
| GET    | `/api/tasks/`      | List all tasks            |
| PUT    | `/api/tasks/{id}/` | Update a task             |
| DELETE | `/api/tasks/{id}/` | Delete a task             |

Supports filtering by `status` and `due_date` via query params:

```
/api/tasks/?status=pending
/api/tasks/?due_date=2025-06-10
```

---

## 📂 Tech Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- PostgreSQL
- JWT Auth (Simple JWT)
- Docker & Docker Compose

---

## ✅ Done ✔️

- ✅ Auth via JWT
- ✅ CRUD operations for tasks
- ✅ Filtering by `status` & `due_date`
- ✅ Dockerized setup
- ✅ Unit tests

---
