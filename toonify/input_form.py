from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    prompt0 = TextAreaField(validators=[DataRequired()])
    annot0 = BooleanField()
    prompt1 = TextAreaField(validators=[DataRequired()])
    annot1 = BooleanField()
    prompt2 = TextAreaField(validators=[DataRequired()])
    annot2 = BooleanField()
    prompt3 = TextAreaField(validators=[DataRequired()])
    annot3 = BooleanField()
    prompt4 = TextAreaField(validators=[DataRequired()])
    annot4 = BooleanField()
    prompt5 = TextAreaField(validators=[DataRequired()])
    annot5 = BooleanField()
    prompt6 = TextAreaField(validators=[DataRequired()])
    annot6 = BooleanField()
    prompt7 = TextAreaField(validators=[DataRequired()])
    annot7 = BooleanField()
    prompt8 = TextAreaField(validators=[DataRequired()])
    annot8 = BooleanField()
    prompt9 = TextAreaField(validators=[DataRequired()])
    annot9 = BooleanField()
    submit = SubmitField("Create masterpiece !!")
