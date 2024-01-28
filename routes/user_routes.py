from flask import Blueprint, jsonify, request
from models import db
from models.user_model import User



user_bp = Blueprint('user', __name__)




@user_bp.route('/add-user', methods=['POST'])
def add_user():
    
   
    try:
        data = request.json
        new_user = User(firstName=data['firstName'],lastName=data['lastName'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        response = {
            'message': 'User added',
            'user_id': new_user.id
        }
        return jsonify(response), 201

    except Exception as e:
        error_message = f'Došlo je do pogreške: {str(e)}'
        return jsonify({'error': error_message}), 500


@user_bp.route('/delete-users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        # Pronalaženje korisnika po ID-u
        user_to_delete = User.query.get(user_id)

        if user_to_delete:
            # Brisanje korisnika iz baze podataka
            db.session.delete(user_to_delete)
            db.session.commit()

            # Odgovor s potvrdom
            response = {
                'message': f'Korisnik s ID-om {user_id} uspješno obrisan!'
            }
            return jsonify(response), 200
        else:
            # Ako korisnik nije pronađen
            return jsonify({'error': f'Korisnik s ID-om {user_id} nije pronađen.'}), 404

    except Exception as e:
        # Ako dođe do pogreške
        error_message = f'Došlo je do pogreške: {str(e)}'
        return jsonify({'error': error_message}), 500


