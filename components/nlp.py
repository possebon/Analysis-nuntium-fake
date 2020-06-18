from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob
import spacy


def tokenize_string(string:str) -> str:
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

def get_polarity_and_subjectivity_from_string(string:str) -> list:
    blob = TextBlob(string)
    
    if blob.detect_language() != "en":
        blob = TextBlob(str(blob.translate(to="en")))
        
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return [polarity, subjectivity]

def get_polarity_scores(string:str) -> dict:
    """Gets polarity scores from VADER

    Args:
        string (str): a news article

    Returns:
        dict: neg, neu, pos, compound
    """    
    
    analyzer = SentimentIntensityAnalyzer()
    
    string = TextBlob(string)
    if string.detect_language() != "en":
        string = str(string.translate(to="en"))
        
    return analyzer.polarity_scores(string)
        
    
    
    



