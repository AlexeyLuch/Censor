from wtforms import  MultipleFileField, Form, TextAreaField, DateField, SubmitField, StringField,IntegerField
from flask_wtf.file import FileField, FileRequired

class WarForm(Form):
    title = StringField('Title')
    description = TextAreaField("Description")
    body = TextAreaField("Body")
    image = FileField(validators=[FileRequired()])
