import pandas as pd
from constants import DISTRICTS


ventura_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Ventura.csv",
    index_col="step",
)
rio_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Rio.csv",
    index_col="step",
)
santa_paula_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-SantaPaula.csv",
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
conejo_valley_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-ConejoValley.csv",
    index_col="step",
)
fillmore_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Fillmore.csv",
    index_col="step",
)
oak_park_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-OakPark.csv",
    index_col="step",
)
moorpark_df = pd.read_csv(
    "https://raw.githubusercontent.com/rhelmstedter/salary-comparison/main/data/2022-2023-Moorpark.csv",
    index_col="step",
)

bachelors_30_units: pd.DataFrame = pd.concat(
    [
        hueneme_df["class 3"],
        ocean_view_df["class 3"],
        oxnard_union_df["class 2"],
        oxnard_elem_df["class 3"],
        pleasant_valley_df["class 3"],
        rio_df["class 2"],
        santa_paula_df["class 2"],
        simi_valley_df["class 3"],
        ventura_df["class 2"],
        conejo_valley_df["class 2"],
        fillmore_df["class 3"],
        oak_park_df["class 2"],
        moorpark_df["class 3"],
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
        conejo_valley_df["class 3"],
        fillmore_df["class 4"],
        oak_park_df["class 3"],
        moorpark_df["class 4"],
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
        santa_paula_df["class 4"],
        simi_valley_df["class 5"],
        ventura_df["class 3"],
        conejo_valley_df["class 4"],
        fillmore_df["class 4"],
        oak_park_df["class 4"],
        moorpark_df["class 5"],
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
        santa_paula_df["class 5"],
        simi_valley_df["class 6"],
        ventura_df["class 4"],
        conejo_valley_df["class 4"],
        fillmore_df["class 5"],
        oak_park_df["class 5"],
        moorpark_df["class 5"],
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
        conejo_valley_df["class 2"],
        fillmore_df["class 6"],
        oak_park_df["class 3"],
        moorpark_df["class 6"],
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
        conejo_valley_df["class 3"],
        fillmore_df["class 6"],
        oak_park_df["class 4"],
        moorpark_df["class 6"],
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
        conejo_valley_df["class 4"],
        fillmore_df["class 6"],
        oak_park_df["class 5"],
        moorpark_df["class 6"],
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
        conejo_valley_df["class 5"],
        fillmore_df["class 6"],
        oak_park_df["class 5"],
        moorpark_df["class 6"],
    ],
    axis=1,
    ignore_index=True,
).rename(columns={i: DISTRICTS[i] for i in range(len(DISTRICTS))})

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
