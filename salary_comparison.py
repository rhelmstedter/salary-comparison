import pandas as pd
from typing import List, Dict
import plotly.graph_objects as go
from dash import html

BLUE = "blue"
LIGHTGRAY = "#eeeeee"
GRAY = "#aaaaaa"

ventura_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-Ventura.csv",
    index_col="step",
)
rio_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-Rio.csv",
    index_col="step",
)
santa_paula_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2020-2021-SantaPaula.csv",
    index_col="step",
)
oxnard_union_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-OxnardU.csv",
    index_col="step",
)
hueneme_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-Hueneme.csv",
    index_col="step",
)
ocean_view_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-OceanView.csv",
    index_col="step",
)
oxnard_elem_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-OxnardE.csv",
    index_col="step",
)
pleasant_valley_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-PleasantValley.csv",
    index_col="step",
)
simi_valley_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/assets/2022-2023-SimiValley.csv",
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
    "Bachelor's with at least 30 units": [bachelors_30_units, "Bachelor's", 30],
    "Bachelor's with at least 45 units": [bachelors_45_units, "Bachelor's", 45],
    "Bachelor's with at least 60 units": [bachelors_60_units, "Bachelor's", 60],
    "Bachelor's with at least 75 units": [bachelors_75_units, "Bachelor's", 75],
    "Master's with at least 30 units": [masters_30_units, "Master's", 30],
    "Master's with at least 45 units": [masters_45_units, "Master's", 45],
    "Master's with at least 60 units": [masters_60_units, "Master's", 60],
    "Master's with at least 75 units": [masters_75_units, "Master's", 75],
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
    districts: List[str],
    focus: str,
) -> Dict[str, int]:
    """Calculates the carreer earnings across each district.

    :df: The DataFrame used to calculate the career earnings
    :districts: the list of districts to include in the calculation.
    :focus: The district to apply the raise to.
    :raise_percent: The proposed raise stored as a float.
    :returns: A dictionary with keys of the district abbreviations and values of the
        carreer earnings.
    """
    return {district: int(df[district].sum()) for district in districts}


def calc_career_diffs(
    career_earnings: Dict[str, int],
    monthly_premiums: Dict[str, int],
    districts: List[str],
    focus: str,
    degree: str,
    units: int,
) -> None:
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


def construct_ploty_graph(
    df: pd.DataFrame,
    districts: List[str],
    focus: str,
    degree: str,
    units: int,
) -> go.Figure:
    """Creates and displays the plot for the salary visualization.

    :df: DataFrame that contains the salary for each district based on the parameters given.
    :districts: The list of districts to include in the plot.
    :focus: The district to highlight in blue on the chart.
    :degree: The degree held by the teacher, either Bachelor's or Master's.
    :units: The number of units obtained by the teacher.

    :returns: None
    """

    fig = go.Figure()
    annotations = []
    for district in districts:
        if district == focus:
            line_color = BLUE
            text_color = BLUE
        else:
            line_color = LIGHTGRAY
            text_color = GRAY
        fig.add_trace(
            go.Scatter(x=df.index, y=df[district], line=dict(color=line_color, width=3))
        )
        # Labels
        annotations.append(
            dict(
                xref="paper",
                x=1,
                y=df.loc[36, district],
                xanchor="left",
                yanchor="middle",
                text=f"{district}",
                font=dict(family="Arial", size=12, color=text_color),
                showarrow=False,
            )
        )
    fig.update_layout(
        width=800,
        height=500,
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            title="Years Teaching",
            tickfont=dict(
                family="Arial",
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
            tickfont=dict(
                family="Arial",
                size=12,
                color="rgb(82, 82, 82)",
            ),
        ),
        autosize=False,
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
            x=0.0,
            y=1.05,
            xanchor="left",
            yanchor="bottom",
            text=f"Career Salary with {degree} Degree\nand {units} units",
            font=dict(family="Arial", size=30, color="rgb(37,37,37)"),
            showarrow=False,
        )
    )
    fig.update_layout(annotations=annotations)
    return fig
