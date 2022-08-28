import textwrap                                         # import textwrap module (to help with long description indentation problems)

Vowels = "a", "i", "o", "u", "e"                        # create a tuple (type of list that is unchangeable) called Vowels
                                                        # tuple is a special kind of list and doesn't need [] (can use () but not necessary)
Words_without_articles = [ "gold", "water" ]            # create a list of words that don't use articles, to be used later with item listing

Rooms = {                                               # create a variable called Rooms that contains a dictionary
    "red": {                                                # create a key called 'red' with value of everything in the dictionary that follows
        "name": "The Red room",                             # create a key: value pair
        "description": """\
            This room is red.
            The brick walls are old and crumbly, and the wall to the north has partially collapsed.
            To the south you see something green.""",
        "exits": {                                          # create a key 'exits' with value of the dictionary below
            "south": "green",                                   # create a key: value pair
            "north": "wasteland"                                # create a key: value pair
        },
        "items": [ "sword", "shield", "apple" ]             # create a key called 'items' with a value that is a list containing the items as strings
    },                                                      # end of dictionary 'red'

    "green": {
        "name": "The Green room",
        "description": """\
            This room is green.
            Every surface is covered with verdandtly green moss that is soft to the touch.""",
        "exits": {
            "north": "red",
            "east": "blue",
            "south": "purple"
        },
        "items": ["golden ring"]
    },

    "purple": {
        "name": "The Purple room",
        "description": """\
            This room is purple.
            Looks like something spewed purple slime all over the place, even the floor is slippery.""",
        "exits": {
            "north": "green"
        },
        "items": ["blue key", "empty bottle" ]

    },

    "blue": {
        "name": "The Blue room",
        "description": """\
            This room is blue.
            It's a large cave of bluish rock, with a bubbling natural fountain at the center of it.
            The water looks drinkable.
            Through an opening in the north wall, you see something glittering, and hear sounds of a large beast breathing as if asleep.
            """,
        "exits": {
            "west": "green",
            "north": "golden"
        },
        "items": []
    },

    "golden": {
        "name": "The Golden room",
        "description": """\
            This room is golden.
            The huge cave is filled with treasure, every inch of it bedecked with gems and gold.
            In the middle of the cave is a mountain of gold, atop which a sleeping dragon lies,
            as golden in color as the rest of the room.""",
        "exits": {
            "south": "blue"
        },
        
        "items": ["gold", "gold", "gold"]
    }
    

}                                                       # end of dictionary 'Rooms'



# check if first letter of item is vowel, then add article 'a' or 'an'
def add_an_article(item):
    if (item in Words_without_articles):
        return item

    first_letter = item[0]
    if (first_letter in Vowels):
        return "an " + item
    else:
        return "a " + item

# join a list of items neatly for output
def join_neatly(list_of_items):                         # define function join_neatly that needs parameter list_of_items
    list_of_items = list(list_of_items)                 # Force the list_of_items to be a real list! (instead of dict_keys list)
    
   # if (len(list_of_items) == 0):                       # check if length (len) of the list list_of_items is 0
   #     return "nothing"
    
    if (len(list_of_items) == 1):                       # check if length (len) of the list list_of_items is just 1
        return list_of_items[0]                         # if so, return the first (and only) item on list (index 0)
    last_item = list_of_items.pop()                     # last_item is set to be the last item on list_of_items (.pop method)
    return ", ".join(list_of_items) + " and " + last_item   # return list_of_items joined with , in between, + and with last item

def describe_room(room_id):                             # define describe_room function that needs parameter room_id (which is created/defined here also)
    room = Rooms[room_id]                               # set 'room' to be a requested value (requesting done with [], takes a key returns a value) from dictionary Rooms
    print("\n=== " + room["name"] + " ===\n")             # prints room name --> request value of key 'name' from room (which points to Rooms) ( === The red room === )
    print(textwrap.dedent(room["description"]))         # print value of key 'description' (room <-- room_id <-- the parameter currently used by describe_room)

    print("\nThere are exits to the " + join_neatly(room["exits"].keys()) + ".")  # print values to keys to 'exits' in 'room'
                                                                            # .keys() is built-in dictionary method, 
                                                                            # here targeting the VALUE (which is a dictionary) of KEY 'room["exits"]'
                                                                            # .keys() returns a list of dict_keys format, which is not a normal list!
                                                                            # note, join_neatly forces dict_keys list to become normal list
                                                                            # finally you get "There are exits to south and north" for this example



    # if (len(room["items"]) != 0):                                           # if room has items (a longer version than the one below)
    if (room["items"]):                                                       # if list has things in it, it returns value 'True' and the loop runs
        print("\nYou see " + join_neatly( map(add_an_article, room["items"]) ) + " here.")    # print items in room using join_neatly and map
                                                                                                # map() executes a function on iterables, in this case
                                                                                                # the function is add_an_article
                                                                                                # and the iterable is room["items"]
                                                                                                # --> [] searches for they key 'items' in 'room,
                                                                                                # and returns its value which is the list of items

# The Main Program:

player_location = "red"                                                  # starting location ("red" is found from the list of keys that is made automatically)
describe_room(player_location)                                           # use function describe_room with parameter 'player_location'

while (True):                                                            # just a trick to make this into a loop that runs constantly :D

    movement = input("\nWhere do you want to go? ")

    if (movement in Rooms[player_location]["exits"]):                     # check if the input string of 'movement' matches any values in exits of the room
        if (Rooms[player_location]["exits"][movement] == "wasteland"):
            print ("\nYou will not survive without water in the Wastleland.")
        else:
            player_location = Rooms[player_location]["exits"][movement]       # change player_location to new room (using string input of movement as key to find the value for new room)  
            describe_room(player_location)                                    # use function describe_room with parameter 'player_location'

    else:
        print("You can't go that way")
