import re
import multiprocessing

import spacy
from nltk.corpus import stopwords

PUNCTS = ['-', '$', '&', '.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{','}']
STOP_WORDS = set(stopwords.words('english'))
SEPERATORS = [" ", "\t", "\n"]
STOP_WORDS.update(PUNCTS)

spacy_ = spacy.load('en')


def parse(text):
    """
    spacy annotations: https://stackoverflow.com/questions/40288323/what-do-spacys-part-of-speech-and-dependency-tags-mean
    """
    text = re.sub('[ ]+', ' ', text).strip()  # Convert multiple whitespaces into one

    doc = spacy_(text)

    token_tags = []
    for tok in doc:
        tags = {"text": tok.text, "lemma": tok.lemma_, "pos": tok.pos_,
                "tag": tok.tag_, "dep": tok.dep_, "shape": tok.shape_,
                     "is_alpha": tok.is_alpha, "is_stop": tok.is_stop}
        token_tags.append(tags)

    return token_tags


def ner(text):
    """
    Using spacy for ner
    """
    doc = spacy_(text)
    named_entities = []
    for tok in doc.ents:
        named_entities.append({"text": tok.text, "start": tok.start_char, "end": tok.end_char, "label": tok.label_})
    return named_entities


def lemmatize(text):
    doc = spacy_(text)
    return [tok.lemma_ for tok in doc]
