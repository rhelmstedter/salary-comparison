import dash
from dash import html, dcc
from content import intro, analysis_text
from salary_comparison import (
    apply_proposed_raise,
    calc_career_diffs,
    calc_career_earnings,
    construct_ploty_graph,
)
from salary_comparison import DISTRICTS, MONTHLY_PREMIUMS, SALARY_PARAMETERS
from dash.dependencies import Input, Output


districts = [{"label": district, "value": district} for district in DISTRICTS]

app = dash.Dash()
app.layout = html.Div(
    [
        html.Div(dcc.Markdown(intro)),
        html.Div(dcc.Markdown(analysis_text)),
        html.Div(
            [
                html.H3("District"),
                dcc.Dropdown(
                    id="focus",
                    options=districts,
                    value="VUSD",
                ),
            ],
        ),
        html.Div(
            [
                html.H3("Degree and Units"),
                dcc.Dropdown(
                    id="degree_and_units",
                    options=[
                        {"label": label, "value": label}
                        for label in SALARY_PARAMETERS.keys()
                    ],
                ),
            ]
        ),
        html.Div(
            [
                html.H3("Proposed Raise"),
                dcc.Dropdown(
                    id="raise_percent",
                    options=[{"label": i, "value": i} for i in range(25)],
                    value=0,
                ),
            ]
        ),
        dcc.Graph(
            id="fig1",
            figure=construct_ploty_graph(
                SALARY_PARAMETERS["Master's with at least 60 units"][0],
                DISTRICTS,
                focus="VUSD",
                degree="Master's",
                units=60,
            ),
        ),
        html.Div(id="career_diffs"),
    ],
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
