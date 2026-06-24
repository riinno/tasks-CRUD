# by Riinno, 2026

# --------------------------------------------
# Importação de dependencias e variaveis base

from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id = 0

# ------------------------------------------------------------------------------
# Rota Create Task

@app.route("/tasks", methods=["POST"])
def create_task():
  global task_id
  data = request.get_json()
  
  new_task = Task(id=task_id, title=data["title"], description=data.get("description", ""))
  task_id += 1
  tasks.append(new_task)
  
  # teste printando as tasks
  # for task in tasks:
  #   print(f"{task.id}, {task.title}, {task.description}\n")
  
  return jsonify({"message": "Nova tarefa criada com sucesso"})

# ------------------------------------------------------------------------------
# Rota manual base

if __name__ == "__main__":
  app.run(debug=True)

# ------------------------------------------------------------------------------