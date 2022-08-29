
from parser import parse

raw_command = input("What do? ")

command, parameters = parse(raw_command)

print("Do:", command)
print("Params:", parameters)

