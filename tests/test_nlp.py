import pytest

from nlpwiz import nlp

TEST_TEXT = "Jack went to New York by the morning flight"

def test_annotation():
    tags = nlp.parse(TEST_TEXT)
    assert tags[0]["pos"] == "PROPN"
    assert tags[0]["dep"] == "nsubj"


def test_lemmatization():
    lemmas = nlp.lemmatize(TEST_TEXT)
    assert lemmas[1] == "go"
