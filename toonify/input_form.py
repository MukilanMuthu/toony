from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    prompt0 = TextAreaField(validators=[DataRequired()])
    prompt1 = TextAreaField(validators=[DataRequired()])
    prompt2 = TextAreaField(validators=[DataRequired()])
    prompt3 = TextAreaField(validators=[DataRequired()])
    prompt4 = TextAreaField(validators=[DataRequired()])
    prompt5 = TextAreaField(validators=[DataRequired()])
    prompt6 = TextAreaField(validators=[DataRequired()])
    prompt7 = TextAreaField(validators=[DataRequired()])
    prompt8 = TextAreaField(validators=[DataRequired()])
    prompt9 = TextAreaField(validators=[DataRequired()])
    submit = SubmitField("Create Comic")
