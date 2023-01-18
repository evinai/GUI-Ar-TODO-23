import functions
import PySimpleGUI as sgu

label = sgu.Text("Type in a to-do")
input_box = sgu.InputText(tooltip="Enter a to-do here")
add_button = sgu.Button("Add", tooltip="Add a to-do")

window = sgu.Window(title="Todo List", layout=[[label, input_box, add_button]]) # goes inside another square bracket. This is one row. if 2 lists, 2 rows.
window.read()
window.close()