import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html

TEAL = "#079A82"
GREEN = "#0b7a75"
RED = "rgba(171,74,67,0.6)"
LIGHTGRAY = "#eeeeee"
GRAY = "#aaaaaa"

ventura_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Ventura.csv",
    index_col="step",
)
rio_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Rio.csv",
    index_col="step",
)
santa_paula_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2020-2021-SantaPaula.csv",
    index_col="step",
)
oxnard_union_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-OxnardU.csv",
    index_col="step",
)
hueneme_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Hueneme.csv",
    index_col="step",
)
ocean_view_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-OceanView.csv",
    index_col="step",
)
oxnard_elem_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-OxnardE.csv",
    index_col="step",
)
pleasant_valley_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-PleasantValley.csv",
    index_col="step",
)
simi_valley_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-SimiValley.csv",
    index_col="step",
)

MONTHLY_PREMIUMS = {
    "HESD": 0,
    "OVSD": 350,
    "OUHSD": 180,
    "OSD": 130,
    "PVSD": 200,
    "RSD": 200,
    "SPUSD": 250,
    "SVUSD": 250,
    "VUSD": 0,
}
DISTRICTS = list(MONTHLY_PREMIUMS.keys())
bachelors_30_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 3"],
        ocean_view_df["class 3"],
        oxnard_union_df["class 2"],
        oxnard_elem_df["class 3"],
        pleasant_valley_df["class 3"],
        rio_df["class 2"],
        santa_paula_df["class 3"],
        simi_valley_df["class 3"],
        ventura_df["class 2"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
bachelors_45_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 4"],
        ocean_view_df["class 4"],
        oxnard_union_df["class 3"],
        oxnard_elem_df["class 4"],
        pleasant_valley_df["class 4"],
        rio_df["class 3"],
        santa_paula_df["class 3"],
        simi_valley_df["class 4"],
        ventura_df["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
bachelors_60_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 5"],
        ocean_view_df["class 5"],
        oxnard_union_df["class 3"],
        oxnard_elem_df["class 5"],
        pleasant_valley_df["class 4"],
        rio_df["class 4"],
        santa_paula_df["class 3"],
        simi_valley_df["class 5"],
        ventura_df["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
bachelors_75_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 5"],
        ocean_view_df["class 5"],
        oxnard_union_df["class 3"],
        oxnard_elem_df["class 5"],
        pleasant_valley_df["class 4"],
        rio_df["class 4"],
        santa_paula_df["class 3"],
        simi_valley_df["class 6"],
        ventura_df["class 4"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
masters_30_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 4"],
        ocean_view_df["class 4"],
        oxnard_union_df["class 3"],
        oxnard_elem_df["class 3"],
        pleasant_valley_df["class 3"] + 500,
        rio_df["class 5"],
        santa_paula_df["class 5"],
        simi_valley_df["class 6"],
        ventura_df["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
masters_45_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 5"],
        ocean_view_df["class 5"],
        oxnard_union_df["class 4"],
        oxnard_elem_df["class 4"],
        pleasant_valley_df["class 4"] + 500,
        rio_df["class 5"],
        santa_paula_df["class 5"],
        simi_valley_df["class 6"],
        ventura_df["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
masters_60_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 5"],
        ocean_view_df["class 5"],
        oxnard_union_df["class 4"],
        oxnard_elem_df["class 5"],
        pleasant_valley_df["class 5"] + 500,
        rio_df["class 5"],
        santa_paula_df["class 5"],
        simi_valley_df["class 6"],
        ventura_df["class 4"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})
masters_75_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 5"],
        ocean_view_df["class 5"],
        oxnard_union_df["class 4"],
        oxnard_elem_df["class 6"],
        pleasant_valley_df["class 5"] + 500,
        rio_df["class 5"],
        santa_paula_df["class 5"],
        simi_valley_df["class 6"],
        ventura_df["class 5"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})


SALARY_PARAMETERS = {
    "Bachelor's and 30 units": [bachelors_30_units, "Bachelor's", 30],
    "Bachelor's and 45 units": [bachelors_45_units, "Bachelor's", 45],
    "Bachelor's and 60 units": [bachelors_60_units, "Bachelor's", 60],
    "Bachelor's and 75 units": [bachelors_75_units, "Bachelor's", 75],
    "Master's and 30 units": [masters_30_units, "Master's", 30],
    "Master's and 45 units": [masters_45_units, "Master's", 45],
    "Master's and 60 units": [masters_60_units, "Master's", 60],
    "Master's and 75 units": [masters_75_units, "Master's", 75],
}


def apply_proposed_raise(
    df: pd.DataFrame,
    focus: str,
    raise_percent: float,
) -> pd.DataFrame:
    """Apply a proposed raise to the district in focus.

    :df: The dataframe that contains all the salary data.
    :focus: The district to which the proposed raise will be applied.
    :raise_percent: The proposed raise as a percentage.
    """
    df[focus] = df[focus] * (1 + raise_percent / 100)
    return df


def calc_career_earnings(
    df: pd.DataFrame,
    districts: list[str],
) -> dict[str, int]:
    """Calculates the carreer earnings across each district.

    :df: The DataFrame used to calculate the career earnings
    :districts: the list of districts to include in the calculation.
    :returns: A dictionary with keys of the district abbreviations and values of the
        carreer earnings.
    """
    return {district: int(df[district].sum()) for district in districts}


def construct_bar_graph(
    career_earnings: dict[str, int],
    monthly_premiums: dict[str, int],
    districts: list[str],
    focus: str,
    degree: str,
    units: int,
) -> go.Figure:
    """Calculates and displays the differnces in earnings across a 36 year teaching career.

    :career_earnings: A dictionary with keys containing the district abbreviations and
        values of the career earnings for each district.
    :districts: The list of districts to include in calculating the differences in earnings.
    :focus: The district of focus. All other earnings are subtracted from this district.
    :degree: The degree held by the teacher, either Bachelor's or Master's.
    :units: The number of units obtained by the teacher.

    :returns: None
    """
    career_premiums = {
        district: (monthly * 12 * 36) for district, monthly in monthly_premiums.items()
    }
    sorted_career_earnings = dict(sorted(career_earnings.items(), key=lambda x: x[1]))
    career_earnings_deltas = {
        district: (
            career_earnings[focus]
            - career_premiums[focus]
            - (career_earnings[district] - career_premiums[district]),
            career_earnings[focus] - career_earnings[district],
        )
        for district in sorted_career_earnings.keys()
    }
    # Creating two subplots
    fig = make_subplots(
        rows=1,
        cols=2,
        specs=[[{}, {}]],
        shared_xaxes=True,
        shared_yaxes=False,
        vertical_spacing=0.001,
    )
    colors = [
        LIGHTGRAY,
    ] * len(DISTRICTS)
    focus_index = list(sorted_career_earnings.keys()).index(focus)
    colors[focus_index] = TEAL
    # lifetime earnings
    fig.append_trace(
        go.Bar(
            x=list(sorted_career_earnings.values()),
            y=list(sorted_career_earnings.keys()),
            marker_color=colors,
            name="",
            orientation="h",
            hovertemplate=[f"${x/1_000_000:.2f}M" for x in sorted_career_earnings.values()],
        ),
        1,
        1,
    )
    # lifetime earnings deltas
    fig.append_trace(
        go.Bar(
            x=[abs(delta[0] - delta[1]) for delta in career_earnings_deltas.values()],
            y=list(sorted_career_earnings.keys()),
            base=[delta[1] for delta in career_earnings_deltas.values()],
            marker=dict(
                color=TEAL,
                line=dict(
                    color=TEAL,
                    width=1,
                ),
            ),
            name="",
            orientation="h",
            hovertemplate=[
                f"${x[0]/1000:.0f}k to ${x[1]/1000:.0f}k"
                for x in career_earnings_deltas.values()
            ],
        ),
        1,
        2,
    )
    fig.update_layout(
        yaxis=dict(
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
        yaxis2=dict(
            showgrid=False,
            showline=True,
            showticklabels=False,
            linecolor="rgba(102, 102, 102, 0.8)",
            linewidth=2,
            domain=[0, 1],
        ),
        xaxis=dict(
            title="Lifetime Earnings",
            zeroline=False,
            showline=False,
            showticklabels=True,
            tickprefix="$",
            showgrid=True,
            domain=[0, 0.45],
            tickfont=dict(
                family="Lato",
                size=12,
                color="rgb(82, 82, 82)",
            ),
        ),
        xaxis2=dict(
            title="Difference in Lifetime Earnings<br>Adjusted for Health Premiums",
            zeroline=True,
            showline=False,
            showticklabels=True,
            tickprefix="$",
            showgrid=True,
            domain=[0.50, 1],
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
            t=10,
        ),
        showlegend=False,
        plot_bgcolor="white",
    )
    annotations = []
    # # Title
    # annotations.append(
    #     dict(
    #         xref="paper",
    #         yref="paper",
    #         x=0,
    #         y=1,
    #         xanchor="left",
    #         yanchor="bottom",
    #         text="Lifetime Earnings Compared by District",
    #         font=dict(family="Lato", size=30, color="rgb(37,37,37)"),
    #         showarrow=False,
    #     )
    # )
    fig.update_layout(annotations=annotations)
    return fig


def construct_ploty_graph(
    df: pd.DataFrame,
    districts: list[str],
    focus: str,
    degree: str,
    units: int,
) -> go.Figure:
    """Creates and displays the plot for the salary visualization.

    :df: DataFrame that contains the salary for each district based on the parameters given.
    :districts: The list of districts to include in the plot.
    :focus: The district to highlight in on the chart.
    :degree: The degree held by the teacher, either Bachelor's or Master's.
    :units: The number of units obtained by the teacher.

    :returns: None
    """

    fig = go.Figure()
    annotations = []
    for district in districts:
        if district == focus:
            line_color = TEAL
            text_color = TEAL
            # Labels
            annotations.append(
                dict(
                    xref="paper",
                    x=1,
                    y=df.loc[36, district],
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
                x=df.index,
                y=df[district],
                line=dict(color=line_color, width=3),
                text=district,
            ),
        )
        fig.update_traces(name="")
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
    # Title
    annotations.append(
        dict(
            xref="paper",
            yref="paper",
            x=0,
            y=1.05,
            xanchor="left",
            yanchor="bottom",
            text=f"{degree} Degree and {units} units",
            font=dict(family="Lato", size=30, color="rgb(37,37,37)"),
            showarrow=False,
        )
    )
    fig.update_layout(annotations=annotations)
    return fig

def calc_career_diffs(
    career_earnings: dict[str, int],
    monthly_premiums: dict[str, int],
    districts: list[str],
    focus: str,
    degree: str,
    units: int,
) -> list[html.P]:
    """Calculates and displays the differnces in earnings across a 36 year teaching career.

    :career_earnings: A dictionary with keys containing the district abbreviations and
        values of the career earnings for each district.
    :districts: The list of districts to include in calculating the differences in earnings.
    :focus: The district of focus. All other earnings are subtracted from this district.
    :degree: The degree held by the teacher, either Bachelor's or Master's.
    :units: The number of units obtained by the teacher.

    :returns: None
    """
    career_premiums = {
        district: (monthly * 12 * 36) for district, monthly in monthly_premiums.items()
    }
    career_earnings_deltas = [
        career_earnings[focus] - career_earnings[district] for district in districts
    ]
    career_earnings_deltas_insurance = [
        (career_earnings[focus] - career_premiums[focus])
        - (career_earnings[district] - career_premiums[district])
        for district in districts
    ]
    career_diffs = []
    career_diffs.append(
        html.P(
            f"""This analysis assumes a teacher starts with a {degree} degree with {units} units and remains in {focus} for a 36 year career.\nThe {focus} teacher makes:\n"""
        )
    )
    for district, delta, insurance_delta in zip(
        districts, career_earnings_deltas, career_earnings_deltas_insurance
    ):
        if district == focus:
            continue
        if insurance_delta < 0 and delta < 0:
            if insurance_delta == delta:
                career_diffs.append(
                    html.P(f"🟥 ${abs(delta):,.0f} less than {district}.\n")
                )
            else:
                career_diffs.append(
                    html.P(
                        f"🟥 ${abs(insurance_delta):,.0f} to ${abs(delta):,.0f} less than {district}.\n"
                    )
                )
        elif insurance_delta >= 0 and delta <= 0:
            career_diffs.append(
                html.P(
                    f"🟧 ${abs(delta):,.0f} less to ${abs(insurance_delta):,.0f} more than {district}.\n"
                )
            )
        elif insurance_delta >= 0 and delta >= 0:
            if insurance_delta == delta:
                html.P(
                    career_diffs.append(f"🟩 ${abs(delta):,.0f} more than {district}.\n")
                )
            else:
                career_diffs.append(
                    html.P(
                        f"🟩 ${abs(delta):,.0f} to ${abs(insurance_delta):,.0f} more than {district}.\n"
                    )
                )
    return career_diffs

if __name__ == "__main__":
    df, degree, units = SALARY_PARAMETERS["Master's and 60 units"]
    career_earnings = calc_career_earnings(df, DISTRICTS, "VUSD")
    fig = construct_bar_graph(
        career_earnings, MONTHLY_PREMIUMS, DISTRICTS, "VUSD", degree, units
    )
    fig.show()
