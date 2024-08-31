import pandas as pd

from constants import DISTRICTS
from salary import Salary


def _create_dataframe(filename: str) -> pd.DataFrame:
    """helper function to use in the salary_scales dictionary comprehension."""
    return pd.read_csv(
        f"https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/{filename}",
        index_col="step",
    )


disticts_and_files: tuple[str] = (
    ("CVUSD", "2022-2023-ConejoValley.csv"),
    ("FUSD", "2022-2023-Fillmore.csv"),
    ("HESD", "2022-2023-Hueneme.csv"),
    ("MUSD", "2022-2023-Moorpark.csv"),
    ("OPUSD", "2022-2023-OakPark.csv"),
    ("OSD", "2022-2023-OxnardE.csv"),
    ("OUHSD", "2022-2023-OxnardU.csv"),
    ("OVSD", "2022-2023-OceanView.csv"),
    ("PVSD", "2022-2023-PleasantValley.csv"),
    ("RSD", "2022-2023-Rio.csv"),
    ("SPUSD", "2022-2023-SantaPaula.csv"),
    ("SVUSD", "2022-2023-SimiValley.csv"),
    ("VUSD", "2022-2023-Ventura.csv"),
)
salary_scales: dict[str, pd.DataFrame] = {
    district: _create_dataframe(file) for district, file in disticts_and_files
}

# NOTE: The order of the dataframe columns must match the order of DISTRICTS because
# otherwise the colmun names don't align properly. Currently, both are in lexicographical
# order.
bachelors_30_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 2"],
        salary_scales["FUSD"]["class 3"],
        salary_scales["HESD"]["class 3"],
        salary_scales["MUSD"]["class 3"],
        salary_scales["OPUSD"]["class 2"],
        salary_scales["OSD"]["class 3"],
        salary_scales["OUHSD"]["class 2"],
        salary_scales["OVSD"]["class 3"],
        salary_scales["PVSD"]["class 3"],
        salary_scales["RSD"]["class 2"],
        salary_scales["SPUSD"]["class 2"],
        salary_scales["SVUSD"]["class 3"],
        salary_scales["VUSD"]["class 2"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
bachelors_45_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 3"],
        salary_scales["FUSD"]["class 4"],
        salary_scales["HESD"]["class 4"],
        salary_scales["MUSD"]["class 4"],
        salary_scales["OPUSD"]["class 3"],
        salary_scales["OSD"]["class 4"],
        salary_scales["OUHSD"]["class 3"],
        salary_scales["OVSD"]["class 4"],
        salary_scales["PVSD"]["class 4"],
        salary_scales["RSD"]["class 3"],
        salary_scales["SPUSD"]["class 3"],
        salary_scales["SVUSD"]["class 4"],
        salary_scales["VUSD"]["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
bachelors_60_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 4"],
        salary_scales["FUSD"]["class 4"],
        salary_scales["HESD"]["class 5"],
        salary_scales["MUSD"]["class 5"],
        salary_scales["OPUSD"]["class 4"],
        salary_scales["OSD"]["class 5"],
        salary_scales["OUHSD"]["class 3"],
        salary_scales["OVSD"]["class 5"],
        salary_scales["PVSD"]["class 4"],
        salary_scales["RSD"]["class 4"],
        salary_scales["SPUSD"]["class 4"],
        salary_scales["SVUSD"]["class 5"],
        salary_scales["VUSD"]["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
bachelors_75_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 4"],
        salary_scales["FUSD"]["class 5"],
        salary_scales["HESD"]["class 5"],
        salary_scales["MUSD"]["class 5"],
        salary_scales["OPUSD"]["class 5"],
        salary_scales["OSD"]["class 5"],
        salary_scales["OUHSD"]["class 3"],
        salary_scales["OVSD"]["class 5"],
        salary_scales["PVSD"]["class 4"],
        salary_scales["RSD"]["class 4"],
        salary_scales["SPUSD"]["class 5"],
        salary_scales["SVUSD"]["class 6"],
        salary_scales["VUSD"]["class 4"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_30_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 2"],
        salary_scales["FUSD"]["class 6"],
        salary_scales["HESD"]["class 4"],
        salary_scales["MUSD"]["class 6"],
        salary_scales["OPUSD"]["class 3"],
        salary_scales["OSD"]["class 3"],
        salary_scales["OUHSD"]["class 3"],
        salary_scales["OVSD"]["class 4"],
        salary_scales["PVSD"]["class 3"] + 500,
        salary_scales["RSD"]["class 5"],
        salary_scales["SPUSD"]["class 5"],
        salary_scales["SVUSD"]["class 6"],
        salary_scales["VUSD"]["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_45_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 3"],
        salary_scales["FUSD"]["class 6"],
        salary_scales["HESD"]["class 5"],
        salary_scales["MUSD"]["class 6"],
        salary_scales["OPUSD"]["class 4"],
        salary_scales["OSD"]["class 4"],
        salary_scales["OUHSD"]["class 4"],
        salary_scales["OVSD"]["class 5"],
        salary_scales["PVSD"]["class 4"] + 500,
        salary_scales["RSD"]["class 5"],
        salary_scales["SPUSD"]["class 5"],
        salary_scales["SVUSD"]["class 6"],
        salary_scales["VUSD"]["class 3"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_60_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 4"],
        salary_scales["FUSD"]["class 6"],
        salary_scales["HESD"]["class 5"],
        salary_scales["MUSD"]["class 6"],
        salary_scales["OPUSD"]["class 5"],
        salary_scales["OSD"]["class 5"],
        salary_scales["OUHSD"]["class 4"],
        salary_scales["OVSD"]["class 5"],
        salary_scales["PVSD"]["class 5"] + 500,
        salary_scales["RSD"]["class 5"],
        salary_scales["SPUSD"]["class 5"],
        salary_scales["SVUSD"]["class 6"],
        salary_scales["VUSD"]["class 4"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})
masters_75_units: pd.DataFrame = pd.concat(
    [
        salary_scales["CVUSD"]["class 5"],
        salary_scales["FUSD"]["class 6"],
        salary_scales["HESD"]["class 5"],
        salary_scales["MUSD"]["class 6"],
        salary_scales["OPUSD"]["class 5"],
        salary_scales["OSD"]["class 6"],
        salary_scales["OUHSD"]["class 4"],
        salary_scales["OVSD"]["class 5"],
        salary_scales["PVSD"]["class 5"] + 500,
        salary_scales["RSD"]["class 5"],
        salary_scales["SPUSD"]["class 5"],
        salary_scales["SVUSD"]["class 6"],
        salary_scales["VUSD"]["class 5"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: district for i, district in enumerate(DISTRICTS)})

SALARY_PARAMETERS: dict[str, Salary] = {
    "Bachelor's and 30 units": Salary(bachelors_30_units, "Bachelor's", 30),
    "Bachelor's and 45 units": Salary(bachelors_45_units, "Bachelor's", 45),
    "Bachelor's and 60 units": Salary(bachelors_60_units, "Bachelor's", 60),
    "Bachelor's and 75 units": Salary(bachelors_75_units, "Bachelor's", 75),
    "Master's and 30 units": Salary(masters_30_units, "Master's", 30),
    "Master's and 45 units": Salary(masters_45_units, "Master's", 45),
    "Master's and 60 units": Salary(masters_60_units, "Master's", 60),
    "Master's and 75 units": Salary(masters_75_units, "Master's", 75),
}
