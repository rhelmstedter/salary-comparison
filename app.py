import dash
import plotly.graph_objects as go
from dash import dcc, html
from dash.dependencies import Input, Output

import content
from constants import DISTRICTS, MONTHLY_PREMIUMS
from districts_data import SALARY_PARAMETERS
from salary import Salary
from salary_comparison import (
    calc_career_deltas,
    calc_expected_value,
    calc_overall_expected_value,
    construct_analysis_content,
    construct_annual_salary_graph,
    construct_lifetime_earnings_graph,
)

default_salary: Salary = SALARY_PARAMETERS["Master's and 60 units"]

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Teacher Salaries Ventura County"
app.layout = html.Div(
    [
        html.Div(
            children=[
                html.H1(
                    children="Teacher Salaries in Ventura County", className="header-title"
                ),
                html.P(
                    children="The estimated lifetime earnings for teachers in Ventura County, CA.",
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
                            options=DISTRICTS,
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
                salary=default_salary,
                focus="VUSD",
            ),
            className="card",
        ),
        dcc.Graph(
            id="bar_graph",
            figure=construct_lifetime_earnings_graph(
                salary=default_salary,
                focus="VUSD",
            ),
            className="card",
        ),
        html.Div(id="career_diffs", className="wrapper"),
        html.Div(dcc.Markdown(content.details, className="wrapper")),
        html.Div(dcc.Markdown(content.diff_calcs, className="wrapper")),
        html.Div(dcc.Markdown(content.benefits, className="wrapper")),
        html.Div(dcc.Markdown(content.benefits_table, className="wrapper")),
        html.Div(dcc.Markdown(content.updates, className="wrapper")),
        html.Div(dcc.Markdown(content.outro, className="wrapper")),
    ],
    className="wrapper",
)


@app.callback(
    [
        Output("bar_graph", "figure"),
        Output("line_graph", "figure"),
        Output("career_diffs", "children"),
    ],
    [
        Input("degree_and_units", "value"),
        Input("focus", "value"),
        Input("raise_percent", "value"),
    ],
)
def update_layout(
    degree_and_units: str, focus: str, raise_percent: int
) -> tuple[go.Figure, list[html.P]]:
    """Updates the graphs and the expected value calculations based on the
    selections from the dropdown menus

    :degree_and_units: The string used as a key for the SALARY_PARAMETERS dict.
    :focus: The district of focus. Is highlights on the graph and used to calculate
        expected value.
    :raise_percent: The integer used to apply a raise percent.

    :returns: The bar graph, the line graph, and the expected value analysis content.
    """
    salary = SALARY_PARAMETERS[degree_and_units].apply_proposed_raise(
        focus, raise_percent
    )
    bar_graph = construct_lifetime_earnings_graph(
        salary,
        focus,
    )
    line_graph = construct_annual_salary_graph(
        salary,
        focus,
    )
    career_earnings_deltas, career_earnings_deltas_insurance = calc_career_deltas(
        salary.calc_career_earnings(),
        MONTHLY_PREMIUMS,
        focus,
        False,
    )
    expected_value = calc_expected_value(
        career_earnings_deltas,
        career_earnings_deltas_insurance,
    )
    overall_expected_value = calc_overall_expected_value(
        focus,
        raise_percent,
    )
    analysis_content = construct_analysis_content(
        expected_value,
        overall_expected_value,
        salary,
        focus,
    )
    return bar_graph, line_graph, analysis_content


if __name__ == "__main__":
    app.run_server(debug=True)
