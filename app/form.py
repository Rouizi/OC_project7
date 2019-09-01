from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    username = StringField('Adresse', validators=[DataRequired()])
    submit = SubmitField('Envoyez')