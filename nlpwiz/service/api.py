
import os
import logging
import traceback

from nlpwiz.service import client #this works only where services are installed as microservices(check with Ajay)

logger = logging.getLogger(__name__)


def get_similar_words(model_name, word, count=100):
    method_name = "similar_words"
    try:
        similar_words = client.invoke(model_name, method_name=method_name, params={"word": word, "count": count})
        logging.debug("similar words for {}: {}".format(word, str(similar_words)))
    except Exception as e:
        logger.warning(e)
        traceback.print_exc()
        similar_words = []
    #return [w.replace("_", " ")for w in simila
    return [w for w in similar_words if "_" not in w]


def get_words_dist(model_name, word1, word2):
    try:
        similarity = client.invoke(model_name, method_name="similarity", params={"word1": word1, "word2": word2})
    except Exception as e:
        logger.warning(str(e))
        traceback.print_exc()
        similarity = None

    if similarity is None:
        return similarity
    else:
        return 1 - similarity #sim to distance


def sentence_vector(txt, model="word2vec"):
    try:
        sentence_score = client.invoke(model, method_name="sentence_vector", params={"sentence": txt})
    except Exception as e:
        logger.warning(str(e))
        sentence_score = None
    return sentence_score

def sentence_similarity(s1, s2, model="word2vec"):
    sentence_score = client.invoke(model, method_name="sentence_similarity", params={"sentence1": s1, "sentence2": s2})
    return sentence_score


def word_vector(txt, model="word2vec"):
    try:
        sentence_score = client.invoke(model, method_name="infer", params={"word": txt})
    except Exception as e:
        logger.warning(str(e))
        traceback.print_exc()
        sentence_score = None
    return sentence_score


def perplexity(text):
    perplexity = client.invoke(model_name="language_model", method_name="perplexity",
                               params={"sentence": text},
                               model_params={"lmname": "4gram.lm.pruned.1e-9"})
    return perplexity
