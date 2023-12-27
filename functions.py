FILEPATH = "todos.txt"

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath="todos.txt" ):
    """ write a to-item in text files"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
