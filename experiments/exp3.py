prompt = "Type add, show or exit: "

todos = []

while True:
    user_action = input(prompt)
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case _: #whatever
            print("Invalid input")

print("bye bye")
