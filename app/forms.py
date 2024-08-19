from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TimeField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class RoutineForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    submit = SubmitField('Save')

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description')
    priority = IntegerField('Priority', validators=[DataRequired()])
    submit = SubmitField('Save')
