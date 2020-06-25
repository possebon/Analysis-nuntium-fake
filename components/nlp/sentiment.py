# External Libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def get_polarity_and_subjectivity_from_string(string:str) -> list:
    blob = TextBlob(string)
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
        
    return analyzer.polarity_scores(string)