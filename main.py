from flask import Flask, request, jsonify, url_for, redirect, render_template
import psycopg2 
from models import db
from routes.termin_routes import termin_bp
from routes.user_routes import user_bp








app = Flask(__name__)
app.config['SECRET_KEY'] = 'bananajezuta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fluoclip:464130@100.124.214.138:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(termin_bp, url_prefix='/termin')

@app.route("/")
def home():
    return "Home"










if __name__ == "__main__":
    with app.app_context():
        db.create_all() # <--- create db object.
    app.run(debug=True)