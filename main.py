# Old School Helper
# main.py
# - User can define slayer monsters
# - User can define gear for a given slayer monster
# - User can select a defined slayer monster to display gear required
# - User can save this data (slayer monsters, gear) and load for later use.

import osh_io

import json
  
  
# Utility functions

def quote(value):
	return "\"" + value + "\""

def input_bool(message):
	print(message)
	value = input()
	if value == "yes":
		return True
	elif value == "no":
		return False
	else:
		print(quote(value) + " is not a valid input.")
		return input_bool(message)

def concat(*values):
	result = ""
	for value in values:
		result = result + str(value)
	return result
		
# Business logic

possible_slots = [
	"helmet", "necklace", "ammo", "cape", "torso", "legs",
	"gloves", "boots", "ring", "weapon", "offhand"
]

file_path = "data.json"

# Represents a data record for a monster and corresponding gear.
class slayer_record:
	def __init__(self, monster, gear):
		self.monster = monster
		self.gear = gear

class slayer_gear:
	# Possible slots:
	# - helmet
	# - neck
	# - ammo
	# - cape
	# - torso
	# - legs
	# - gloves
	# - boots
	# - ring
	# - weapon (class)
	# - offhand
	
	# Param: data is a dictionary. Keys represents the slot, values represent
	# the equipment.
	def __init__(self, data):
		counter = 0
		
		slot_len = len(possible_slots)
		data_len = len(data.items())

		if not "weapon" in data:
			raise ValueError("Data param must have weapon slot.")
		
		data_two_handed = data["weapon"].two_handed
		if data_two_handed:
			slot_len = slot_len - 1
	
		
		if slot_len != data_len:
			raise ValueError(concat("Data param must be same length as possible slots (current=", data_len, ", expected=", slot_len, ")"))
	    
		for possible_slot in possible_slots:
			if data_two_handed and possible_slot == "offhand":
				continue
			if not possible_slot in data:
				raise ValueError("Data param must contain key: " + possible_slot)
		self.data=data
		
class weapon_record:
	def __init__(self, name, two_handed):
		self.name = name
		self.two_handed = two_handed

	def __str__(self):
		return self.name

records = []

def add_slayer_monster():
	print("Defining new slayer monster.")
	print("Enter slayer monster name: ")
	name = input()
	
	record = slayer_record(name, None)
	records.append(record)
	
	print("Slayer monster " + name + " added.")

def get_record_by_monster():
	end = False
	
	while not end:
		print("Enter monster name: ")
		monster = input()
		for record in records:
			if record.monster == monster:
				return record
		print("Monster with that name does not exist on record.")
		end = not input_bool("Try again? ")
	
	return None

def add_gear():
	if len(records) == 0:
		print("Cannot add gear for slayer monster.")
		print("Make sure that a slayer monster has been defined.")
		return

	print("Defining gear for slayer monster.")
	
	record = get_record_by_monster()
	if record is None:
		print("Cannot add gear if no record is selected.")
		return
		
	monster = record.monster
		
	gear = {}
	two_handed = False
	
	for possible_slot in possible_slots:
		print("Enter item for " + possible_slot + " slot: ")
		item_name = input()
		if possible_slot == "weapon":
			two_handed = not input_bool("Is the weapon one-handed? ")
			weapon = weapon_record(item_name, two_handed)
			gear[possible_slot] = weapon
		elif possible_slot == "offhand" and two_handed:
			continue
		else:
			gear[possible_slot] = item_name

	record.gear = slayer_gear(gear)

def show_monster_gear():
	if len(records) == 0:
		print("Cannot show gear for slayer monster.")
		print("Make sure that a slayer monster has been defined.")
		return

	print("Showing gear for slayer monster.")
	
	record = get_record_by_monster()
	if record is None:
		print("Cannot show gear if no record is selected.")
		return

	if record.gear is None:
		print("No gear has been defined for record.")
		return
		
	for slot, item in record.gear.data.items():
		print(concat(slot, " slot: ", item))
	
	
def exit_program():
	print("Saving data.")
	
	with open(file_path, "w", encoding="utf-8") as f:
		json.dump(records.data, f, ensure_ascii=False, indent=4)

possible_slots = [
	"helmet", "necklace", "ammo", "cape", "torso", "legs",
	"gloves", "boots", "ring", "weapon", "offhand"
]


def debug_steel_dragon():

    print("Adding steel dragon record.")

    gear_dict = {
	"helmet": "foo",
	"necklace": "foo",
	"ammo": "foo",
	"cape": "foo",
	"torso": "foo",
	"legs": "foo",
	"gloves": "foo",
	"boots": "foo",
	"ring": "foo",
	"weapon": weapon_record("foo", False),
	"offhand": "foo"
    }
    gear = slayer_gear(gear_dict)
    record = slayer_record("steel dragon", gear)
    records.append(record)
    
    print("Record added.")
    
    

print("Welcome to Old School Helper")
print("****************************")

if osh_io.path_exists(file_path):
        print(concat("Loading data from file ", file_path))
        with open(file_path) as f:
                records = json.load(f)
        print("Data successfully loaded.")

while True:
	print("Available commands:")

	options = {
		"add slayer monster": add_slayer_monster,
		"add gear": add_gear,
		"show monster gear": show_monster_gear,
		"exit": exit_program,
		"DEBUG steel dragon": debug_steel_dragon
	}

	for key, value in options.items():
		if key.startswith("DEBUG"):
			continue
		print("\t* " + key)

	print("\n")
	print("Enter command: ")
	option = input()

	if not option in options:
		print("That command does not exist.")
		print("Please try again.")
		continue

	func = options[option]
	func()
