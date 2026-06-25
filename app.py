# by Riinno, 2026

# ----------------------------------------------------------------------------------
# Importação de dependencias e variaveis base

from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id = 0

# ----------------------------------------------------------------------------------
# Rota Create Task

@app.route("/tasks", methods=["POST"])
def create_task():
  global task_id, total_tasks
  data = request.get_json()
  
  new_task = Task(id=task_id, title=data["title"], description=data["description"])
  task_id += 1
  tasks.append(new_task)
  
  # teste printando as tasks
  for task in tasks:
    print(f"{task.id}, {task.title}, {task.description}\n")
  
  return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

# ----------------------------------------------------------------------------------
# Rota Read Task

@app.route("/tasks", methods=["GET"])
def read_tasks():
  tasks_dictionary = [task.to_dictionary() for task in tasks]

  output = {
    "tasks": tasks_dictionary,
    "total_tasks": len(tasks_dictionary)
  }

  return jsonify(output)

# Rota Read Task para task com id especifico

@app.route("/tasks/<int:id>", methods=["GET"])
def read_specific_task(id):
  for task in tasks:
    if task.id == id:
      return jsonify(task.to_dictionary())

  return jsonify({"message": "Não existe tarefa com esse id"}), 404

# ----------------------------------------------------------------------------------
# Rota Update Tasks

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
  data = request.get_json()

  for task in tasks:
    if task.id == id:
      task.title = data["title"]
      task.description = data["description"]
      task.completed = data["completed"]

      return jsonify({"message": "Tarefa atualizada com sucesso"})
    
  return jsonify({"message": "Não existe tarefa com esse id"}), 404

# ----------------------------------------------------------------------------------
# Rota Delete Tasks

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
  for task in tasks:
    if task.id == id:
      tasks.remove(task)
      
      return jsonify({"message": "Tarefa deletada com sucesso"})
    
  return jsonify({"message": "Não existe tarefa com esse id"}), 404

# ----------------------------------------------------------------------------------
# Rota manual base

if __name__ == "__main__":
  app.run(debug=True)

# ----------------------------------------------------------------------------------