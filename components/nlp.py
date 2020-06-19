from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from translate import Translator
from textblob import TextBlob
from faker import Faker
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
        
    
def translate_to_en(string:str) -> str:
    translator = get_new_translator()
    divide = False
    if len(string) > 500:
        divide = True
        first_index = 0
        last_index = string[:500].rfind(".")
    if not divide:    
        translation = translator.translate(string)
        

    while divide:
        translation = ""
        translation_ = translator.translate(string[first_index:last_index])
        
        # Check if exceeded requests amount
        while len(translation_) == 194 and "MYMEMORY" in translation_:
            translator = get_new_translator()
            translation_ = translator.translate(string[first_index:last_index])
        translation += translation_
        if len(string) - last_index > 500:
            step = last_index + 500
            print("Step: ", step)
            range_index = string[last_index:step].rfind(".")
            if range_index <= 0:
                range_index = string[last_index:step].rfind(",")
            if range_index <= 0:
                range_index = string[last_index:step].rfind(" ")
            print("Last index: ", last_index)
            print("Range: ", range_index)
            last_index = range_index + last_index
            print("New Last index: ", last_index)
            print("Len string: ", len(string))
        else:
            translation_ = translator.translate(string[last_index:])
            # Check if exceeded requests amount
            while len(translation_) == 194 and "MYMEMORY" in translation_:
                translator = get_new_translator()
                translation_ = translator.translate(string[first_index:last_index])
            translation += translation_      
            divide = False
            
    return translation

def get_new_translator():
    faker = Faker()
    email = faker.email()
    print(email)
    translator = Translator(from_lang="pt-br", to_lang="en", email=email)
    return translator
