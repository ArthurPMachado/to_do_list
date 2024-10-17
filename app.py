from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_id_control
  data = request.get_json()
  new_task = Task(id=task_id_control, title=data['title'], description=data.get('description', ''))
  task_id_control += 1
  tasks.append(new_task)

  response = {
    "message": 'New task created successfully',
    "id": new_task.id
  }

  return jsonify(response), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
  task_list = [task.to_dict() for task in tasks]
  output = {
    "tasks": task_list,
    "total_tasks": len(task_list)
  }

  return output

@app.route('/tasks/<int:taskid>', methods=['GET'])
def get_task(taskid):
  for task_db in tasks:
    if task_db.id == taskid:
      return jsonify(task_db.to_dict())

  return jsonify({'message': 'Task was not found'}), 404

@app.route('/tasks/<int:taskid>', methods=['PUT'])
def update_task(taskid):
  task = None
  for task_db in tasks:
    if task_db.id == taskid:
      task = task_db
      break
  
  if not task:
    return jsonify({'message': 'Task was not found'}), 404
  
  data = request.get_json()
  task.title = data['title']
  task.description = data.get('description')
  task.completed = data['completed']
  
  response = {
    'message': 'Task updated successfully'
  }

  return jsonify(response), 204

@app.route('/tasks/<int:taskid>', methods=['DELETE'])
def delete_task(taskid):
  task = None
  for task_db in tasks:
    if task_db.id == taskid:
      task = task_db
      break
  
  if not task:
    return jsonify({'message': 'Task was not found'}), 404
  
  tasks.remove(task)
  
  response = {
    'message': 'Task deleted successfully'
  }

  return jsonify(response), 204

if __name__ == '__main__':
  app.run(debug=True)