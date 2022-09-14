from string import Formatter
from program.classes.noun import Noun
from program.utils import join_neatly

class SentenceFormatter(Formatter):
    sentences = []

    def __str__(self):
        return " ".join(self.sentences)

    def format(self, format_string, **args):
        self.sentences.append(super().format(format_string, **args))

    def format_field(self, value, format_spec):

        #   :and    <- last_separator = "and" (the default)
        #   :or     <- last_separator = "or"
        #   :a :an  <- noun_article = "a" or "an" or empty (Noun handles this)
        #   :the    <- noun_article = "the" or empty (Noun handles this)

        article = "an"
        last_separator = "and"
        for spec in format_spec.split(":"):
            if spec == "and":
                last_separator = "and"
            elif spec == "or":
                last_separator = "or"
            elif spec == "the":
                article = "the"
            elif spec == "a" or spec == "an":
                article = "an"

        if isinstance(value, Noun):
            value = [value]

        if isinstance(value, list):
            if article == "the":
                value = list(map(lambda noun: noun.the(), value))
            value = list(map(lambda noun: str(noun), value))
            value = join_neatly(value)

        if not isinstance(value, str):
            value = str(value)

        return super().format(value, format_spec)

#===================================================================

text_output = SentenceFormatter()
add_sentence = text_output.format

add_sentence("Jaakolla oli iso {kala:the}.", kala=Noun("a makkara"))
add_sentence("Se oli tosi {nasta}.", nasta=[Noun("nice"), Noun("lovely"), Noun("the best")])

print("--------------------")
print(text_output)


