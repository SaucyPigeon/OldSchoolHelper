# Old School Helper
# utils.py
# Contains various non-business logic utility functions

# Print a message and return a boolean user input (True/False).
# Input must be either "y" or "n".
def input_bool(message):
    print(message)
    i = input()
    if i == "y":
        return True
    if i == "n":
        return False
    print("Invalid input: has to be either \"y\" or \"n\". Please try again.")
    return input_bool(message)


# Prompt the user with "Are you sure that you want to ___?".
def confirm_prompt(action):
    return input_bool("Are you sure that you want to " + action + "?")

# Print a message and return a string user input.
def prompt(message):
    print(message)
    i = input()
    return i

# Return the message with the quote string added to both sides.
def quote(message, quote_s):
    return quote_s + message + quote_s
    



