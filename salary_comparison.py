from statistics import mean

import plotly.graph_objects as go
from dash import html

from constants import MONTHLY_PREMIUMS
from districts_data import SALARY_PARAMETERS
from salary import Salary

TEAL = "#079A82"
LIGHTGRAY = "#eeeeee"
GRAY = "#aaaaaa"
MONTHS_PER_YEAR = 12
CAREER_LENGTH = 36


def calc_career_deltas(
    career_earnings: dict[str, int],
    monthly_premiums: dict[str, int],
    focus: str,
    include_focus: bool = True,
) -> tuple[list]:
    """Calculates the deltas in earnings across a 36 year teaching career accounting
        monthly premiums.

    :career_earnings: A dictionary with keys containing the district abbreviations and
        values of the career earnings for each district.
    :focus: The district of focus. All other earnings are subtracted from this district.
    :degree: The degree held by the teacher, either Bachelor's or Master's.
    :units: The number of units obtained by the teacher.

    :returns: The lists of deltas between the focus district and the list of districts.
        The first list accounts for opting out of insurance. The second list accounts
        for opting into insurance.
    """
    districts = career_earnings.keys()
    career_premiums = {
        district: (monthly * MONTHS_PER_YEAR * CAREER_LENGTH)
        for district, monthly in monthly_premiums.items()
    }
    if include_focus:
        career_earnings_deltas = [
            career_earnings[focus] - career_earnings[district] for district in districts
        ]
        career_earnings_deltas_insurance = [
            (career_earnings[focus] - career_premiums[focus])
            - (career_earnings[district] - career_premiums[district])
            for district in districts
        ]
    else:
        career_earnings_deltas = [
            career_earnings[focus] - career_earnings[district]
            for district in districts
            if district != focus
        ]
        career_earnings_deltas_insurance = [
            (career_earnings[focus] - career_premiums[focus])
            - (career_earnings[district] - career_premiums[district])
            for district in districts
            if district != focus
        ]
    return career_earnings_deltas, career_earnings_deltas_insurance


def calc_expected_value(
    career_earnings_deltas: list,
    career_earnings_deltas_insurance: list,
) -> int:
    """Calculates the expected value of a given district.

    :career_earnings_deltas: The list of deltas when opting out of insurance.
    :career_earnings_deltas_insurance: The list of deltas when opting in to insurance.

    :returns: The expected value rounded to the thousands place.
    """
    total_deltas = sum(
        delta + insurance_delta
        for delta, insurance_delta in zip(
            career_earnings_deltas, career_earnings_deltas_insurance
        )
    )
    expected_value = total_deltas / (2 * len(career_earnings_deltas))
    return int(expected_value)


def construct_analysis_content(
    expected_value: int,
    overall_expected_value: int,
    salary: Salary,
    focus: str,
) -> list[html.P]:
    """Contructs the anaylsis content displayed under the graphs.

    :expected_value: The expected value of an employee in the focus district.
    :overall_expected_value: The expected value across all degree types and units of an
        employee in the focus district.
    :salary: The Salary object used in the anaylsis.
    :focus: The district of focus. All other earnings are subtracted from this district.

    :returns: A list of html paragraphs that display the expected value.
    """
    analysis_content = []
    analysis_content.append(
        html.P(f"""Assuming the teacher remains in {focus} for a 36 year career:""")
    )
    analysis_content.append(
        html.P(
            f"""Lifetime earnings with a {salary.degree} degree with {salary.units} units has an expected value of ${round(expected_value,-3):,.0f}."""
        )
    )
    analysis_content.append(
        html.P(
            f"Lifetime earnings across all degree types and units has an expected value of ${round(overall_expected_value, -3):,.0f}."
        )
    )
    return analysis_content


def calc_overall_expected_value(
    focus: str = "VUSD",
    raise_percent: int = 0,
) -> int:
    """Calculates the expected value across all degree types and unitsself.

    :focus: The district of focus.
    :raise_percent: The proposed raise as a percentage.

    :returns: The overall expected value rounded to the thousands place.
    """
    expected_values = []
    for data, degree, units in SALARY_PARAMETERS.values():
        career_earnings = (
            Salary(data, degree, units)
            .apply_proposed_raise(focus, raise_percent)
            .calc_career_earnings()
        )
        deltas = calc_career_deltas(
            career_earnings,
            MONTHLY_PREMIUMS,
            focus,
            False,
        )
        expected_values.append((calc_expected_value(deltas[0], deltas[1])))
    return int(mean(item for item in expected_values))


def construct_lifetime_earnings_graph(
    salary: Salary,
    focus: str,
) -> go.Figure:
    """Constructs a horizontal barchart of lifetime earnings and displays the difference
        between a district and the focus on hover.

    :salary: The Salary object used to construct the graph.
    :focus: The district of focus. All other earnings are subtracted from this district.

    :returns: The plotly figure that contains the lifetime earnings barchart
    """
    career_earnings = salary.calc_career_earnings()
    sorted_career_earnings = dict(sorted(career_earnings.items(), key=lambda x: x[1]))
    career_deltas, career_deltas_insurance = calc_career_deltas(
        sorted_career_earnings,
        MONTHLY_PREMIUMS,
        focus,
        True,
    )
    hovertemplate = []
    for delta, insurance_delta in zip(career_deltas, career_deltas_insurance):
        if delta == insurance_delta:
            hovertemplate.append(
                f"${-1*insurance_delta/1000:.0f}k difference with {focus}"
            )
        elif insurance_delta < 0 and delta < 0:
            hovertemplate.append(
                f"${-1*insurance_delta/1000:.0f}k to ${-1*delta/1000:.0f}k difference with {focus}"
            )
        elif insurance_delta > 0 and delta < 0:
            hovertemplate.append(
                f"${-1*insurance_delta/1000:.0f}k to ${-1*delta/1000:.0f}k difference with {focus}"
            )
        elif insurance_delta > 0 and delta > 0:
            hovertemplate.append(
                f"${-1*insurance_delta/1000:.0f}k to ${-1*delta/1000:.0f}k difference with {focus}"
            )
        elif insurance_delta < 0 and delta > 0:
            hovertemplate.append(
                f"${-1*delta/1000:.0f}k to ${-1*insurance_delta/1000:.0f}k difference with {focus}"
            )
    colors = [
        LIGHTGRAY,
    ] * len(career_earnings)
    focus_index = list(sorted_career_earnings.keys()).index(focus)
    colors[focus_index] = TEAL
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=list(sorted_career_earnings.values()),
            y=list(sorted_career_earnings.keys()),
            marker_color=colors,
            name="",
            orientation="h",
            hovertemplate=hovertemplate,
        ),
    )
    fig.update_layout(
        yaxis=dict(
            title="District",
            showgrid=False,
            showline=False,
            showticklabels=True,
            domain=[0, 1],
            tickfont=dict(
                family="Lato",
                size=12,
                color="rgb(82, 82, 82)",
            ),
        ),
        xaxis=dict(
            title="Lifetime Earnings",
            tickprefix="$",
            tickfont=dict(
                family="Lato",
                size=12,
                color="rgb(82, 82, 82)",
            ),
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
        ),
        autosize=True,
        margin=dict(
            autoexpand=False,
            l=100,
            r=100,
            t=10,
        ),
        showlegend=False,
        plot_bgcolor="white",
    )
    return fig


def construct_annual_salary_graph(
    salary: Salary,
    focus: str,
) -> go.Figure:
    """Creates the line plot of the annual salary for each district.

    :salary: The Salary object used to construct the graph.
    :focus: The district to highlight in on the chart.

    :returns: The plotly figure that contains the annual salary vs years teaching
    """

    fig = go.Figure()
    annotations = []
    for district in salary.salary_data.columns:
        if district == focus:
            line_color = TEAL
            text_color = TEAL
            # label focus district only
            annotations.append(
                dict(
                    xref="paper",
                    x=1,
                    y=salary.salary_data.loc[36, district],
                    xanchor="left",
                    yanchor="middle",
                    text=f"{district}",
                    font=dict(family="Lato", size=12, color=text_color),
                    showarrow=False,
                )
            )
        else:
            line_color = LIGHTGRAY
            text_color = GRAY
        fig.add_trace(
            go.Scatter(
                x=salary.salary_data.index,
                y=salary.salary_data[district],
                line=dict(color=line_color, width=3),
                text=district,
            ),
        )
        fig.update_traces(name="")
    # style axes
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            title="Years Teaching",
            tickfont=dict(
                family="Lato",
                size=12,
                color="rgb(82, 82, 82)",
            ),
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showline=True,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            title="Annual Salary in Dollars",
            tickprefix="$",
            tickfont=dict(
                family="Lato",
                size=12,
                color="rgb(82, 82, 82)",
            ),
        ),
        autosize=True,
        margin=dict(
            autoexpand=False,
            l=100,
            r=100,
            t=110,
        ),
        showlegend=False,
        plot_bgcolor="white",
    )
    # title
    annotations.append(
        dict(
            xref="paper",
            yref="paper",
            x=0,
            y=1.10,
            xanchor="left",
            yanchor="bottom",
            text=f"{salary.degree} Degree and {salary.units} units",
            font=dict(family="Lato", size=30, color="rgb(37,37,37)"),
            showarrow=False,
        )
    )
    fig.update_layout(annotations=annotations)
    return fig


if __name__ == "__main__":
    print(calc_overall_expected_value())
