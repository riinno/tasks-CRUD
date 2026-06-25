# by Riinno, 2026

# -------------------------------------------------------------------
# Importacao e variaveis base

import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

# -------------------------------------------------------------------
# Teste para rota de Create do CRUD

def test_create_task():
  new_task_data = {
    "title": "Nova tarefa",
    "description": "Tarefa de teste"
  }

  # testa se o código da resposta do servidor é 200 OK
  response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
  assert response.status_code == 200

  # testa se tem as chaves "message" e "id" na resposta do servidor
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  
  tasks.append(response_json["id"])

# -------------------------------------------------------------------

