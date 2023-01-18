FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """Function Objectives: Read and Return the todos from the designated file path."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Function Objectives: Write the todos to the designated file path."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)




if __name__ == "__main__":
    print(get_todos())
    # WE ONLY WANT TO SEE THIS CODE WHEN WE RUN THIS FILE DIRECTLY. NOT WHEN WE IMPORT IT.
    # If I run main.py, I dont want to see this code. I only want to see this code when I run functions.py directly.
    print("hello from functions")
