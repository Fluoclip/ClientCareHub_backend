from flask import Flask, request, jsonify, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 
import psycopg2 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'bananajezuta'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fluoclip:464130@100.124.214.138:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# Create A Model For Table
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable = False)
    email = db.Column(db.String(6000), nullable = False)


@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data={
        "user_id": user_id,
        "name": "Banana",
        "email": "banana@banana.ba"
    }
    return jsonify(user_data), 200
@app.route('/add-users', methods=['POST'])
def add_user():
    try:
        # Podaci iz zahtjeva
        data = request.json

        # Stvaranje novog korisnika
        new_user = User(name=data['name'], email=data['email'])

        # Dodavanje korisnika u bazu podataka
        db.session.add(new_user)
        db.session.commit()

        # Odgovor s potvrdom
        response = {
            'message': 'Korisnik uspješno dodan!',
            'user_id': new_user.id
        }
        return jsonify(response), 201

    except Exception as e:
        # Ako dođe do pogreške
        error_message = f'Došlo je do pogreške: {str(e)}'
        return jsonify({'error': error_message}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # <--- create db object.
    app.run(debug=True)