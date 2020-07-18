# Old School Helper
# main.py
# Allows user to add slayer tasks.
# Slayer tasks have preferred gear setups saved as well.

import task_manager
from utils import quote

class command:
    def __init__(self, name, desc, func):
        self.name = name
        self.desc = desc
        self.func = func

    def __str__(self):
        return self.name + ": " + self.desc

def get_command_with_name(commands, name):
    for command in commands:
        if command.name == name:
            return command
    return None



def entry():
    print(quote("Old School Helper", "==="))
    print("Available commands:")

    tasks = task_manager.task_manager()
    
    commands = [
        command("add task", "add new task", tasks.add_new_task),
        command("select", "select task", tasks.select_task),
        command("deselect", "deselect task", tasks.deselect_task),
        command("delete", "delete selected task", tasks.delete_task),
        command("add gear", "add gear to task", tasks.add_gear_to_task),
        command("remove gear", "remove gear from task", tasks.remove_gear_from_task),
        command("display gear", "display task gear", tasks.display_task_gear),
        command("help", "display available commands", None)
        ]

    for c in commands:
        print(str(c))

    while True:
        print("Enter command:")
        command_input = input()
        selected_command = get_command_with_name(commands, command_input)
        if selected_command is None:
            print("That is not a valid command. Please try again.")
            continue
        if selected_command.name == "help":
            for c in commands:
                print(str(c))
            continue
        
        selected_command.func()

entry()
