from string import Formatter
from textwrap import TextWrapper
from program.classes.noun import Noun

class StoryFormatter(Formatter):
    sentences = []
    textwrapper = None

    def __init__(self, width=70, left_margin="    ", first_paragraph_indent="", following_paragraph_indent="    "):
        self.left_margin = left_margin
        self.first_paragraph_indent = first_paragraph_indent
        self.following_paragraph_indent = following_paragraph_indent
        self.sentences = []
        self.textwrapper = TextWrapper(
            width=width,
            initial_indent=first_paragraph_indent + left_margin,
            subsequent_indent=left_margin
        )

    def __str__(self):
        text = " ".join(self.sentences)
        return "\n".join(self.textwrapper.wrap(text))

    def end_chapter(self):
        print(str(self))
        self.sentences = []
        self.textwrapper.initial_indent = self.left_margin + self.first_paragraph_indent

    def start_new_paragraph(self):
        print(str(self))
        self.sentences = []
        self.textwrapper.initial_indent = self.left_margin + self.following_paragraph_indent

    def say_sentence(self, format_string, *args, **kwargs):
        self.format(format_string, *args, **kwargs)

    def format(self, format_string, *args, **kwargs):
        self.sentences.append(super().format(format_string, *args, **kwargs))

    def format_field(self, value, format_spec):

        # Make sure we are handling a list of nouns (or something very similar)
        words=None
        match value:
            case list() | tuple() as value: words = list(map(Noun, value))
            case str()            as value: words = [ Noun(value) ]
            case Noun()           as value: words = [ value ]
            case _: return super().format_field(value, format_spec)

        if not len(words):
            return "nothing"

        # Parse formatting info:
        #   :or         last_separator = "or"
        #   :the        noun_prefix = "the"
        #   :some       noun_prefix = "some"
        noun_prefix = None
        last_separator = "and"
        for spec in format_spec.split(":"):
            match spec:
                case "or":   last_separator = "or"
                case "the":  noun_prefix = "the"
                case "some": noun_prefix = "some"
                case "":     pass
                case _:      raise ValueError(f"Unknown format spec `{spec}`")

        # Convert words into strings (with correct prefixes)
        words = list(map(lambda noun: noun.__str__(prefix=noun_prefix), words))

        if len(words) == 1:
            return words[0]
        last_word = words.pop()
        return ", ".join(words) + " " + last_separator + " " + last_word

#===================================================================

storyformatter = StoryFormatter()

say_sentence        = storyformatter.say_sentence
start_new_paragraph = storyformatter.start_new_paragraph
end_chapter         = storyformatter.end_chapter

say_sentence("Joopa joo.")
say_sentence("Jaakolla oli iso {:the}.", Noun("a makkara"))
say_sentence("Se oli tosi {nasta:the}.", nasta=[Noun("nice"), Noun("lovely"), "a best"])
say_sentence("Jaakolla oli iso {}.", Noun("a makkara"))
say_sentence("Se oli tosi {nasta:or:some}.", nasta=[Noun("nice"), Noun("lovely"), "a best"])
say_sentence("Jaakolla oli iso {}.", Noun("a makkara"))
say_sentence("Se oli tosi {nasta:the}.", nasta=[Noun("nice"), Noun("lovely"), "a best"])
say_sentence("Jaakolla oli iso {}.", [])
start_new_paragraph()
say_sentence("Makkara oli tosi {nasta:the}.", nasta=[Noun("nice"), Noun("lovely"), "a best"])
say_sentence("Jaakolla oli iso {}.", Noun("a makkara"))
say_sentence("Se oli tosi {nasta:the}.", nasta=[Noun("nice"), Noun("lovely"), "a best"])
say_sentence("Jaakolla oli iso {}.", Noun("a makkara"))
say_sentence("Sen koko oli {:.2f} megapascalia.", 123.456789)
say_sentence("Jaakolla oli iso {}.", Noun("a makkara"))
say_sentence("Se oli tosi {nasta:the}.", nasta=[Noun("nice"), Noun("lovely"), "a best"])
end_chapter()


