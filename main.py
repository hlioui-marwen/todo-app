#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("the time below:")
print("It is", now)
prompt = "Type add, show, complete, edit or exit: "

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
#            file = open("filesold/todos.txt", "r")
#            todos = file.readlines()
#            file.close()
# same as
        todos = functions.get_todos()

        todos.append(todo + "\n")

#            file = open("filesold/todos.txt", "w")
#            file.writelines(todos)
#            file.close()
        functions.write_todos(todos)

    elif user_action.startswith("show"):
#            file = open("filesold/todos.txt", "r")
#            todos = file.readlines()
#            file.close()
        todos = functions.get_todos()

#            new_todos = []
#            for item in todos:
#                new_item = item.strip("\n")
#                new_todos.append(new_item)
#  or
#            new_todos = [item.strip("\n") for item in todos]
#  OR
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_toso = input("Enter new todo: ")
            todos[number] = new_toso + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Invalid input. Try again.")
            continue


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input. Try again.")

print("bye bye")
