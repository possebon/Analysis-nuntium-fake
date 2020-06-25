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
from wordcloud import WordCloud
import base64
# Components
from nlp.common_words import get_most_common_words, remove_common_stop_words
from dataset import load_dataframe_from_csv, download_dataframe_as_csv

def get_dataframes() -> list:
    path_true = "./data_csv/true.csv"
    path_fake = "./data_csv/fake.csv"
    
    df_true = load_dataframe_from_csv(path_true)
    df_fake = load_dataframe_from_csv(path_fake)
    
    return [df_true, df_fake]

def create_dataframes() -> list:
    path_true = "../../data_csv/true.csv"
    path_fake = "../../data_csv/fake.csv"

    df_true = load_dataframe_from_csv(path_true)
    df_fake = load_dataframe_from_csv(path_fake)

    common_words = get_most_common_words(df_true)
    common_words = remove_common_stop_words(common_words)
    df_true = pd.DataFrame.from_dict(common_words, orient="index").reset_index()
    df_true.columns = ["Word", "Count"]
    df_true = df_true.sort_values(by="Count", ascending=False)
    
    common_words = get_most_common_words(df_fake)
    common_words = remove_common_stop_words(common_words)
    df_fake = pd.DataFrame.from_dict(common_words, orient="index").reset_index()
    df_fake.columns = ["Word", "Count"]
    df_fake = df_fake.sort_values(by="Count", ascending=False)

    return [df_true, df_fake]

def download_dataframes(df_true, df_fake) -> None:
    download_dataframe_as_csv(df_true, "./data_csv/plots/true_common_words")
    download_dataframe_as_csv(df_fake, "./data_csv/plots/fake_common_words")

def get_dataframes_words(size:int=500) -> list:
    df_true = pd.read_csv("./data_csv/plots/true_common_words.csv")
    df_fake = pd.read_csv("./data_csv/plots/fake_common_words.csv")
    return [df_true[:size], df_fake[:size]]    
    
def get_dataframes_bigrams(size:int=500) -> list:
    df_true = pd.read_csv("./data_csv/plots/true_common_bigrams.csv")
    df_fake = pd.read_csv("./data_csv/plots/fake_common_bigrams.csv")
    return [df_true[:size], df_fake[:size]]    

def display_chart_words(df_true, df_fake):
    df_true, df_fake = get_dataframes_words(150)
    
    df_true.insert(0, "Veracity", "True")
    df_fake.insert(0, "Veracity", "Fake")
    df = pd.concat([df_true, df_fake])
    colors = ["blue" if veracity == "True" else "red" for veracity in df["Veracity"]]
    
    fig = make_subplots(rows=1, cols=3, subplot_titles=["True", "True/Fake", "Fake"], shared_xaxes=True)

    fig.add_trace(
        go.Bar(x=df_true["Count"], y=df_true["Word"], name="True", orientation='h'),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=df["Count"], y=df["Word"], marker=dict(color = colors), orientation='h'),
        row=1, col=2
    )

    fig.add_trace(
        go.Bar(x=df_fake["Count"], y=df_fake["Word"], name="Fake", marker=dict(color= "red"), orientation='h'),
        row=1, col=3
    )
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
    return fig

def display_chart_bigrams(df_true, df_fake):
    df_true, df_fake = get_dataframes_bigrams(150)
    
    df_true.insert(0, "Veracity", "True")
    df_fake.insert(0, "Veracity", "Fake")
    df = pd.concat([df_true, df_fake])
    colors = ["blue" if veracity == "True" else "red" for veracity in df["Veracity"]]
    
    fig = make_subplots(rows=1, cols=3, subplot_titles=["True", "True/Fake", "Fake"], shared_yaxes=True)

    fig.add_trace(
        go.Bar(x=df_true["Bigram"], y=df_true["Count"], name="True"),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(x=df["Bigram"], y=df["Count"], marker=dict(color = colors)),
        row=1, col=2
    )

    fig.add_trace(
        go.Bar(x=df_fake["Bigram"], y=df_fake["Count"], name="Fake", marker=dict(color= "red")),
        row=1, col=3
    )
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
    return fig
    
#df_true, df_fake = create_dataframes()
#download_dataframes(df_true, df_fake)

#df_true, df_fake = get_dataframes()
#display_chart(df_true, df_fake)


def display_wordcloud_words():
    df_true, df_fake = get_dataframes_words()
    
    df_true = remove_common_stop_words(df_true)
    df_fake = remove_common_stop_words(df_fake)
    
    wordcloud_image = "./assets/wordcloud_true_words2.png"
    wordcloud_true = WordCloud(width=800, height=600,background_color="white")
    words = {}
    for i, row in df_true.iterrows():
        words[row["Word"]] = row["Count"]
    wordcloud_true = wordcloud_true.generate_from_frequencies(words)
    wordcloud_true.to_file(wordcloud_image)
    
    wordcloud_image = "./assets/wordcloud_fake_words2.png"
    wordcloud_fake = WordCloud(width=800, height=600,background_color="white")
    words = {}
    for i, row in df_fake.iterrows():
        words[row["Word"]] = row["Count"]
    wordcloud_fake = wordcloud_fake.generate_from_frequencies(words)
    wordcloud_fake.to_file(wordcloud_image)
    
def display_wordcloud_bigrams():
    df_true, df_fake = get_dataframes_bigrams()
    
    df_true = remove_common_stop_words(df_true)
    df_fake = remove_common_stop_words(df_fake)
    
    wordcloud_image = "./assets/wordcloud_true_bigrams.png"
    wordcloud_true = WordCloud(width=800, height=600,background_color="white")
    words = {}
    for i, row in df_true.iterrows():
        words[row["Bigram"]] = row["Count"]
    wordcloud_true = wordcloud_true.generate_from_frequencies(words)
    wordcloud_true.to_file(wordcloud_image)
    
    wordcloud_image = "./assets/wordcloud_fake_bigrams.png"
    wordcloud_fake = WordCloud(width=800, height=600,background_color="white")
    words = {}
    for i, row in df_fake.iterrows():
        words[row["Bigram"]] = row["Count"]
    wordcloud_fake = wordcloud_fake.generate_from_frequencies(words)
    wordcloud_fake.to_file(wordcloud_image)
    
    
    