from salary import Salary
import pandas as pd

TEST_SALARY = Salary(
    pd.DataFrame(
        {
            "dist1": [500_000, 500_000, 0, 0, 0, 0],
            "dist2": [500_000, 500_000, 500_000, 500_000, 0, 0],
            "dist3": [500_000, 500_000, 500_000, 500_000, 500_000, 500_000],
        }
    ),
    "Bachelor's",
    "15",
)
TEST_EARNINGS = {
    "dist1": 1_000_000,
    "dist2": 2_000_000,
    "dist3": 3_000_000,
}
TEST_SAME_MONTHLY_PREMIUMS = {
    "dist1": 10,
    "dist2": 10,
    "dist3": 10,
}
TEST_DIFFERENT_MONTHLY_PREMIUMS = {
    "dist1": 10,
    "dist2": 0,
    "dist3": 100,
}
TEST_CAREER_DELTAS = (
    [-10_000, -3_000, 0, 9_000, -2_000, 11_000, 4_000],
    [-8_000, -5_000, 0, 8_000, 1_000, 12_000, -7_000],
)
