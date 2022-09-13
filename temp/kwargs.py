

def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for key, value in kwargs.items():
        result += f" ( {key} : {value} ) "
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
