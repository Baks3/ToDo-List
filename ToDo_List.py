todos = []

while True:
    user_input = input("Type add, show , edit or exit")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter todo")
            todos.append(todo)
        case "show":
            for index,todo in enumerate(todos):
                todo = todo.title()
                print(f"{index+1} - {todo}")
        case "edit":
            number = int(input("Number of todo to edit: "))
            number = number -1
            new_todo = input("Enter todo: ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Enter number of todo to complete"))
            todos.pop(number - 1)
        case "exit":
            break

print("Bye!")