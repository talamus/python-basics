Vowels = "a", "i", "o", "u", "e"

Rooms = {
    "red": {
        "name": "The red room",
        "description": "This room is red.",
        "exits": {
            "south": "green",
            "north": "wasteland"
        },
        "items": [ "sword", "shield", "apple" ]
    }
}

def add_an_article(item):
    first_letter = item[0]
    if (first_letter in Vowels):
        return "an " + item
    else:
        return "a " + item

def join_neatly(list_of_items):
    list_of_items = list(list_of_items) # Force the list_of_items to be a real list! 
    if (len(list_of_items) == 1):
        return list_of_items[0]
    last_item = list_of_items.pop()
    return ", ".join(list_of_items) + " and " + last_item 

def describe_room(room_id):
    room = Rooms[room_id]
    print("\n=== " + room["name"] + " ===")
    print(room["description"])
    print("There are exits to " + join_neatly(room["exits"].keys()) + ".")
    print("You see " + join_neatly( map(add_an_article, room["items"]) ) + " here.")

# The Main Program:
describe_room("red")
