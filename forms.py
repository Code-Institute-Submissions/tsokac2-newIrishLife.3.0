import os
from flask import Flask, request, session
from flask_wtf import FlaskForm
from wtforms import(
    StringField, PasswordField, SubmitField,
    TextAreaField, SelectField)
from wtforms.validators import (
    DataRequired, Length, Regexp,
    Email, EqualTo, ValidationError)
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)