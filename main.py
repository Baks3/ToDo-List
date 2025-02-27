import ToDo_Functions as TDF
from colorama import Fore, Style



def main():
    print(Fore.CYAN + "Welcome to your Awesome Todo List!" + Style.RESET_ALL)
    
    while True:
        todos = TDF.read_todos()

        user_input = input("Type add, show, edit, complete, or exit: ").strip()

        match user_input:
            case "add":
                todo = input("Enter todo: ").strip()
                if todo:
                    todos.append(todo + "\n")
                    TDF.write_todos(todos)
                else:
                    print("Todo cannot be empty.")

            case "show":
                TDF.show_todos(todos)

            case "edit":
                try:
                    number = int(input("Number of todo to edit: "))
                    if 0 < number <= len(todos):
                        new_todo = input("Enter new todo: ").strip()
                        if new_todo:
                            todos[number - 1] = new_todo + "\n"
                            TDF.write_todos(todos)
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
                        TDF.write_todos(todos)
                    else:
                        print("Invalid todo number.")
                except ValueError:
                    print("Please enter a valid number.")

            case "exit":
                print("Bye!")
                break

            case _:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()