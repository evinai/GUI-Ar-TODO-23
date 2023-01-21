import functions
import PySimpleGUI as sgu
import time
import os


if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", "w") as file_local:
        pass # Create the file if it doesn't exist.

# THEME
sgu.theme("DarkAmber") # Add a theme


# LABELS
clock = sgu.Text("", key='clock')
label = sgu.Text("Type in a to-do")

# INPUT BOXES
input_box = sgu.InputText(tooltip="Enter a to-do here", key="todo")
list_box = sgu.Listbox(values=functions.get_todos(), size=(30, 10),
                       enable_events=True, key="todos")

# BUTTONS
add_button = sgu.Button("Add", tooltip="Add a to-do", size=10)
edit_button = sgu.Button("Edit", tooltip="Edit a to-do")
complete_button = sgu.Button("Complete", tooltip="Complete a to-do")
exit_button = sgu.Button("Exit", tooltip="Exit the app")

# Layout
layouts = [[clock],
           [label],
           [input_box, add_button],
           [list_box, edit_button, complete_button],
           [exit_button]]

window = sgu.Window(title="My ToDo App", layout=layouts, font=("Helvetica", 18))

while True:
    event, values = window.read(timeout=300)
    window["clock"].update(value=time.strftime("%b %d, %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values["todo"])
    match event:
        case "Add":
            todos = functions.get_todos()  # get the todos
            print(4, todos)
            new_todo = values["todo"] + "\n"  # get the new to do
            todos.append(new_todo)  # add the new to do to the todos
            print(5, todos)
            functions.write_todos(todos)  # write the todos to the file
            window["todos"].update(values=todos)  # update the list box
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]  # get the selected to do. [0] because it is a list
                new_todo = values["todo"].strip().replace('\n', '')  # get the new to do
                print(6, new_todo)

                todos = functions.get_todos()  # get the todos
                index = todos.index(todo_to_edit)  # get the index of the to do to edit
                todos[index] = new_todo + "\n" # replace the to do to edit with the new to do
                functions.write_todos(todos)  # write the todos to the file
                window["todos"].update(values=todos)  # update the list box in real time
            except IndexError:
                sgu.popup("Please select a to-do to edit", font="Helvetica 18")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0] # get the selected to do. [0] because it is a list
                todos = functions.get_todos()  # get the todos  # get the index of the to do to complete
                todos.remove(todo_to_complete)  # remove the to do to complete
                functions.write_todos(todos)  # write the todos to the file
                window["todos"].update(values=todos)  # update the list box in real time
                window["todo"].update(value="")  # clear the input box
            except IndexError:
                sgu.popup("Please select a to-do to complete", font="Helvetica 18")
        case "Exit":
            exit()  # or break
        case 'todos':
            window["todo"].update(value=values["todos"][0])  # update the input box in real time automatically. [0] because it is a list
        case sgu.WIN_CLOSED:
            exit()  # or break

window.close()
