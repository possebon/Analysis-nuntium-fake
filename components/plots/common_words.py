# Setup path for parent directory
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# External Libraries
import pandas as pd
import plotly.express as px
# Components
from nlp.common_words import get_most_common_words, remove_common_stop_words
from dataset import load_dataframe_from_csv, download_dataframe_as_csv

def create_chart():
    path = "../../data_csv/true"

    df = load_dataframe_from_csv(path)

    common_words = get_most_common_words(df)
    common_words = remove_common_stop_words(common_words)

    df = pd.DataFrame.from_dict(common_words, orient="index").reset_index()
    df.columns = ["Word", "Count"]

    df = df.sort_values(by="Count", ascending=False)
    return df

def download_chart(df):
    download_dataframe_as_csv(df, "../../data_csv/plots/common_words")
    
def get_chart(size:int=500):
    df = pd.read_csv("../../data_csv/plots/common_words.csv")
    return df[:size]    

def display_chart(df):
    df = get_chart(1500)
    fig = px.bar(df, x="Word", y="Count")
    fig.show()