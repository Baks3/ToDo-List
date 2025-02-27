from colorama import Fore, Style

def read_todos():
    with open('todos.txt', 'r') as file:
        return file.readlines()

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

def show_todos(todos):
    print(Fore.YELLOW + "\nYour Todos:" + Style.RESET_ALL)
    if not todos:
        print("No todos yet! Add one ✅")
    for index, todo in enumerate(todos):
        print(f"{Fore.GREEN}{index + 1} - {todo.strip()}{Style.RESET_ALL}")
    print("\n")


