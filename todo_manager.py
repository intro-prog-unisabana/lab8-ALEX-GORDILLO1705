"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""


def read_todo_file(file_path):
    """Reads tasks from a file. Returns a list of tasks."""
    try:
        with open (file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"archivo {file_path} no encontrado. Se creará un nuevo archivo al guardar tareas.")
        return []    
    raise NotImplementedError


def write_todo_file(file_path, tasks):
    """Writes tasks to a file, one per line."""
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    raise NotImplementedError
