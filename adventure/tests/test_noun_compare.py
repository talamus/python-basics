from program.classes.noun import Noun

bottle = Noun("a bright blue bottle")
book = Noun("the Big Black Bible")
inventory = [ bottle, book ]

def test_book_adjectives():
    assert book == "bible"
    assert book == "big bible"
    assert book == "a black bible"
    assert book != "pink bible"

def test_inventory_matching():
    assert "bible" in inventory
    assert "the blue bottle" in inventory
    assert "red bottle" not in inventory

def test_string_output():
    assert str(bottle) == "a bright blue bottle"
    assert str(book) == "the Big Black Bible"