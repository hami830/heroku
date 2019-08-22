from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALchemy_DATABASE_URI'] = 'postgresql://postgres:H@midou8@localhost/FlaskApps'
db = SQLAlchemy(app)
flask sqlalchemy postgres tutorial