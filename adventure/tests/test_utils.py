from program.utils import list_index, list_split

def test_splitting_by_of():
    input = "an old book of magic spells of destruction".split()
    splitter = "of"
    result = list_split(splitter, input)
    assert result[0] == ["an", "old", "book"]
    assert result[1] == ["magic", "spells", "of", "destruction"]

def test_splitting_by_filled_with():
    input = "a crystal bottle filled with holy water".split()
    splitter = ["filled", "with"]
    result = list_split(splitter, input)
    assert result[0] == ["a", "crystal", "bottle"]
    assert result[1] == ["holy", "water"]

def test_splitting_by_filled_with_2():
    input = "spinach filled cheese with wine bottle filled with drunkness".split()
    splitter = ["filled", "with"]
    result = list_split(splitter, input)
    assert result[0] == ["spinach", "filled", "cheese", "with", "wine", "bottle"]
    assert result[1] == ["drunkness"]

def test_list_index():
    short_list = ["filled", "with"]
    long_list = "a crystal bottle filled with holy water".split()
    assert list_index(short_list, long_list) == 3
    assert list_index(["of"], long_list) == None
