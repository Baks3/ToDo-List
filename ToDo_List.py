todos = []

while True:
    user_input = input("Type add, show or exit")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter todo")
            todos.append(todo)

        case "show":
            for todo in todos:
                todo = todo.title()
                print(todo)

        case "exit":
            break

print("Bye!")