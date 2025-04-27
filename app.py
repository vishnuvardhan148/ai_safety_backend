from flask import Flask, request, jsonify
from models import db, Incident

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([{
        'id': i.id,
        'title': i.title,
        'description': i.description,
        'severity': i.severity,
        'reported_at': i.reported_at
    } for i in incidents])

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    severity = data.get('severity')

    if not title or not description or severity not in ["Low", "Medium", "High"]:
        return jsonify({'error': 'Invalid input'}), 400

    incident = Incident(title=title, description=description, severity=severity)
    db.session.add(incident)
    db.session.commit()

    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at
    }), 201

@app.route('/incidents/<int:id>', methods=['GET'])
def get_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({'error': 'Not found'}), 404

    return jsonify({
        'id': incident.id,
        'title': incident.title,
        'description': incident.description,
        'severity': incident.severity,
        'reported_at': incident.reported_at
    })

@app.route('/incidents/<int:id>', methods=['DELETE'])
def delete_incident(id):
    incident = Incident.query.get(id)
    if not incident:
        return jsonify({'error': 'Not found'}), 404

    db.session.delete(incident)
    db.session.commit()
    return jsonify({'message': 'Deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
