import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import content
from districts_data import DISTRICTS, MONTHLY_PREMIUMS, SALARY_PARAMETERS
from salary_comparison import (
    apply_proposed_raise,
    calc_career_deltas,
    calc_career_earnings,
    calc_expected_value,
    calc_overall_expected_value,
    construct_lifetime_earnings_graph,
    construct_annual_salary_graph,
    construct_analysis_content,
)

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
                html.H1(
                    children="Lifetime Earnings For Teachers", className="header-title"
                ),
                html.P(
                    children="The estimated lifetime earnings for teachers across school districts in Ventura County, CA.",
                    className="header-description",
                ),
            ],
            className="header",
        ),
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
                        html.Div("Proposed Raise Percent", className="menu-title"),
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
            id="line_graph",
            figure=construct_annual_salary_graph(
                SALARY_PARAMETERS["Master's and 60 units"][0],
                DISTRICTS,
                focus="VUSD",
                degree="Master's",
                units=60,
            ),
            className="card",
        ),
        dcc.Graph(
            id="bar_graph",
            figure=construct_lifetime_earnings_graph(
                calc_career_earnings(
                    SALARY_PARAMETERS["Master's and 60 units"][0],
                    DISTRICTS,
                ),
                MONTHLY_PREMIUMS,
                DISTRICTS,
                focus="VUSD",
                degree="Master's",
                units=60,
            ),
            className="card",
        ),
        html.Div(id="career_diffs", className="wrapper"),
        html.Div(dcc.Markdown(content.updates, className="wrapper")),
        html.Div(dcc.Markdown(content.details, className="wrapper")),
        html.Div(dcc.Markdown(content.benefits, className="wrapper")),
        html.Div(dcc.Markdown(content.benefits_table, className="wrapper")),
        html.Div(dcc.Markdown(content.diff_calcs, className="wrapper")),
        html.Div(dcc.Markdown(content.outro, className="wrapper")),
    ],
    className="wrapper",
)


@app.callback(
    Output("line_graph", "figure"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_line_graph(degree_and_units, focus, raise_percent):
    (
        salary_data,
        degree,
        units,
    ) = SALARY_PARAMETERS[degree_and_units]
    salary_data = apply_proposed_raise(
        salary_data.copy(deep=True), focus, raise_percent
    )
    return construct_annual_salary_graph(salary_data, DISTRICTS, focus, degree, units)


@app.callback(
    Output("bar_graph", "figure"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_bar_graph(degree_and_units, focus, raise_percent):
    (
        salary_data,
        degree,
        units,
    ) = SALARY_PARAMETERS[degree_and_units]
    salary_data = apply_proposed_raise(
        salary_data.copy(deep=True), focus, raise_percent
    )
    career_earnings = calc_career_earnings(
        salary_data,
        DISTRICTS,
    )
    return construct_lifetime_earnings_graph(
        career_earnings,
        MONTHLY_PREMIUMS,
        DISTRICTS,
        focus,
        degree,
        units,
    )


@app.callback(
    Output("career_diffs", "children"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_output_div(degree_and_units, focus, raise_percent):
    (
        salary_data,
        degree,
        units,
    ) = SALARY_PARAMETERS[degree_and_units]
    salary_data = apply_proposed_raise(
        salary_data.copy(deep=True), focus, raise_percent
    )
    career_earnings = calc_career_earnings(
        salary_data,
        DISTRICTS,
    )
    career_earnings_deltas, career_earnings_deltas_insurance = calc_career_deltas(
        career_earnings,
        MONTHLY_PREMIUMS,
        DISTRICTS,
        focus,
        False,
    )
    expected_value = calc_expected_value(
        career_earnings_deltas,
        career_earnings_deltas_insurance,
    )
    overall_expected_value = calc_overall_expected_value(
        DISTRICTS,
        focus,
        raise_percent,
    )
    return construct_analysis_content(
        expected_value,
        overall_expected_value,
        focus,
        degree,
        units,
    )


if __name__ == "__main__":
    app.run_server(debug=True)
