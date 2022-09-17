import program.commands as command

def parse(input):

    match list(filter(lambda word : word not in ("a", "an", "the"), input.split())):
    # split command string and remove articles, before matching cases, output is list of strings

        case ["n"] | ["north"]:
            command.go("north")

        case ["e"] | ["east"]:
            command.go("east")

        case ["s"] | ["south"]:
            command.go("south")

        case ["w"] | ["west"]:
            command.go("west")

        case ["go", "to", direction] | ["go", direction]:
            command.go(direction)

        case ["look", "at", *item] | ["examine", *item] | ["ex", *item]:                # if you use *item, it will be a list (of strings), if just item, it will be a string
            command.examine(item)

        case ["l"] | ["look"] | ["look", "around"]:
            command.look_around()

        case ["take", *item] | ["get", *item]:
            command.take(item)

        case ["drop", *item]:
            command.drop(item)

        case ["wear", *item] | ["put", "on", *item] | ["put", *item, "on"]:
            command.wear(item)

        case ["remove", *item] | ["take", "off", *item] | ["take", *item, "off"]:
            command.remove(item)

        case ["i"] | ["inventory"] | ["check", "pockets"] | ["check", "pocket"]:
            command.inventory()

        case ["quit"]:
            print("\nQuitters!\n")
            quit()

        case other:
            print("Sorry, you can't do that yet.")