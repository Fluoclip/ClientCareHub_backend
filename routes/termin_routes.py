from flask import Blueprint, jsonify, request
from models import db
from models.termin_model import Termin


termin_bp = Blueprint('termin', __name__)




@termin_bp.route('/add-termin', methods=['POST'])
def add_termin():
    try:
        data = request.json
        new_termin = Termin(client=data['client'],location=data['location'],time=data['time'], date=data['date'], description=data['description'])
        db.session.add(new_termin)
        db.session.commit()
        response = {
            'message': 'Termin added',
            'termin_id': new_termin.id
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = f'Došlo je do pogreške: {str(e)}'
        return jsonify({'error': error_message}), 500