# Old School Helper
# task_manager.py
# Encapsulates program state

from utils import input_bool

class task:
    def __init__(self, monster):
        self.monster = monster
        self.gear = None

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
        return None
    
    def deselect_task(self):
        return None
    
    def delete_task(self):
        return None
    
    def add_gear_to_task(self):
        if self.selected_task is None:
            print("No current task selected.")
            return
        if not self.selected_task.gear is None:
            print("Gear already exists for this task (" + self.selected_task.monster + ").")
            while True:
                if not input_bool("Are you sure that you want to overwrite existing gear?"):
                    return

        self.selected_task.gear = {}
        slots = [
            "helmet",
            "cape",
            "amulet",
            "ammo",
            "weapon",
            "offhand",
            "torso",
            "legs",
            "gloves",
            "boots",
            "ring"
            ]
        two_handed = False
        for slot in slots:
            if slot == "weapon":
                two_handed = input_bool("Is the weapon two-handed?")
            if two_handed and slot == "offhand":
                continue
            print("Enter item for " + slot + " slot:")
            i = input()
            self.selected_task.gear[slot] = i
        print("Gear successfully added for " + self.selected_task.monster + ".")
            
    
    def remove_gear_from_task(self):
        return None

    def display_task_gear(self):
        if self.selected_task is None:
            print("No current task selected.")
            return
        if self.selected_task.gear is None:
            print("Slayer task has no gear recorded.")
            return
        print("Gear for " + self.selected_task.monster + ":")
        for key, value in self.selected_task.gear.items():
            print(key + " slot: " + value)
