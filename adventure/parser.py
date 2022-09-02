import Commands



def parse(command):

    match list(filter(lambda word : word not in ("a", "an", "the"), command.split())):
    # split command string and remove articles, before matching cases, output is list of strings

        case ["n"] | ["north"]:
            Commands.go("north")
        
        case ["e"] | ["east"]:
            Commands.go("east")

        case ["s"] | ["south"]:
            Commands.go("south")
        
        case ["w"] | ["west"]:
            Commands.go("west")

        case ["go", "to", direction] | ["go", direction]:
            Commands.go(direction)
       
        case ["look", "at", *item] | ["examine", *item]:                # if you use *item, it will be a list (of strings), if just item, it will be a string
            Commands.examine(item)

        case ["l"] | ["look"] | ["look", "around"]:
            Commands.look_around()

        case ["take", *item] | ["get", *item]:
            Commands.take(item)

        case ["drop", *item]:
            Commands.drop(item)

        case ["i"] | ["inventory"] | ["check", "pockets"] | ["check", "pocket"]:
            Commands.inventory()

        case ["quit"]:
            print("\nQuitters!\n")
            quit()

        case other:
            print("Sorry, you can't do that yet.")