import dash
from dash import html, dcc
from content import analysis_text, outro, explanation
from salary_comparison import (
    apply_proposed_raise,
    calc_career_diffs,
    calc_career_earnings,
    construct_ploty_graph,
)
from salary_comparison import DISTRICTS, MONTHLY_PREMIUMS, SALARY_PARAMETERS
from dash.dependencies import Input, Output


districts = [{"label": district, "value": district} for district in DISTRICTS]
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "VC Schools Lifetime Earnings"
app.layout = html.Div(
    [
        html.Div(
            children=[
                html.H1(children="Lifetime Earnings For Teachers", className="header-title"),
                html.P(
                    children="The estimated lifetime earnings for teachers across school districts in Ventura County, CA.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        # html.Div(dcc.Markdown(intro, className="wrapper")),
        html.Div(dcc.Markdown(analysis_text, className="wrapper")),
        html.Div(
            [
                html.Div(
                    [
                        html.Div("District", className="menu-title"),
                        dcc.Dropdown(
                            id="focus",
                            options=districts,
                            value="VUSD",
                            className="Dropdown",
                        ),
                    ],
                ),
                html.Div(
                    [
                        html.Div("Degree and Units", className="menu-title"),
                        dcc.Dropdown(
                            id="degree_and_units",
                            options=[
                                {"label": label, "value": label}
                                for label in SALARY_PARAMETERS.keys()
                            ],
                            value="Master's and 60 units",
                            className="Dropdown",
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Div("Proposed Raise", className="menu-title"),
                        dcc.Dropdown(
                            id="raise_percent",
                            options=[{"label": i, "value": i} for i in range(25)],
                            value=0,
                            className="Dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        dcc.Graph(
            id="fig1",
            figure=construct_ploty_graph(
                SALARY_PARAMETERS["Master's and 60 units"][0],
                DISTRICTS,
                focus="VUSD",
                degree="Master's",
                units=60,
            ),
            className="card",
        ),
        html.Div(id="career_diffs", className="wrapper"),
        html.Div(dcc.Markdown(explanation, className="wrapper")),
        html.Div(dcc.Markdown(outro, className="wrapper")),
    ],
    className="wrapper",
)


@app.callback(
    Output("fig1", "figure"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_graph(degree_and_units, focus, raise_percent):
    (
        df,
        degree,
        units,
    ) = SALARY_PARAMETERS[degree_and_units]
    df = apply_proposed_raise(df.copy(deep=True), focus, raise_percent)
    return construct_ploty_graph(df, DISTRICTS, focus, degree, units)


@app.callback(
    Output("career_diffs", "children"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_output_div(degree_and_units, focus, raise_percent):
    (
        df,
        degree,
        units,
    ) = SALARY_PARAMETERS[degree_and_units]
    df = apply_proposed_raise(df.copy(deep=True), focus, raise_percent)
    career_earnings = calc_career_earnings(
        df=df,
        districts=DISTRICTS,
        focus=focus,
    )
    return calc_career_diffs(
        career_earnings,
        monthly_premiums=MONTHLY_PREMIUMS,
        districts=DISTRICTS,
        focus=focus,
        degree=degree,
        units=units,
    )


if __name__ == "__main__":
    app.run_server(debug=True)
