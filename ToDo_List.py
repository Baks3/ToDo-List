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


while True:
    todos = read_todos()

    user_input = input("Type add, show, edit, complete, or exit: ").strip()

    match user_input:
        case "add":
            todo = input("Enter todo: ").strip()
            if todo:
                todos.append(todo + "\n")
                write_todos(todos)
            else:
                print("Todo cannot be empty.")

        case "show":
            show_todos(todos)

        case "edit":
            try:
                number = int(input("Number of todo to edit: "))
                if 0 < number <= len(todos):
                    new_todo = input("Enter new todo: ").strip()
                    if new_todo:
                        todos[number - 1] = new_todo + "\n"
                        write_todos(todos)
                    else:
                        print("New todo cannot be empty.")
                else:
                    print("Invalid todo number.")
            except ValueError:
                print("Please enter a valid number.")

        case "complete":
            try:
                number = int(input("Enter number of todo to complete: "))
                if 0 < number <= len(todos):
                    todos.pop(number - 1)
                    write_todos(todos)
                else:
                    print("Invalid todo number.")
            except ValueError:
                print("Please enter a valid number.")

        case "exit":
            print("Bye!")
            break

        case _:
            print("Invalid input. Please try again.")
