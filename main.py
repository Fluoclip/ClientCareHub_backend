from flask import Flask, request, jsonify, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bananajezuta'

# our database uri
username = "fluoclip"
password = "464130"
dbname = "testDB"
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@localhost:5432/{dbname}"

db = SQLAlchemy(app)



# Create A Model For Table
class BlogPosts(db.Model):
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



if __name__ == "__main__":
    app.run(debug=True)