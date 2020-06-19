# Setup path for parent directory
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# External Libraries
import pandas as pd
import plotly.express as px
# Components
from nlp.common_words import get_most_common_bigrams, remove_common_stop_words
from dataset import load_dataframe_from_csv, download_dataframe_as_csv

def create_chart():
    path = "../../data_csv/true.csv"

    df = load_dataframe_from_csv(path)

    common_bigrams = get_most_common_bigrams(df)
    common_bigrams = remove_common_stop_words(common_bigrams.most_common(30000))
    common_bigrams =  [b for b in common_bigrams if b != 0]
    df = pd.DataFrame(common_bigrams)
    df.columns = ["Bigram", "Count"]

    df = df.sort_values(by="Count", ascending=False)
    return df

def download_chart(df):
    download_dataframe_as_csv(df, "../../data_csv/plots/common_bigrams")
    
def get_chart(size:int=500):
    df = pd.read_csv("../../data_csv/plots/common_bigrams.csv")
    return df[:size]    

def display_chart(df):
    df = get_chart(1500)
    fig = px.bar(df, x="Bigram", y="Count")
    fig.show()
    
df = create_chart()

download_chart(df)

display_chart(df)