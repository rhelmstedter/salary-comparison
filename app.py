import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import content
from districts_data import SALARY_PARAMETERS
from constants import DISTRICTS, MONTHLY_PREMIUMS
from salary_comparison import (
    calc_career_deltas,
    calc_expected_value,
    calc_overall_expected_value,
    construct_lifetime_earnings_graph,
    construct_annual_salary_graph,
    construct_analysis_content,
)

districts = [{"label": district, "value": district} for district in sorted(DISTRICTS)]
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
                            options=[{"label": f"{i}%", "value": i} for i in range(25)],
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
                salary=SALARY_PARAMETERS["Master's and 60 units"],
                focus="VUSD",
            ),
            className="card",
        ),
        dcc.Graph(
            id="bar_graph",
            figure=construct_lifetime_earnings_graph(
                SALARY_PARAMETERS.get("Master's and 60 units"),
                focus="VUSD",
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
    salary = SALARY_PARAMETERS[degree_and_units]
    salary.apply_proposed_raise(focus, raise_percent)
    return construct_annual_salary_graph(
        salary,
        focus,
    )


@app.callback(
    Output("bar_graph", "figure"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_bar_graph(degree_and_units, focus, raise_percent):
    salary = SALARY_PARAMETERS[degree_and_units]
    salary.apply_proposed_raise(focus, raise_percent)
    return construct_lifetime_earnings_graph(
        salary,
        focus,
    )


@app.callback(
    Output("career_diffs", "children"),
    Input("degree_and_units", "value"),
    Input("focus", "value"),
    Input("raise_percent", "value"),
)
def update_output_div(degree_and_units, focus, raise_percent):
    salary = SALARY_PARAMETERS[degree_and_units]
    salary.apply_proposed_raise(focus, raise_percent)
    career_earnings_deltas, career_earnings_deltas_insurance = calc_career_deltas(
        salary.calc_career_earnings(DISTRICTS),
        MONTHLY_PREMIUMS,
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
    )


if __name__ == "__main__":
    app.run_server(debug=True)
