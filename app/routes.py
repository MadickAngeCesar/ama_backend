from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Routine, Task
from .forms import RoutineForm, TaskForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    routines = Routine.query.all()
    tasks = Task.query.all()
    return render_template('index.html', routines=routines, tasks=tasks)

@main.route('/routine_add', methods=['GET', 'POST'])
def add_routine():
    form = RoutineForm()
    if form.validate_on_submit():
        routine = Routine(
            title=form.title.data,
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data
        )
        db.session.add(routine)
        db.session.commit()
        flash('Routine added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_routine.html', form=form)

@main.route('/tasks_add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data
        )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!')
        return redirect(url_for('main.index'))
    return render_template('add_task.html', form=form)


@main.route('/routine_update/<int:id>', methods=['GET', 'POST'])
def update_routine(id):
    routine = Routine.query.get_or_404(id)
    form = RoutineForm(obj=routine)
    if form.validate_on_submit():
        routine.title = form.title.data
        routine.description = form.description.data
        routine.start_time = form.start_time.data
        routine.end_time = form.end_time.data
        db.session.commit()
        flash('Routine updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('update_routine.html', form=form)

@main.route('/task_update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('update_task.html', form=form)

@main.route('/routine_delete/<int:id>', methods=['POST'])
def delete_routine(id):
    routine = Routine.query.get_or_404(id)
    db.session.delete(routine)
    db.session.commit()
    flash('Routine deleted successfully!')
    return redirect(url_for('main.index'))

@main.route('/task_delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!')
    return redirect(url_for('main.index'))

