
# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from components.plots import meta, common_words

df_true, df_fake = meta.get_dataframes()

# Page 0
categories = meta.display_charts_category(df_true)

# Page 1
emotiveness = meta.display_charts_emotiveness(df_true, df_fake)
diversity = meta.display_charts_diversity(df_true, df_fake)
pausality = meta.display_charts_pausality(df_true, df_fake)

# Page 2
tokens = meta.display_charts_tokens(df_true, df_fake)
words = meta.display_charts_words(df_true, df_fake)
characters = meta.display_charts_characters(df_true, df_fake)

# Page 3
verbs = meta.display_charts_verbs(df_true, df_fake)
verbs2 = meta.display_charts_subjuntive_imperative_verbs(df_true, df_fake)
verbs3 = meta.display_charts_modal_verbs(df_true, df_fake)

# Page 4
pronouns = meta.display_charts_pronouns(df_true, df_fake)       
pronouns2 = meta.display_charts_singular_second_personal_pronouns(df_true, df_fake)
pronouns3 = meta.display_charts_plural_first_personal_pronouns(df_true, df_fake)

# Page 5
adjectives = meta.display_charts_adjectives(df_true, df_fake) 
adverbs = meta.display_charts_adverbs(df_true, df_fake)  
nouns = meta.display_charts_nouns(df_true, df_fake)

# Page 6 
avg_word_length = meta.display_charts_average_word_length(df_true, df_fake)   
avg_sentence_length = meta.display_charts_average_sentence_length(df_true, df_fake) 

# Page 7
words_uppercase = meta.display_charts_words_uppercase(df_true, df_fake)
mispelling = meta.display_charts_mispelling(df_true, df_fake)
links = meta.display_charts_links(df_true, df_fake)

# Page 8
page1_3d = meta.display_charts_3d_page_1(df_true, df_fake)
page2_3d = meta.display_charts_3d_page_2(df_true, df_fake)

home = html.Div([
    html.H2("Dados das Fake News Brasileiras"),
    html.P("26/06/2020"),
    html.H4("Fake.Br Corpus"),
    html.P("Como ponto de partida vamos utilizar a base de dados do Fake.Br Corpus,"),
    html.P("que foi a base criada pelo Núcleo Interinstitucional de Linguística Computacional"),
    html.P(" (NILC) para treinar uma ferramenta de detecção automática de fake news em português."),
    html.P(" Esta base é composta por 7.200 notícias (3.600 verdadeiras + 3.600 falsas)"),
    html.P(" que foram coletadas nos mais diversos diários do Brasil."),
    html.H4("Perguntas"),
    html.P("Existe algum período onde o número de fake news são maiores?"),
    html.P("Existe relação entre a escrita correta e as fake news?"),
    html.P("Quais são os temas com mais fake news?")
], style={"margin": "2em"})

page1 = html.Div([
    dcc.Tabs([
        # Page 0
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Categories', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = categories, config={ 'displayModeBar': False})
                ])
            ], style={"padding":"5vh", "width" : "50%", "margin" : "auto"}),
        label="Categories"),
        # Page 1
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Emotiveness', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = emotiveness, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Diversity', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = diversity, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Pausality', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = pausality, config={ 'displayModeBar': False})
                ], style={"width": "30%"})
            ], className="row", style={"padding":"5vh"}),
        label="Emotivity, Diversity and Pausality"),
        # Page 2
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Tokens', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = tokens, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Words', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = words, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Characters', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = characters, config={ 'displayModeBar': False})
                ], style={"width": "30%"})
            ], className="row", style={"padding":"5vh"}),
        label="Tokens, Words and Characters"),
        # Page 3
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Verbs', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = verbs, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Subjuntive/Imperative', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = verbs2, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Modal', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = verbs3, config={ 'displayModeBar': False})
                ], style={"width": "30%"})
            ], className="row", style={"padding":"5vh"}),
        label="Verbs"),
        # Page 4
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H4('Pronouns', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = pronouns, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H4('Singular\Second Personal', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = pronouns2, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H4('Plural First Personal', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = pronouns3, config={ 'displayModeBar': False})
                ], style={"width": "30%"})
            ], className="row", style={"padding":"5vh"} ),
        label="Pronouns"),
        # Page 5
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Adjectives', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = adjectives, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Adverbs', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = adverbs, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Nouns', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = nouns, config={ 'displayModeBar': False})
                ], style={"width": "30%"})
            ], className="row", style={"padding":"5vh"}),
        label="Adjectives, Adverbs and Nouns"),
        # Page 6
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Average Word', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = avg_word_length, config={ 'displayModeBar': False})
                ], style={"width": "40%"}),
                html.Div([
                    html.H3('Average Sentence', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = avg_sentence_length, config={ 'displayModeBar': False})
                ], style={"width": "40%"})
            ], className="row", style={"padding":"5vh"}),
        label="Word and Sentence Length"),
        # Page 7
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H3('Words in Uppercase', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = words_uppercase, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Mispelled Errors (%)', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = mispelling, config={ 'displayModeBar': False})
                ], style={"width": "30%"}),
                html.Div([
                    html.H3('Number of Links', style={"text-align" : "center"}),
                    dcc.Graph(id="dv", figure = links, config={ 'displayModeBar': False})
                ], style={"width": "30%"})
            ], className="row", style={"padding":"5vh"}),
        label="Others"),
        # Page 8
        dcc.Tab(
            html.Div([
                html.Div([
                    html.H4('Avg Sentence(x) / Diversity(y) / Words(z)', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = page1_3d, config={ 'displayModeBar': False})
                ], style={"width": "40%", "padding-right": "5vh", "padding-left": "5vh"}),
                html.Div([
                    html.H4('Characters(x) / Verbs(y) / Errors%(z)', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = page2_3d, config={ 'displayModeBar': False})
                ], style={"width": "40%"}),
            ], className="row", style={"padding":"5vh"}),
        label="3D"),
    ])
])

fig_common_words = common_words.display_chart_words(df_true, df_fake)
fig_common_bigrams = common_words.display_chart_bigrams(df_true, df_fake)

#df_true, df_fake = common_words.get_dataframes()

# Wordcloud
common_words.display_wordcloud_words()
common_words.display_wordcloud_bigrams()

page2 = html.Div([
    dcc.Tabs([
        # Words
        dcc.Tab(html.Div([
                html.Div([
                    html.H3('Most Common Words', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = fig_common_words, config={ 'displayModeBar': False})
                ])
            ], style={"padding":"5vh"}),
        label="Most Common Words"),
        # Bigrams
        dcc.Tab(html.Div([
                html.Div([
                    html.H3('Most Common Bigrams', style={"text-align" : "center"}),
                    dcc.Graph(id="em", figure = fig_common_bigrams, config={ 'displayModeBar': False})
                ])
            ], style={"padding":"5vh"}),
        label="Most Common Bigrams"),
        # Wordcloud Words
        dcc.Tab(html.Div([
                html.Div([
                    html.H3('True Words', style={"text-align" : "center"}),
                    html.Img(src="./assets/wordcloud_true_words5.png", \
                        style={"display" : "block", "margin": "auto", \
                            "max-width": "100%", "max-height" : "100%"})
                ], style={"width": "40%", "padding-right": "5vh"}),
                html.Div([
                    html.H3('Fake Words', style={"text-align" : "center"}),
                    html.Img(src="./assets/wordcloud_fake_words5.png", \
                        style={"display" : "block", "margin": "auto", \
                            "max-width": "100%", "max-height" : "100%"})
                ], style={"width": "40%"})
            ], className="row", style={"padding":"5vh"}),
        label="Most Common Words (Wordcloud)"),
        # Wordcloud Bigrams
        dcc.Tab(html.Div([
                html.Div([
                    html.H3('True Bigrams', style={"text-align" : "center"}),
                    html.Img(src="./assets/wordcloud_true_bigrams5.png", \
                        style={"display" : "block", "margin": "auto", \
                            "max-width": "100%", "max-height" : "100%"})
                ], style={"width": "40%", "padding-right": "5vh"}),
                html.Div([
                    html.H3('Fake Bigrams', style={"text-align" : "center"}),
                    html.Img(src="./assets/wordcloud_fake_bigrams5.png", \
                        style={"display" : "block", "margin": "auto", \
                            "max-width": "100%", "max-height" : "100%"})
                ], style={"width": "40%"})
            ], className="row", style={"padding":"5vh"}),
        label="Most Common Bigrams (Wordcloud)"),
    ])
])

pages = {"home"  : home,
         "page1" : page1,
         "page2" : page2}
