import textwrap                                         # import textwrap module (to help with long description indentation problems)
from Rooms import Rooms

Vowels = "a", "i", "o", "u", "e"                        # create a tuple (type of list that is unchangeable) called Vowels
                                                        # tuple is a special kind of list and doesn't need [] (can use () but not necessary)
Words_without_articles = [ "gold", "water" ]            # create a list of words that don't use articles, to be used later with item listing


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
def join_neatly(list_of_items):                             # define function join_neatly that needs parameter list_of_items
    list_of_items = list(list_of_items)                     # Force the list_of_items to be a real list! (instead of dict_keys list)

   # if (len(list_of_items) == 0):                          # check if length (len) of the list list_of_items is 0
   #     return "nothing"
    
    if (len(list_of_items) == 1):                           # check if length (len) of the list list_of_items is just 1
        return list_of_items[0]                             # if so, return the first (and only) item on list (index 0)
    last_item = list_of_items.pop()                         # last_item is set to be the last item on list_of_items (.pop method)
    return ", ".join(list_of_items) + " and " + last_item   # return list_of_items joined with , in between, + and with last item

def describe_room(room_id):                                 # define describe_room function that needs parameter room_id (which is created/defined here also)
    room = Rooms[room_id]                                   # set 'room' to be a requested value (requesting done with [], takes a key returns a value) from dictionary Rooms
    print("\n=== " + room["name"] + " ===\n")               # prints room name --> request value of key 'name' from room (which points to Rooms) ( === The red room === )
    print(textwrap.dedent(room["description"]))             # print value of key 'description' (room <-- room_id <-- the parameter currently used by describe_room)

    print("\nThere are exits to the " + join_neatly(room["exits"].keys()) + ".")    # print values to keys to 'exits' in 'room'
                                                                                    # .keys() is built-in dictionary method, 
                                                                                    # here targeting the VALUE (which is a dictionary) of KEY 'room["exits"]'
                                                                                    # .keys() returns a list of dict_keys format, which is not a normal list!
                                                                                    # note, join_neatly forces dict_keys list to become normal list
                                                                                    # finally you get "There are exits to south and north" for this example



    # if (len(room["items"]) != 0):                                                             # if room has items (a longer version than the one below)
    if (room["items"]):                                                                         # if list has things in it, it returns value 'True' and the loop runs
        print("\nYou see " + join_neatly( map(add_an_article, room["items"]) ) + " here.")      # print items in room using join_neatly and map
                                                                                                # map() executes a function on iterables, in this case
                                                                                                # the function is add_an_article
                                                                                                # and the iterable is room["items"]
                                                                                                # --> [] searches for they key 'items' in 'room,
                                                                                                # and returns its value which is the list of items


