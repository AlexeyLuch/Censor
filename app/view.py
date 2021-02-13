from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import FileField
from flask_uploads import configure_uploads, IMAGES, UploadSet
from app import app
from celery import Celery


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('base.html',)