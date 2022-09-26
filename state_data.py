##{
import pandas as pd


df = pd.read_csv("~/code/salary-comparison/data/state_wide.csv")
ventura_county = df.where(df.Co == 56).dropna()
cols = [
    # "Co",
    "LEA",
    "total_certificated",
    "lowest_salary",
    # "lowest_column",
    # "average_salary",
    # "highest_step_new_hire",
    "highest_salary",
    # "BA_60units_step10",
    "service_days",
    "20_21_ada",
    # "20_21_percent_change",
]

ventura_county[cols].sort_values(["highest_salary"])
##}
