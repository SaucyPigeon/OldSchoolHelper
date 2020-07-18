# Old School Helper
# gear.py
# Encapsulates gear record

from utils import input_bool

class gear(dict):
    def __init__(self):
        dict.__init__(self)


    def __len__(self):
        return len(self.slot_dict.items())


    def clear(self):
        self.slot_dict.clear()


    def items(self):
        return self.slot_dict.items()

    def input_gear(self, monster):
        if len(self):
            print("Gear already exists for this task (" + monster + ").")
            if not input_bool("Are you sure that you want to overwrite existing gear?"):
                return
            else:
                self.slot_dict.clear()
        
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
            self.slot_dict[slot] = i
            print("Added " + i + " to " + slot + " slot.")
            
        print("Gear successfully added for " + monster + ".")
