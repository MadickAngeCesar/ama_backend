from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TimeField, SubmitField, IntegerField, SelectField
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
    priority = SelectField('Priority', choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], validators=[DataRequired()])
    submit = SubmitField('Save')
