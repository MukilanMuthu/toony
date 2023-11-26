from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    promt0 = TextAreaField()
    promt1 = TextAreaField()
    promt2 = TextAreaField()
    promt3 = TextAreaField()
    promt4 = TextAreaField()
    promt5 = TextAreaField()
    promt6 = TextAreaField()
    promt7 = TextAreaField()
    promt8 = TextAreaField()
    promt9 = TextAreaField()
    submit = SubmitField("Create Comic")
