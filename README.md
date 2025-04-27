HumanChain AI Safety Incident Log API
📋 Project Description
This is a simple backend service built with Flask and SQLite to log and manage hypothetical AI safety incidents for HumanChain.

⚙️ Tech Stack
Language: Python

Framework: Flask

Database: SQLite

ORM: SQLAlchemy

🚀 How to Run Locally
Clone or download the project folder.

Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate  # Mac/Linux
Install the dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python app.py
The app will be running at:
http://127.0.0.1:5000/

🗂️ API Endpoints
1. GET /incidents
Retrieve all incidents.

bash
Copy
Edit
curl http://127.0.0.1:5000/incidents
2. POST /incidents
Create a new incident.

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/incidents -H "Content-Type: application/json" -d "{\"title\":\"Sample Incident\",\"description\":\"Example Description\",\"severity\":\"High\"}"
3. GET /incidents/{id}
Retrieve a specific incident by ID.

bash
Copy
Edit
curl http://127.0.0.1:5000/incidents/1
4. DELETE /incidents/{id}
Delete an incident by ID.

bash
Copy
Edit
curl -X DELETE http://127.0.0.1:5000/incidents/1
