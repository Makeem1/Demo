from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField 
from wtforms.validators import DataRequired, Length, Email, InputRequired



class TaskForm(FlaskForm):
    firstname = StringField("First Name ", validators=[ InputRequired(), Length(min = 4, max = 20)  ])
    lastname = StringField("Last Name ", validators=[InputRequired(), Length(min = 4, max = 20)])
    message = StringField("Message ", validators=[InputRequired(), Length(min = 10, max = 1800)])
    duration = IntegerField("Duration", validators=[InputRequired()])
    duration_unit = SelectField('unit', choices=['Minutes', 'Hours', 'Days'])
    submit = SubmitField("Send")