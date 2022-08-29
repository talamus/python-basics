
def parse(raw_command):
    splitted = raw_command.split()    
    return splitted[0], splitted[1:]

# Test code that is run when this module is being developed:
if __name__ == "__main__":

    test_command = "take apple"
    print("test command:", test_command)
    print("output:", parse(test_command))

    test_command = "inventory"
    print("test command:", test_command)
    print("output:", parse(test_command))
