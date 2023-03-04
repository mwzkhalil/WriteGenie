from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TextInputForm(FlaskForm):
    text = StringField('Enter your text:', validators=[DataRequired()])
    submit = SubmitField('Submit')
