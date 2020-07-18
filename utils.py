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



# Return the message with the quote string added to both sides.
def quote(message, quote_s):
    return quote_s + message + quote_s
    



