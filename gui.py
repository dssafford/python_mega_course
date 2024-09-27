import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do')
add_button = sg.Button('Add')

# For layout each item in list in square brackets is a seperat row in window
window = sg.Window("My To-Do App", layout=[[label], [input_box,add_button]])
window.read()
window.close()

