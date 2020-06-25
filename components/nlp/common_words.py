# Python Standard Libraries
from collections import Counter
import string
# External Libraries
from nltk.corpus import stopwords
# Components
from nlp.tools import tokenize_string

def get_most_common_words(dataframe):
    common_words = Counter()
    for id, row in dataframe.iterrows():
        for word in row["News"].split(" "):
            punctuation = str.maketrans(dict.fromkeys(string.punctuation))
            word = word.translate(punctuation)
            common_words[word] += 1
    return common_words

def get_most_common_words_lemmatized(dataframe):
    common_words = Counter()
    for id, row in dataframe.iterrows():
        tokens = tokenize_string(row["News"])
        for word in tokens:
            punctuation = str.maketrans(dict.fromkeys(string.punctuation))
            word = word.translate(punctuation)
            common_words[word] += 1
    return common_words


def get_most_common_bigrams(dataframe):
    common_bigrams = Counter()
    for row in dataframe.itertuples():
        last_word = ""
        rows = row[4].split(" ")
        for word in rows:
            punctuation = str.maketrans(dict.fromkeys(string.punctuation))
            word = word.translate(punctuation)
            if len(word) > 1:
                if len(last_word) > 1:
                    common_bigrams[f"{last_word} {word}"] += 1
            last_word = word
    return common_bigrams
            

def remove_common_stop_words(common_words):
    for i, word in enumerate(list(common_words)):
        # This allows the method to be used on bigrams
        if isinstance(word, tuple):
            words = word[0].split(" ")
            for word in words:
                if word in stopwords.words("portuguese") or len(word) < 3:
                    common_words[i] = ("", 0)
        else:
            if word in stopwords.words("portuguese") or len(word) < 3:
                    common_words[word] = 0
    return common_words



