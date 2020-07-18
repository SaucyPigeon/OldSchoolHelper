# Old School Helper
# task.py
# Plain old data type for task records.

from gear import gear
import json


class task(object):
    def __init__(self, monster: str):
        self.monster = monster
        self.gear = {}


    def __str__(self):
        return self.monster


    def input_gear(self):
        if len(self.gear):
            print("Gear already exists for this task (" + self.monster + ").")
            if not input_bool("Are you sure that you want to overwrite existing gear?"):
                return
            else:
                self.gear.clear()
        
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
                two_handed = input_bool("Is the weapon two_handed?")
            # Skip offhand slot if weapon is two-handed.
            if two_handed and slot == "offhand":
                continue
            print("Enter item for " + slot + " slot:")
            i = input()
            self.gear[slot] = i
            print("Added " + i + " to " + slot + " slot.")
            
        print("Gear successfully added for " + self.monster + ".")


