# AI Safety Incident Log API

A simple RESTful API service to log and manage AI safety incidents, built for the HumanChain Backend Intern Assignment.

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
- **Database**: SQLite (via SQLAlchemy ORM)

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd ai_safety_backend
```

### 2. Set Up Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Database (`database.db`) is auto-created when you first run the app.
It uses the `Incident` model defined in `models.py`.

To manually create the database:

```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

✅ **Optional**: Pre-populate the database with 2-3 sample incidents by running POST API calls (examples below).

---

## 🚀 Running the Server

Make sure the virtual environment is activated, then:

```bash
python app.py
```

Server will start at:  
➡️ `http://127.0.0.1:5000/`

---

## 🔥 API Endpoints

All responses and requests use **JSON**.

---

### 1. Get All Incidents

- **Endpoint**: `GET /incidents`
- **Description**: Retrieves all incidents.

```bash
curl http://127.0.0.1:5000/incidents
```

---

### 2. Create a New Incident

- **Endpoint**: `POST /incidents`
- **Description**: Log a new AI safety incident.

```bash
curl -X POST http://127.0.0.1:5000/incidents \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Incident","description":"Something went wrong","severity":"Medium"}'
```

✅ Valid severity values: `Low`, `Medium`, `High`

---

### 3. Get Incident by ID

- **Endpoint**: `GET /incidents/<id>`
- **Description**: Retrieve a specific incident.

```bash
curl http://127.0.0.1:5000/incidents/1
```

---

### 4. Delete Incident by ID

- **Endpoint**: `DELETE /incidents/<id>`
- **Description**: Delete an incident.

```bash
curl -X DELETE http://127.0.0.1:5000/incidents/1
```

---

## ⚙️ Environment Variables

No external environment variables are required for this basic version.  
The database is configured as:

```python
sqlite:///database.db
```

If needed, you can modify `app.config['SQLALCHEMY_DATABASE_URI']` in `app.py`.

---

## 🛠️ Design Decisions

- **Flask** was chosen for its simplicity and lightweight setup.
- **SQLite** was selected to avoid extra installation overhead.
- The API is fully RESTful and returns appropriate status codes (e.g., `201`, `400`, `404`, `200`).

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

## 🎉 Congratulations!

You are now ready to interact with the AI Safety Incident Log API!
