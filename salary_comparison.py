# @title Run Analysis { run: "auto" }

import pandas as pd
from matplotlib import pyplot as plt
from typing import List, Dict
from collections import namedtuple

focus = "VUSD"  # @param ["HESD", "OVSD", "OUHSD", "OSD", "PVSD", "RSD", "SPUSD", "SVUSD", "VUSD"]
BLUE = "blue"
LIGHTGRAY = "#dddddd"
GRAY = "#bbbbbb"

ventura_df = pd.read_csv(
    "./2022-2023-Ventura.csv",
    index_col="step",
)
rio_df = pd.read_csv("./2022-2023-Rio.csv", index_col="step")
santa_paula_df = pd.read_csv(
    "./2020-2021-SantaPaula.csv",
    index_col="step",
)
oxnard_union_df = pd.read_csv(
    "./2022-2023-OxnardU.csv",
    index_col="step",
)
hueneme_df = pd.read_csv(
    "./2022-2023-Hueneme.csv",
    index_col="step",
)
ocean_view_df = pd.read_csv(
    "./2022-2023-OceanView.csv",
    index_col="step",
)
oxnard_elem_df = pd.read_csv(
    "./2022-2023-OxnardE.csv",
    index_col="step",
)
pleasant_valley_df = pd.read_csv(
    "./2022-2023-PleasantValley.csv",
    index_col="step",
)
simi_valley_df = pd.read_csv(
    "./2022-2023-SimiValley.csv",
    index_col="step",
)

DISTRICTS = [
    "HESD",
    "OVSD",
    "OUHSD",
    "OSD",
    "PVSD",
    "RSD",
    "SPUSD",
    "SVUSD",
    "VUSD",
]
bachelors_with_30: pd.DataFrame = pd.concat(
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
masters_with_60: pd.DataFrame = pd.concat(
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
masters_with_75: pd.DataFrame = pd.concat(
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


def calc_career_earnings(
    df: pd.DataFrame, districts: List[str] = DISTRICTS
) -> Dict[str, int]:
    """Calculates the carreer earnings across each district.

    :df: The DataFrame used to calculate the career earnings
    :districts: the list of districts to include in the calculation.
    :returns: A dictionary with keys of the district abbreviations and values of the
        carreer earnings.
    """
    return {district: int(df[district].sum()) for district in districts}


def calc_career_diffs(
    career_earnings: Dict[str, int],
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
    monthly_premiums = {
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
    print(
        f"This analysis assumes a teacher starts with a {degree} degree\n"
        f"with {units} units and remains in {focus} for a 36 year career.\n"
        f"The {focus} teacher makes:\n"
    )
    print(f"{career_earnings}")
    print(f"{career_premiums}")
    print(f"{career_earnings_deltas}")
    print(f"{career_earnings_deltas_insurance}")
    for district, delta, insurance_delta in zip(
        districts, career_earnings_deltas, career_earnings_deltas_insurance
    ):
        if district == focus:
            continue
        if insurance_delta < 0 and delta < 0:
            if insurance_delta == delta:
                print(f"🟥 ${abs(delta):,.0f} less than {district}.")
            else:
                print(
                    f"🟥 ${abs(insurance_delta):,.0f} to ${abs(delta):,.0f} less than {district}."
                )
        elif insurance_delta >= 0 and delta <= 0:
            print(
                f"🟧 ${abs(delta):,.0f} less to ${abs(insurance_delta):,.0f} more than {district}."
            )
        elif insurance_delta >= 0 and delta >= 0:
            if insurance_delta == delta:
                print(f"🟩 ${abs(delta):,.0f} more than {district}.")
            else:
                print(
                    f"🟩 ${abs(delta):,.0f} to ${abs(insurance_delta):,.0f} more than {district}."
                )
    print()


def plot_salaries(
    df: pd.DataFrame, districts: List[str], focus: str, degree: str, units: int
) -> None:
    """Creates and displays the plot for the salary visualization.

    :df: DataFrame that contains the salary for each district based on the parameters given.
    :districts: The list of districts to include in the plot.
    :focus: The district to highlight in blue on the chart.
    :degree: The degree held by the teacher, either Bachelor's or Master's.
    :units: The number of units obtained by the teacher.

    :returns: None
    """

    plt.style.use("fivethirtyeight")
    plt.figure(figsize=(8, 7))
    for district in districts:
        if district == focus:
            line_color = BLUE
            text_color = BLUE
            fontweight = "bold"
        else:
            line_color = LIGHTGRAY
            text_color = GRAY
            fontweight = "light"
        plt.text(
            max(df.index),
            df.loc[36, district],
            s=district,
            color=text_color,
            fontweight=fontweight,
        )
        plt.plot(df.index, df[district], color=line_color)
    plt.title(f"Career Salary with {degree} Degree and {units} units")
    plt.xlabel("Years Teaching")
    plt.ylabel("Annual Salary in Dollars")
    plt.tight_layout()
    plt.show()


SalaryParameters = namedtuple("SalaryParameters", ["degree", "dataframe", "units"])
parameter_sets = (
    SalaryParameters("Bachelor's", bachelors_with_30, 30),
    SalaryParameters("Master's", masters_with_60, 60),
    SalaryParameters("Master's", masters_with_75, 75),
)
for parameter_set in parameter_sets:
    print(f"{parameter_set.degree} Degree and {parameter_set.units} Units\n")
    career_earnings_bachelors = calc_career_earnings(parameter_set.dataframe)
    calc_career_diffs(
        career_earnings_bachelors,
        districts=DISTRICTS,
        focus=focus,
        degree=parameter_set.degree,
        units=parameter_set.units,
    )
    plot_salaries(
        parameter_set.dataframe,
        districts=DISTRICTS,
        focus=focus,
        degree=parameter_set.degree,
        units=parameter_set.units,
    )
