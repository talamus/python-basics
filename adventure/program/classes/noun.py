
class Noun:
    article = None
    name = None
    adjectives = None
    other_names = None

    def __init__(self, input):                      # define __init__ that is called every time Noun type object is created
        if isinstance(input, str):                  # if input is string
            input = input.split()                   # split input string into list
        else:                                       # else if input is not string (something list like, iterable)
            input = list(input)                     # make a list of input (so we don't mess up the original by mistake)

        articles = ("a", "an", "the")               # define articles, this is a tuple list (can't be changed)
        prepositions = ("of", "with")               # define prepositions for splitting longer item names in input

        if input and input[0] in articles:          # if input is not empty and the first item in split input list is in articles list
            self.article = input[0]                 # make that item the article (becomes a string)
            input = input[1:]                       # set input list to be input list starting from second item (-> remove article from list)

        if input and prepositions[0] in input:
            index_list = []
            for i in range(0, len(input)):
                if input[i] == prepositions[0]:
                    index_list.append(i)

            self.name = input.pop((index_list[0] - 1))
            self.adjectives = input
            input_new = list(input)
            self.other_names = input_new.pop(index_list[0] + 1)

        else:
            self.name = input.pop()                     # take last item of input list, make that the name of object (becomes a string)
            self.adjectives = input                     # remaining items on input list are marked as adjectives (remains as a list)

        print(":::", self.__dict__)


    def the(self):
        output = []
        if self.article:
            output.append("the")
        else:
            output.append("some")
        output += self.adjectives                      # a+=b is shorthand for a = a + b :) so this adds self.adjectives to output
        output.append(self.name)
        return " ".join(output)

    def __eq__(self, other):                        # defining comparison between 'self' and 'other
        other = Noun(other)                         # make 'other' also into Noun type object
        difference = set(                           # create variable difference that compares
            map(str.lower, other.adjectives)        # other.adjectives (adjectives of the input) (mapped to lowercase)
        ).difference(set(                           # via the set method  .difference
            map(str.lower, self.adjectives)         # with self.adjectives (adjectives of the object) (mapped to lowercase)
        ))

        if self.name.lower() == other.name.lower():    # if input is exactly the object name
            if difference:                             # and then if difference returns True (meaning result of it is not empty, there are differencies)
                return False                           # then return False (input and object don't match)
            else: return True                          # at least part of input matches object, so return True
        else: return False                             # input doesn't match name of object, return False

    def __str__(self) -> str:                          # Create a new string object from the given object (-> is just a type hint and not a function )
        output = []
        if self.article:
            output.append(self.article)

            if self.other_names:
                output.append(self.name)
                output += self.adjectives
                return " ".join(output)

            else:
                output += self.adjectives                      # a+=b is shorthand for a = a + b :) so this adds self.adjectives to output
                output.append(self.name)
                return " ".join(output)
