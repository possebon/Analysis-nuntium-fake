# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from components.pages import pages

external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "13rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa",
}

CONTENT_STYLE = {
    "marginLeft": "13rem"
}

sidebar = html.Div(
    [
        html.H2("Fake News", className="display-5"),
        html.Hr(),
        html.P(
            "An interface analysis of brazilian fake news.", className="lead", style={'fontSize' : '15px'}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home",      href="/home",     id="page-1-link"),
                dbc.NavLink("Analysis",  href="/analysis-1", id="page-2-link"),
                dbc.NavLink("Common Words",  href="/analysis-2", id="page-3-link")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/" or pathname == "/home":
        # Treat page 1 as the homepage / index
        return True, False, False
    elif pathname == "/analysis-1":
        return False, True, False
    elif pathname == "/analysis-2":
        return False, False, True
    return False, False, False

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return pages['home']
    elif pathname == "/analysis-1":
        return pages['page1']
    elif pathname == "/analysis-2":
        return pages['page2']
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
