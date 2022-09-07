from program.classes.noun import Noun

book = Noun("an old book of magic spells of destruction")

def test_book_comparison():
    assert book == "old book"
    assert book == "book of magic spells"
    assert book == "book of spells"
    assert book == "old book of spells"
    assert book == "book of magic"
    assert book == "book of destruction"

def test_spells_comparison():
    assert book == "magic spells"
    assert book == "spells"
    assert book == "the spells of destruction"
   
    