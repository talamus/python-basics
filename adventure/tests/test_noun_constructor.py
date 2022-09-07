from program.classes.noun import Noun

def test_simple_noun_with_article():
    word = Noun("an apple")
    assert word.article == "an"
    assert word.name == "apple"
    assert word.adjectives == []

def test_noun_without_article():
    word = Noun("water")
    assert word.article == None
    assert word.name == "water"
    assert word.adjectives == []

def test_noun_without_article_and_with_an_adjective():
    word = Noun("clear water")
    assert word.article == None
    assert word.name == "water"
    assert word.adjectives == ["clear"]

def test_noun_with_article_and_multiple_adjectives():
    word = Noun("a big bad wolf")
    assert word.article == "a"
    assert word.name == "wolf"
    assert word.adjectives == ["big", "bad"]

def test_noun_with_article_and_multiple_adjectives():
    word = Noun("the big bad wolf")
    assert word.article == "the"
    assert word.name == "wolf"
    assert word.adjectives == ["big", "bad"]
