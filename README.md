# AI Safety Incident Log API

A simple RESTful API service to log and manage AI safety incidents, built using Flask and SQLAlchemy.

---

## 📚 Project Overview

This backend service allows users to:
- Log new AI safety incidents.
- Retrieve all incidents.
- Retrieve a specific incident by ID.
- Delete an incident.

It uses:
- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (via SQLAlchemy)

---

## 📦 Installation & Setup

### 1. Prerequisites

- Python 3.8+
- pip (Python package manager)

Check if installed:

```bash
python --version
pip --version
```


### 2. Project Setup

Create a new folder and set up a virtual environment:

```bash
mkdir ai_safety_backend
cd ai_safety_backend
python -m venv venv
```

Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

---

### 3. Install Required Packages

```bash
pip install Flask SQLAlchemy

---

### 4. Create Project Files

Create the following files:

- `app.py`
- `models.py`
- `requirements.txt`

`database.db` will be auto-created when the server runs.

To create empty files quickly:

```bash
touch app.py models.py requirements.txt
```

---

## 🚀 Running the Server

Activate the virtual environment (if not already activated):

```bash
# Windows
venv\Scripts\activate

```

Run the application:

```bash
python app.py
```

Server will be available at:  
➡️ `http://127.0.0.1:5000/`

---

## 🔥 API Endpoints

All API requests and responses use **JSON** format.

---

### 1. Get All Incidents

- **Method**: GET
- **URL**: `/incidents`

```bash
curl http://127.0.0.1:5000/incidents
```

---

### 2. Create a New Incident

- **Method**: POST
- **URL**: `/incidents`

```bash
curl -X POST http://127.0.0.1:5000/incidents \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Incident","description":"Something went wrong","severity":"Medium"}'
```

---

### 3. Get Incident by ID

- **Method**: GET
- **URL**: `/incidents/<id>`

```bash
curl http://127.0.0.1:5000/incidents/1
```

---

### 4. Delete Incident by ID

- **Method**: DELETE
- **URL**: `/incidents/<id>`

```bash
curl -X DELETE http://127.0.0.1:5000/incidents/1
```

---

## 📄 Requirements

Listed in `requirements.txt`:

```
Flask
SQLAlchemy
```

Install them with:

```bash
pip install -r requirements.txt
```

---

