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