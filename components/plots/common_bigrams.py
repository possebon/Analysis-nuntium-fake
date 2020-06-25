# Setup path for parent directory
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# External Libraries
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
# Components
from nlp.common_words import get_most_common_bigrams, remove_common_stop_words
from dataset import load_dataframe_from_csv, download_dataframe_as_csv

def create_dataframes() -> list:
    path_true = "../../data_csv/true.csv"
    path_fake = "../../data_csv/fake.csv"

    df_true = load_dataframe_from_csv(path_true)
    df_fake = load_dataframe_from_csv(path_fake)

    common_bigrams = get_most_common_bigrams(df_true)
    common_bigrams = remove_common_stop_words(common_bigrams.most_common(30000))
    common_bigrams =  [b for b in common_bigrams if b != 0]
    df_true = pd.DataFrame(common_bigrams)
    df_true.columns = ["Bigram", "Count"]
    df_true = df_true[df_true["Count"] != 0]
    
    common_bigrams = get_most_common_bigrams(df_fake)
    common_bigrams = remove_common_stop_words(common_bigrams.most_common(30000))
    common_bigrams =  [b for b in common_bigrams if b != 0]
    df_fake = pd.DataFrame(common_bigrams)
    df_fake.columns = ["Bigram", "Count"]
    df_fake = df_fake[df_fake["Count"] != 0]
    
    df_true = df_true.sort_values(by="Count", ascending=False)
    df_fake = df_fake.sort_values(by="Count", ascending=False)

    return [df_true, df_fake]

def download_dataframes(df_true, df_fake):
    download_dataframe_as_csv(df_true, "../../data_csv/plots/true_common_bigrams")
    download_dataframe_as_csv(df_fake, "../../data_csv/plots/fake_common_bigrams")
    
def get_dataframes(size:int=500):
    df_true = pd.read_csv("../../data_csv/plots/true_common_bigrams.csv")
    df_fake = pd.read_csv("../../data_csv/plots/fake_common_bigrams.csv")
    return [df_true[:size], df_fake[:size]]    

def display_chart(df_true, df_fake):
    df_true, df_fake = get_dataframes(150)
    
    df_true.insert(0, "Veracity", "True")
    df_fake.insert(0, "Veracity", "Fake")
    df = pd.concat([df_true, df_fake])
    colors = ["blue" if veracity == "True" else "red" for veracity in df["Veracity"]]
    
    fig = make_subplots(rows=1, cols=3, subplot_titles=["True", "True/Fake", "Fake"], shared_yaxes=True)

    fig.add_trace(
        go.Bar(x=df_true["Bigram"], y=df_true["Count"]),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=df["Bigram"], y=df["Count"], marker=dict(color = colors)),
        row=1, col=2
    )

    fig.add_trace(
        go.Bar(x=df_fake["Bigram"], y=df_fake["Count"], marker=dict(color= "red")),
        row=1, col=3
    )
    fig.show()

#df_true, df_fake = create_dataframes()
#download_dataframes(df_true, df_fake)

df_true, df_fake = get_dataframes()
display_chart(df_true, df_fake)