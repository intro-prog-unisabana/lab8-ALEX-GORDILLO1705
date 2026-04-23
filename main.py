"""Laboratorio 8 - CLI del gestor de tareas."""
# main.py
import sys
from todo_manager import read_todo_file, write_todo_file

try:
    # Validar argumentos mínimos
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    # Comando de ayuda
    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...

Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit(0)

    file_path = sys.argv[1]

    # Si solo pasa el archivo → salir silenciosamente
    if len(sys.argv) == 2:
        sys.exit(0)

    # Leer archivo una sola vez
    tasks = read_todo_file(file_path)

    i = 2
    file_modified = False

    while i < len(sys.argv):
        command = sys.argv[i]

        if command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)
            i += 1

        elif command == "add":
            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "add".')

            task = sys.argv[i + 1]
            tasks.append(task)
            print(f'Task "{task}" added.')
            file_modified = True
            i += 2

        elif command == "remove":
            if i + 1 >= len(sys.argv):
                raise IndexError('Task description required for "remove".')

            task = sys.argv[i + 1]

            try:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
                file_modified = True
            except ValueError:
                print(f'Task "{task}" not found.')

            i += 2

        else:
            raise ValueError("Command not found!")

    # Guardar solo una vez al final
    if file_modified or not tasks:
        write_todo_file(file_path, tasks)

except IndexError as e:
    print(e)
    sys.exit(0)

except ValueError as e:
    print(e)
    sys.exit(0)