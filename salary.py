import pandas as pd


class Salary:
    def __init__(self, salary_data, degree, units):
        self.salary_data = salary_data
        self.degree = degree
        self.units = units

    def __repr__(self):
        return f"Salary(salary_data={self.salary_data}, degree={self.degree}, units={self.units}"

    def apply_proposed_raise(
        self,
        focus: str,
        raise_percent: float,
    ) -> pd.DataFrame:
        """Apply a proposed raise to the district of focus.

        :salary_data: The dataframe that contains all the salary data.
        :focus: The district to which the proposed raise will be applied.
        :raise_percent: The proposed raise as a percentage.
        """
        self.salary_data = self.salary_data.copy(deep=True)
        self.salary_data[focus] = self.salary_data[focus] * (1 + raise_percent / 100)

    def calc_career_earnings(
        self,
        districts: list[str],
    ) -> dict[str, int]:
        """Calculates the carreer earnings for each district.

        :salary_data: The DataFrame used to calculate the career earnings
        :districts: the list of districts to include in the calculation.
        :returns: A dictionary with keys of the district abbreviations and values of the
            carreer earnings.
        """
        return {
            district: int(self.salary_data[district].sum()) for district in districts
        }
