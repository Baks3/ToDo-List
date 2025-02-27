import ToDo_Functions as TDF
from colorama import Fore, Style



def main():
    print(Fore.CYAN + "Welcome to your Awesome Todo List!" + Style.RESET_ALL)

    while True:
        todos = TDF.read_todos()

        user_input = input("\nType add 📝, show 👀, edit ✏️, complete ✅, or exit ❌: ").strip().lower()

        match user_input:
            case "add":
                todo = input("Enter todo: ").strip()
                if todo:
                    todos.append(todo + "\n")
                    TDF.write_todos(todos)
                else:
                    print(Fore.RED + "Todo cannot be empty!" + Style.RESET_ALL)

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
                        print(Fore.RED + "Invalid number." + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

            case "complete":
                try:
                    number = int(input("Enter number of todo to complete: "))
                    if 0 < number <= len(todos):
                        todos.pop(number - 1)
                        TDF.write_todos(todos)
                    else:
                        print(Fore.RED + "Invalid todo number." + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)

            case "exit":
                print(Fore.MAGENTA + "Bye! Come back soon!" + Style.RESET_ALL)
                break

            case _:
                print(Fore.RED + "Invalid option, try again!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()