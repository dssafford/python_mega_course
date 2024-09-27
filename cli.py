from functions import get_todos, write_todos



while True:
    user_action = input('Type (a)dd, (e)dit, (s)how, (c)omplete or e(x)it: ')
    user_action = user_action.strip()

    if (user_action.startswith('add')): # | (user_action[0] == 'a'):
        # todo = input('Add a todo: ') + '\n'
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')
        # file = open('files/todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos)

    elif (user_action.startswith('show')) | (user_action[0] == 's'):
        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index+1}-{item}')

    elif (user_action.startswith('edit')) | (user_action[0] == 'e'):
        # number = int(input('Enter the number of the todo to edit: '))
        try:
            number = int(user_action[5:])-1

            todos = get_todos()

            todos[number] = input('Enter the new value: ') + '\n'

            write_todos(todos)

        except ValueError:
            print('Your command is not valid - ValueError')
            continue

    elif ('exit' in user_action) | (user_action[0] == 'x'):
        break

    elif (user_action.startswith('complete')) | (user_action[0] == 'c'):
        # number = int(input('Enter the number of the todo to complete: '))
        try:
            number = int(user_action[9:])
            print('number = ' + str(number))
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} has been removed"
            print(message)

        except IndexError:
            print('IndexError - There is no item with that number')
            continue

    else:
        print('Invalid input, try again')


print("Bye")



