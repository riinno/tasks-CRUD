# by Riinno, 2026

# ---------------------------------------------------------------------
# Inicializa os valores do objeto tarefa

class Task:
  def __init__(self, id, title, description, completed=False) -> None:
    self.id = id
    self.title = title
    self.description = description
    self.completed = completed

# ---------------------------------------------------------------------
# Retorna a tarefa (objeto) em formato de dicionario

  def to_dictionary(self):
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "completed": self.completed
    }
  
# ---------------------------------------------------------------------