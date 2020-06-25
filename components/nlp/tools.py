# External Libraries
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import spacy

def tokenize_string(string:str) -> list:
    tknzr = TweetTokenizer()
    return tknzr.tokenize(string)

def lemmatize_token(token:str) -> str:
    lmtzr = spacy.load("pt_core_news_sm")
    for t in lmtzr(token):
        return t.lemma_
    
def remove_stop_word(tokens:list) -> list:
    stop_words = stopwords.words("portuguese")
    without_stop_words = [t for t in tokens if t not in stop_words]
    return without_stop_words