# Old School Helper
# task_manager.py
# Encapsulates program state

from utils import input_bool
from utils import confirm_prompt
from utils import prompt
from gear import gear

import json

class task(dict):
    def __init__(self, monster):
        dict.__init__(self, monster=monster, gear=gear())

    def __str__(self):
        return self.monster

class task_manager:
    def __init__(self):
        self.selected_task = None
        self.tasks = []


    def add_new_task(self):
        print("Enter task monster:")
        monster = input()
        t = task(monster)
        self.selected_task = t
        self.tasks.append(t)
        print(monster + " slayer task added and selected.")

    def select_task(self):
        # If no tasks recorded, cannot select task.
        if not len(self.tasks):
            print("There are no tasks currently recorded. Please add a task.")
            return
        # Print currently selected task
        if not self.selected_task is None:
            print("Currently selected task: " + str(self.selected_task))
            # If there are no other tasks to select, abort.
            if len(self.tasks) == 1:
                print("There is only one task on record and it is already selected.")
                return

       

        print("Available tasks:")

        for task in self.tasks:
            if task is self.selected_task:
                print(">>>" + str(task) + "<<<")
            else:
                print(str(task))


        while True:
            print("Enter task to select:")
            i = input()
            for task in self.tasks:
                if task.monster == i:
                    self.selected_task = task
                    print(str(task) + " selected.")
                    return
            print("That task does not exist. Please try again.")
        
        
    
    def deselect_task(self):
        if self.selected_task is None:
            print("No task is currently selected.")
        else:
            self.selected_task = None
            print("Task deselected.")
    
    def delete_task(self):
        if not len(self.tasks):
            print("There are no tasks currently recorded to delete.")
            return
        if self.selected_task is None:
            print("No task currently selected. Please select a task.")
            return

        print("The currently selected task is " + str(self.selected_task))
        if input_bool("Are you sure that you want to delete this task?"):
            t = self.selected_task
            self.tasks.remove(t)
            self.selected_task = None
            print("Task successfully removed.")
            
    
    def add_gear_to_task(self):
        if not len(self.tasks):
            print("There are no tasks recorded to which to add gear. Please add a task.")
            return
        if self.selected_task is None:
            print("No current task selected.")
            return

        self.selected_task.gear.input_gear(self.selected_task.monster)
            
    
    def remove_gear_from_task(self):
        if not len(self.tasks):
            print("There are no tasks from which to remove gear.")
            return
        if self.selected_task is None:
            print("No task is currently selected. Please select a task.")
            return
        if not len(self.selected_task.gear):
            print("Task already has no gear.")
            return
        if input_bool("Are you sure that you want to remove gear from " + str(self.selected_task) + "?"):
            self.selected_task.gear.clear()
            print("Gear removed from task.")
        else:
            print("Operation aborted.")

    def display_task_gear(self):
        if self.selected_task is None:
            print("No current task selected.")
            return
        if not len(self.selected_task.gear):
            print("Slayer task has no gear recorded.")
            return
        print("Gear for " + self.selected_task.monster + ":")
        for key, value in self.selected_task.gear.items():
            print(key + " slot: " + value)

    def rename_task_monster(self):
        if not len(self.tasks):
            print("No tasks are currently recorded. Please add a task.")
            return
        if self.selected_task is None:
            print("No current task selected.")
            return
        if confirm_prompt("rename the task's monster (" + self.selected_task.monster + ")"):
            new_monster = prompt("Enter new monster name:")
            old_monster = self.selected_task.monster
            self.selected_task.monster = new_monster
            print("Successfully renamed " + old_monster + " to " + new_monster + ".")
        else:
            print("Operation aborted.")

    def save(self):
        path = "data.json"
        with open(path, "w") as outfile:
            s = json.dumps(self.__dict__)
            outfile.write(s)
        print("Successfully saved to " + path)


    def load(self):
        return None
        
