def read_todos():
    with open('todos.txt', 'r') as file:
        return file.readlines()

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

def show_todos(todos):
    if todos:
        for index, todo in enumerate(todos):
            print(f"{index + 1} - {todo.strip().title()}")
    else:
        print("No todos to show!")


