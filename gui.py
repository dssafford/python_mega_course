import functions
import FreeSimpleGUI as sg

label = sg.Text('Type in a To-Do')
input_box = sg.InputText(tooltip='Enter a To-Do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete', key='complete')
exit_button = sg.Button('Exit', key='exit')

# For layout each item in list in square brackets is a seperat row in window
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box,add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font='Helvetica 20')

while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case sg.WIN_CLOSED:
            break

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            # refresh the list in the list box
            window['todos'].update(values=todos)

        case "complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "exit":
            break


window.close()

