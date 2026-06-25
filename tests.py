# by Riinno, 2026

# --------------------------------------------------------------------------
# Importacao e variaveis base

import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

# --------------------------------------------------------------------------
# Teste para rota de Create do CRUD

def test_create_task():
  new_task_data = {
    "title": "Nova tarefa",
    "description": "Tarefa de teste"
  }

  # envia um "post" com new_task_data para o servidor de tasks
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  
  # testa se o código da resposta do servidor é 200 OK
  assert response.status_code == 200

  # testa se tem as chaves "message" e "id" na resposta do servidor
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  
  tasks.append(response_json["id"])

# --------------------------------------------------------------------------
# Teste para rota de Read geral do CRUD

def test_read_tasks():
  # envia um "get" ao servidor de tasks,
  # requisitando a lista de tasks
  response = requests.get(f"{BASE_URL}/tasks")

  # testa se o código da resposta do servidor é 200 OK
  assert response.status_code == 200

  # testa se tem as chaves "tasks" e "total_tasks" na resposta do servidor
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json


# Teste para rota de Read especifica do CRUD

def test_read_specific_task():
  if tasks:
    task_id = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    
    # testa se o código da resposta do servidor é 200 OK
    assert response.status_code == 200
  
    # testa se o valor da chave "id" da resposta do servidor 
    # é igual ao id salvo localmente pelo script de testes
    response_json = response.json()
    assert task_id == response_json["id"]

# --------------------------------------------------------------------------
# Teste para rota de Update do CRUD

def test_update_task():
  if tasks:
    task_id = tasks[0]
    
    task_data = {
      "title": "Nova tarefa atualizada",
      "description": "Tarefa de teste atualizada",
      "completed": True
    }

    # testa se o código da resposta do servidor ao PUT é 200 OK
    response_put = requests.put(f"{BASE_URL}/tasks/{task_id}", json=task_data)
    assert response_put.status_code == 200

    # testa se tem a chave "message" na resposta do servidor ao PUT
    response_put_json = response_put.json()
    assert "message" in response_put_json


    # testa se o código da resposta do servidor ao GET é 200 OK
    response_get = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response_get.status_code == 200
    
    # testa se a task retornada pelo servido (em resposta ao GET)
    # é igual a task atualizada
    response_get_json = response_get.json()
    assert response_get_json["title"] == task_data["title"]
    assert response_get_json["description"] == task_data["description"]
    assert response_get_json["completed"] == task_data["completed"]

# --------------------------------------------------------------------------
# Teste para rota de Delete do CRUD

def test_delete_task():
  if tasks:
    task_id = tasks[0]
    response_get = requests.get(f"{BASE_URL}/tasks")
    # salva a quantidade de tasks antes de deletar
    tasks_before_delete = response_get.json()["total_tasks"]

    # testa se o código da resposta do servidor ao DELETE é 200 OK
    response_delete = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response_delete.status_code == 200
    
    response_get = requests.get(f"{BASE_URL}/tasks")
    # salva a quantidade de tasks depois de deletar
    tasks_after_delete = response_get.json()["total_tasks"]

    assert tasks_before_delete == tasks_after_delete + 1

# --------------------------------------------------------------------------