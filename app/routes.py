from flask import Blueprint, request, jsonify
from . import db
from .models import Routine, Task
from datetime import datetime

main = Blueprint('main', __name__)

# Utility function to handle time parsing with support for both HH:MM and HH:MM:SS formats
def parse_time(time_str):
    for fmt in ('%H:%M', '%H:%M:%S'):
        try:
            return datetime.strptime(time_str, fmt).time()
        except ValueError:
            continue
    return None

# Get all routines
@main.route('/api/routines', methods=['GET'])
def get_routines():
    routines = Routine.query.all()
    return jsonify([r.to_dict() for r in routines])

# Get all tasks
@main.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])

# Get a single routine by ID
@main.route('/api/routine/<int:id>', methods=['GET'])
def get_routine(id):
    routine = Routine.query.get(id)
    if routine:
        return jsonify(routine.to_dict())
    return jsonify({'message': 'Routine not found'}), 404

# Get a single task by ID
@main.route('/api/task/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if task:
        return jsonify(task.to_dict())
    return jsonify({'message': 'Task not found'}), 404

# Add a new routine
@main.route('/api/routine', methods=['POST'])
def add_routine():
    data = request.get_json()
    start_time = parse_time(data.get('start_time'))
    end_time = parse_time(data.get('end_time'))

    if not start_time or not end_time:
        return jsonify({'message': 'Invalid time format. Use HH:MM or HH:MM:SS.'}), 400

    routine = Routine(
        title=data['title'],
        start_time=start_time,
        end_time=end_time,
        description=data['description']
    )
    db.session.add(routine)
    db.session.commit()
    return jsonify(routine.to_dict()), 201


# Add a new task
@main.route('/api/task', methods=['POST'])
def add_task():
    data = request.get_json()
    task = Task(
        title=data['title'],
        priority=data['priority'],
        description=data['description']
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

# Update an existing routine
@main.route('/api/routine/<int:id>', methods=['PUT'])
def update_routine(id):
    routine = Routine.query.get(id)
    if not routine:
        return jsonify({'message': 'Routine not found'}), 404

    data = request.get_json()
    start_time = parse_time(data.get('start_time'))
    end_time = parse_time(data.get('end_time'))

    if start_time is not None:
        routine.start_time = start_time
    if end_time is not None:
        routine.end_time = end_time

    routine.title = data.get('title', routine.title)
    routine.description = data.get('description', routine.description)
    db.session.commit()
    return jsonify(routine.to_dict()), 200

# Update an existing task
@main.route('/api/task/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.priority = data.get('priority', task.priority)
    task.description = data.get('description', task.description)
    db.session.commit()
    return jsonify(task.to_dict()), 200

# Delete a routine
@main.route('/api/routine/<int:id>', methods=['DELETE'])
def delete_routine(id):
    routine = Routine.query.get(id)
    if routine:
        db.session.delete(routine)
        db.session.commit()
        return jsonify({'message': 'Routine deleted successfully!'}), 200
    return jsonify({'message': 'Routine not found!'}), 404

# Delete a task
@main.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted successfully!'}), 200
    return jsonify({'message': 'Task not found!'}), 404
