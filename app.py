from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guests.db'
app.config['UPLOAD_FOLDER'] = 'static/images'  # Folder where images will be stored
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
db = SQLAlchemy(app)

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    relationship_status = db.Column(db.String(100))
    picture = db.Column(db.String(255))  # Store the filename of the image
    favorite_song = db.Column(db.String(100))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/guests')
def guests():
    all_guests = Guest.query.all()
    return render_template('guests.html', guests=all_guests)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        filename = None
        if 'picture' in request.files:
            file = request.files['picture']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        new_guest = Guest(
            name=request.form['name'],
            surname=request.form['surname'],
            email=request.form['email'],
            relationship_status=request.form['relationship_status'],
            picture=filename,
            favorite_song=request.form['favorite_song']
        )
        db.session.add(new_guest)
        db.session.commit()
        return redirect(url_for('guests'))
    return render_template('register.html')

def create_database():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_database()
    app.run(debug=True)
