todos = []

while True:
    user_input = input("Type add, show , edit or exit")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter todo")
            todos.append(todo)

        case "show":
            for todo in todos:
                todo = todo.title()
                print(todo)
        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number -1
            new_todo = input("Enter todo: ")
            todos[number] = new_todo

        case "exit":
            break

print("Bye!")