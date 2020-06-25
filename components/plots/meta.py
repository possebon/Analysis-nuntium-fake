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
from dataset import load_dataframe_from_csv

def get_dataframes() -> list:
    path_true = "./data_csv/true-meta.csv"
    path_fake = "./data_csv/fake-meta.csv"
    
    df_true = load_dataframe_from_csv(path_true)
    df_fake = load_dataframe_from_csv(path_fake)
    
    return [df_true, df_fake]

# Page 0 - Categories

def display_charts_category(df_true):

    fig = px.pie(df_true, names="Category")
    return fig
        

# Page 1 - Emotivity, Diversity and Pausality

def display_charts_emotiveness(df_true, df_fake):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Emotiveness"], name="Fake", xbins=dict(start=0, size = 0.005),\
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Emotiveness"], name="True", xbins=dict(start=0, size = 0.005),\
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
    
def display_charts_diversity(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Diversity"], name="Fake", xbins=dict(start=0, size = 0.005), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Diversity"], name="True", xbins=dict(start=0, size = 0.005), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
    
def display_charts_pausality(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Pausality"], name="Fake", xbins=dict(start=0, size = 0.1), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Pausality"], name="True", xbins=dict(start=0, size = 0.1), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig

# Page 2 - Tokens, Words and Characters

def display_charts_tokens(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Tokens"], name="Fake", xbins=dict(start=0, size = 20), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Tokens"], name="True", xbins=dict(start=0, size = 20), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
    
def display_charts_words(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Words"], name="Fake", xbins=dict(start=0, size = 10), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Words"], name="True", xbins=dict(start=0, size = 10), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig    
def display_charts_characters(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Characters"], name="Fake", xbins=dict(start=0, size = 50), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Characters"], name="True", xbins=dict(start=0, size = 50), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
    
# Page 3 - Verbs

def display_charts_verbs(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Verbs"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Verbs"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig  

def display_charts_subjuntive_imperative_verbs(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Subjuntive\Imperative Verbs"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Subjuntive\Imperative Verbs"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig 
     
def display_charts_modal_verbs(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Modal Verbs"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Modal Verbs"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
  
# Page 4 - Pronouns

def display_charts_pronouns(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Pronouns"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Pronouns"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig

def display_charts_singular_second_personal_pronouns(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Singular\Second Personal Pronouns"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Singular\Second Personal Pronouns"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig

def display_charts_plural_first_personal_pronouns(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Plural First Personal Pronouns"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Plural First Personal Pronouns"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig  
        
# Page 5 - Adjectives, Adverbs and Nouns

def display_charts_adjectives(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Adjectives"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Adjectives"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig   

def display_charts_adverbs(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Adverbs"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Adverbs"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig 
    
def display_charts_nouns(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Nouns"], name="Fake", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Nouns"], name="True", xbins=dict(start=0, size = 1.0), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig 
    
# Page 6 - Word and Sentence Length

def display_charts_average_word_length(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Average Word Length"], name="Fake", xbins=dict(start=0, size = 0.01), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Average Word Length"], name="True", xbins=dict(start=0, size = 0.01), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig

def display_charts_average_sentence_length(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Average Sentence Length"], name="Fake", xbins=dict(start=0, size = 0.05), \
        marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Average Sentence Length"], name="True", xbins=dict(start=0, size = 0.05), \
        marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
    
# Page 7 - Others

def display_charts_words_uppercase(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Words Uppercase"], name="Fake", marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Words Uppercase"], name="True", marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig 

def display_charts_mispelling(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Percentage of Spelling Errors"], name="Fake", marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Percentage of Spelling Errors"], name="True", marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig

def display_charts_links(df_true, df_fake):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df_fake["Links Inside"], name="Fake", marker=dict(color= "red"), opacity=0.4))
    fig.add_trace(go.Histogram(x=df_true["Links Inside"], name="True", marker=dict(color= "blue"), opacity=0.6))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(barmode='overlay', showlegend=False, margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig
    
# Page 8 - 3D

def display_charts_3d_page_1(df_true, df_fake):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=df_fake["Average Sentence Length"], y=df_fake["Diversity"], z=df_fake["Words"], \
        name="Fake", mode='markers', marker=dict(color= "red", opacity=0.3)))
    fig.add_trace(go.Scatter3d(x=df_true["Average Sentence Length"], y=df_true["Diversity"], z=df_true["Words"], \
        name="True", mode='markers', marker=dict(color= "blue", opacity=0.3)))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), hovermode="x")
    return fig

def display_charts_3d_page_2(df_true, df_fake):
    fig = go.Figure()
    fig.add_trace(go.Scatter3d(x=df_fake["Characters"], y=df_fake["Verbs"], z=df_fake["Percentage of Spelling Errors"], \
        name="Fake", mode='markers', marker=dict(color= "red", opacity=0.3)))
    fig.add_trace(go.Scatter3d(x=df_true["Characters"], y=df_true["Verbs"], z=df_true["Percentage of Spelling Errors"], \
        name="True", mode='markers', marker=dict(color= "blue", opacity=0.3)))
    fig.update_traces(hovertemplate=None)
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), showlegend=False, hovermode="x")
    return fig