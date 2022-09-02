import textwrap                                             # Import textwrap module (to help with long description indentation problems)
from Rooms import Rooms                                     # Import dictionary Rooms from file Rooms.py
from Item import Item



# Join a list of items neatly for output:
def join_neatly(list_of_items):                             # Define function "join_neatly" that needs parameter "list_of_items"
    list_of_items = list(list_of_items)                     # Force the "list_of_items" to be a real list! (instead of dict_keys list)

    if (len(list_of_items) == 1):                           # Check if length (len) of the list list_of_items is just 1
        return list_of_items[0]                             # If so, return the first (and only) item on list (index 0)
    last_item = list_of_items.pop()                         # Last_item is set to be the last item on list_of_items (.pop() method)
    return ", ".join(map(str, list_of_items)) + " and " + str(last_item)   # Return list_of_items joined with , in between, + and with last item


def describe_room(room_id):                                 # Define describe_room function that needs parameter room_id (which is created/defined here also)
    room = Rooms[room_id]                                   # Set 'room' to be a requested value (requesting done with [], takes a key returns a value) from dictionary Rooms
    print("\n=== " + room["name"] + " ===\n")               # Prints room name --> request value of key 'name' from room (which points to Rooms) ( === The red room === )
    print(textwrap.dedent(room["description"]))             # Print value of key 'description' (room <-- room_id <-- the parameter currently used by describe_room)

    print("\nThere are exits to the " + join_neatly(room["exits"].keys()) + ".")    # Print values to keys to 'exits' in 'room'
                                                                                    # .keys() is built-in dictionary method,
                                                                                    # here targeting the VALUE (which is a dictionary) of KEY 'room["exits"]'
                                                                                    # .keys() returns a list of dict_keys format, which is not a normal list!
                                                                                    # note, join_neatly forces dict_keys list to become normal list
                                                                                    # finally you get "There are exits to south and north" for this example

   
    if (room["items"]):                                                 # If list has things in it, it returns value 'True' and the loop runs
        print("\nYou see " + join_neatly(map(str, room["items"])) + " here.")     # Print items in room using join_neatly
                                                                        # [] searches for they key 'items' in 'room,
                                                                        # and returns its value which is the list of items




