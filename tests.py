import pytest
import requests

BASE_URL = 'http://localhost:5000'
tasks = []

def test_create_task():
  new_task_data = {
    'title': 'Test title',
    'description': 'Test description'
  }
  
  response = requests.post(f'{BASE_URL}/tasks', json=new_task_data)
  response_json = response.json()
  
  assert response.status_code == 201
  assert "message" in response_json
  assert "id" in response_json

  tasks.append(response_json['id'])

def test_get_tasks():
  response = requests.get(f"{BASE_URL}/tasks")
  response_json = response.json()

  assert response.status_code == 200
  assert "tasks" in response_json
  assert "total_tasks" in response_json

def test_get_task():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    response_json = response.json()

    assert response.status_code == 200
    assert task_id == response_json['id']
