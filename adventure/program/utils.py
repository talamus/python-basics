import textwrap                                             # Import textwrap module (to help with long description indentation problems)
from data.rooms import Rooms
from data.items import *
from data.player import *

def join_neatly(list_of_items: list[str]) -> str:
    """ Join a list of items neatly for output. """

    list_of_items = list(list_of_items)                     # Force the "list_of_items" to be a real list! (instead of dict_keys list)

    if (len(list_of_items) == 1):                           # Check if length (len) of the list list_of_items is just 1
        return list_of_items[0]                             # If so, return the first (and only) item on list (index 0)
    last_item = list_of_items.pop()                         # Last_item is set to be the last item on list_of_items (.pop() method)
    return ", ".join(map(str, list_of_items)) + " and " + str(last_item)   # Return list_of_items joined with , in between, + and with last item


def describe_room(room_id: str):
    """ Print description of a room identified by room_id. """

    room = Rooms[room_id]                                   # Set 'room' to be a requested value (requesting done with [], takes a key returns a value) from dictionary Rooms
    print("\n=== " + room["name"] + " ===\n")               # Prints room name --> request value of key 'name' from room (which points to Rooms) ( === The red room === )
    print(textwrap.dedent(room["description"]))             # Print value of key 'description' (room <-- room_id <-- the parameter currently used by describe_room)

    if room["exits"]:
        exits = list(room["exits"])
        hidden_exits = []
        for exit in exits:
            if "hidden" in exit:
                exit_parts = exit.split()
                hidden_exits.append(exit_parts[1])
                exits.remove(exit)

        if not exits:
            print("\nYou see no way out!")
        elif len(exits) == 1:
            print("\nThere is an exit to the " + join_neatly(exits) + ".")
        else:
            print("\nThere are exits to the " + join_neatly(exits) + ".")

        if ring in player.inventory and ring.wearable.worn:
            if len(hidden_exits) != 0:
                if len(hidden_exits) == 1:
                    print("You see a glowing exit to the " + join_neatly(hidden_exits) + ".")
                else:
                    print("You see glowing exits to the " + join_neatly(hidden_exits) + ".")



        #print("\nThere are exits to the " + join_neatly(room["exits"].keys()) + ".")    # Print values to keys to 'exits' in 'room'
                                                                                    # .keys() is built-in dictionary method,
                                                                                    # here targeting the VALUE (which is a dictionary) of KEY 'room["exits"]'
                                                                                    # .keys() returns a list of dict_keys format, which is not a normal list!
                                                                                    # note, join_neatly forces dict_keys list to become normal list
                                                                                    # finally you get "There are exits to south and north" for this example

    if (room["items"]):                                                             # If list has things in it, it returns value 'True' and the loop runs
        print("\nYou see " + join_neatly(map(str, room["items"])) + " here.")       # Print items in room using join_neatly
                                                                                    # [] searches for they key 'items' in 'room,
                                                                                    # and returns its value which is the list of items

    if (room["fixtures"]):                                                          # If list has things in it, it returns value 'True' and the loop runs
        for fixture in room["fixtures"]:
            if not fixture.hidden.hidden:
                print("\nYou see " + str(fixture) + " here.")


def list_index(short_list: str | list[str], long_list: list[str]) -> int:
    """
        Return the first occurence where the short_list is found at long_list.
        Return None if short_list not found.
    """
    if isinstance(short_list, str):                                                 # If short_list is string:
        short_list = short_list.split()                                             # Split it into list (by whitespace)

    # Now `short_list` is list of strings, f.ex. ["of"] or ["filled", "with"]
    # `long_list` is the full list of strings, f.ex. ["a", "book", "of", "spells"]

    if not short_list[0] in long_list:                                              # If the first item of short_list is not found in long_list
        return None                                                                 # none of it will be. Return None. (Meaning: There's no splitter in long_list.)

    index_list = []                                                                 # (<-- list of possible index locations for short_list)
    for index, item in enumerate(long_list):                                        # For every item in the long_list:
        if item == short_list[0]:                                                   # Compare it to the first item in short_list
            index_list.append(index)                                                # If True: add the location to index_list

    for index in index_list:                                                        # For every possible index location:
        if long_list[index : index + len(short_list)] == short_list:                # Check if the full short_list is found
            return index                                                            # If True: return this index location as the answer

    return None                                                                     # Otherwise: short_list was not found, return None


def list_index_2(short_list: str | list[str], long_list: list[str]) -> int:
    """
        Return the first occurence where the short_list is found at long_list.
        Return None if short_list not found.
    """
    if isinstance(short_list, str):                                                 # If short_list is string:
        short_list = short_list.split()                                             # Split it into list (by whitespace)

    # Now `short_list` is list of strings, f.ex. ["of"] or ["filled", "with"]
    # `long_list` is the full list of strings, f.ex. ["a", "book", "of", "spells"]

    index = 0
    try:
        while True:
            index = long_list.index(short_list[0], index)
            if long_list[index : index + len(short_list)] == short_list:            # Check if the full short_list is found
                return index                                                        # If True: return this index location as the answer
            index += 1
    except ValueError:
        return None


def list_split(splitter: str | list[str], long_list: list[str]) -> tuple[list[str], list[str]]:
    """
        Split long_list (a list of strings).
        Splitter can be a string or a list of strings.
    """
    if isinstance(splitter, str):                                                   # If splitter is string:
        splitter = splitter.split()                                                 # Split it into list (by whitespace)
    else:                                                                           # Otherwise:
        splitter = list(splitter)                                                   # Force into a list (because it will be spliced later)

    # Now `splitter` is list of strings, f.ex. ["of"] or ["filled", "width"]
    # `long_list` is the full list of strings, f.ex. ["a", "book", "of", "spells"]

    index = list_index(splitter, long_list)                                         # Try to find the location (index number) of splitter from the long_list
    if index != None:                                                               # If splitter is found in long_list
        return (long_list[:index], long_list[index + len(splitter):])               # Return tuple containing two lists: long_list items before and after splitter
    else:                                                                           # Else splitter was not found
        return (long_list, [])                                                      # Return full long_list and an empty list

