import pandas as pd

from constants import DISTRICTS


def _create_dataframe(filename: str) -> pd.DataFrame:
    """helper function to use in the dictionary comprehension"""
    return pd.read_csv(
        f"https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/{filename}",
        index_col="step",
    )


labels_and_files = [
    ("ventura_df", "2022-2023-Ventura.csv"),
    ("rio_df", "2022-2023-Rio.csv"),
    ("santa_paula_df", "2022-2023-SantaPaula.csv"),
    ("oxnard_union_df", "2022-2023-OxnardU.csv"),
    ("hueneme_df", "2022-2023-Hueneme.csv"),
    ("ocean_view_df", "2022-2023-OceanView.csv"),
    ("oxnard_elem_df", "2022-2023-OxnardE.csv"),
    ("pleasant_valley_df", "2022-2023-PleasantValley.csv"),
    ("simi_valley_df", "2022-2023-SimiValley.csv"),
    ("conejo_valley_df", "2022-2023-ConejoValley.csv"),
    ("fillmore_df", "2022-2023-Fillmore.csv"),
    ("oak_park_df", "2022-2023-OakPark.csv"),
    ("moorpark_df", "2022-2023-Moorpark.csv"),
]


salary_scales = {label: _create_dataframe(file) for label, file in labels_and_files}

# NOTE: the order of the dataframes must match the order of the monthly premiums
bachelors_30_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 3"],
        salary_scales["ocean_view_df"]["class 3"],
        salary_scales["oxnard_union_df"]["class 2"],
        salary_scales["oxnard_elem_df"]["class 3"],
        salary_scales["pleasant_valley_df"]["class 3"],
        salary_scales["rio_df"]["class 2"],
        salary_scales["santa_paula_df"]["class 2"],
        salary_scales["simi_valley_df"]["class 3"],
        salary_scales["ventura_df"]["class 2"],
        salary_scales["conejo_valley_df"]["class 2"],
        salary_scales["fillmore_df"]["class 3"],
        salary_scales["oak_park_df"]["class 2"],
        salary_scales["moorpark_df"]["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
bachelors_45_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 4"],
        salary_scales["ocean_view_df"]["class 4"],
        salary_scales["oxnard_union_df"]["class 3"],
        salary_scales["oxnard_elem_df"]["class 4"],
        salary_scales["pleasant_valley_df"]["class 4"],
        salary_scales["rio_df"]["class 3"],
        salary_scales["santa_paula_df"]["class 3"],
        salary_scales["simi_valley_df"]["class 4"],
        salary_scales["ventura_df"]["class 3"],
        salary_scales["conejo_valley_df"]["class 3"],
        salary_scales["fillmore_df"]["class 4"],
        salary_scales["oak_park_df"]["class 3"],
        salary_scales["moorpark_df"]["class 4"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
bachelors_60_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 5"],
        salary_scales["ocean_view_df"]["class 5"],
        salary_scales["oxnard_union_df"]["class 3"],
        salary_scales["oxnard_elem_df"]["class 5"],
        salary_scales["pleasant_valley_df"]["class 4"],
        salary_scales["rio_df"]["class 4"],
        salary_scales["santa_paula_df"]["class 4"],
        salary_scales["simi_valley_df"]["class 5"],
        salary_scales["ventura_df"]["class 3"],
        salary_scales["conejo_valley_df"]["class 4"],
        salary_scales["fillmore_df"]["class 4"],
        salary_scales["oak_park_df"]["class 4"],
        salary_scales["moorpark_df"]["class 5"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
bachelors_75_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 5"],
        salary_scales["ocean_view_df"]["class 5"],
        salary_scales["oxnard_union_df"]["class 3"],
        salary_scales["oxnard_elem_df"]["class 5"],
        salary_scales["pleasant_valley_df"]["class 4"],
        salary_scales["rio_df"]["class 4"],
        salary_scales["santa_paula_df"]["class 5"],
        salary_scales["simi_valley_df"]["class 6"],
        salary_scales["ventura_df"]["class 4"],
        salary_scales["conejo_valley_df"]["class 4"],
        salary_scales["fillmore_df"]["class 5"],
        salary_scales["oak_park_df"]["class 5"],
        salary_scales["moorpark_df"]["class 5"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_30_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 4"],
        salary_scales["ocean_view_df"]["class 4"],
        salary_scales["oxnard_union_df"]["class 3"],
        salary_scales["oxnard_elem_df"]["class 3"],
        salary_scales["pleasant_valley_df"]["class 3"] + 500,
        salary_scales["rio_df"]["class 5"],
        salary_scales["santa_paula_df"]["class 5"],
        salary_scales["simi_valley_df"]["class 6"],
        salary_scales["ventura_df"]["class 3"],
        salary_scales["conejo_valley_df"]["class 2"],
        salary_scales["fillmore_df"]["class 6"],
        salary_scales["oak_park_df"]["class 3"],
        salary_scales["moorpark_df"]["class 6"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_45_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 5"],
        salary_scales["ocean_view_df"]["class 5"],
        salary_scales["oxnard_union_df"]["class 4"],
        salary_scales["oxnard_elem_df"]["class 4"],
        salary_scales["pleasant_valley_df"]["class 4"] + 500,
        salary_scales["rio_df"]["class 5"],
        salary_scales["santa_paula_df"]["class 5"],
        salary_scales["simi_valley_df"]["class 6"],
        salary_scales["ventura_df"]["class 3"],
        salary_scales["conejo_valley_df"]["class 3"],
        salary_scales["fillmore_df"]["class 6"],
        salary_scales["oak_park_df"]["class 4"],
        salary_scales["moorpark_df"]["class 6"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_60_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 5"],
        salary_scales["ocean_view_df"]["class 5"],
        salary_scales["oxnard_union_df"]["class 4"],
        salary_scales["oxnard_elem_df"]["class 5"],
        salary_scales["pleasant_valley_df"]["class 5"] + 500,
        salary_scales["rio_df"]["class 5"],
        salary_scales["santa_paula_df"]["class 5"],
        salary_scales["simi_valley_df"]["class 6"],
        salary_scales["ventura_df"]["class 4"],
        salary_scales["conejo_valley_df"]["class 4"],
        salary_scales["fillmore_df"]["class 6"],
        salary_scales["oak_park_df"]["class 5"],
        salary_scales["moorpark_df"]["class 6"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_75_units: pd.DataFrame = pd.concat(
    [
        salary_scales["hueneme_df"]["class 5"],
        salary_scales["ocean_view_df"]["class 5"],
        salary_scales["oxnard_union_df"]["class 4"],
        salary_scales["oxnard_elem_df"]["class 6"],
        salary_scales["pleasant_valley_df"]["class 5"] + 500,
        salary_scales["rio_df"]["class 5"],
        salary_scales["santa_paula_df"]["class 5"],
        salary_scales["simi_valley_df"]["class 6"],
        salary_scales["ventura_df"]["class 5"],
        salary_scales["conejo_valley_df"]["class 5"],
        salary_scales["fillmore_df"]["class 6"],
        salary_scales["oak_park_df"]["class 5"],
        salary_scales["moorpark_df"]["class 6"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})

SALARY_PARAMETERS = {
    "Bachelor's and 30 units": (bachelors_30_units, "Bachelor's", 30),
    "Bachelor's and 45 units": (bachelors_45_units, "Bachelor's", 45),
    "Bachelor's and 60 units": (bachelors_60_units, "Bachelor's", 60),
    "Bachelor's and 75 units": (bachelors_75_units, "Bachelor's", 75),
    "Master's and 30 units": (masters_30_units, "Master's", 30),
    "Master's and 45 units": (masters_45_units, "Master's", 45),
    "Master's and 60 units": (masters_60_units, "Master's", 60),
    "Master's and 75 units": (masters_75_units, "Master's", 75),
}

if __name__ == "__main__":
    pass
