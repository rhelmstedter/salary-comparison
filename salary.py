import pandas as pd
from typing import TypeVar

Salary = TypeVar("Salary")


class Salary:
    """A class to represent a teaching salary.

    :salary_data: A pandas dataframe containing the annual salary.
    :degree: The degree held by the teacher, either 'Bachelor's' or 'Master's'
    :units: The number of units held by the teacher.
    """

    def __init__(self, salary_data=pd.DataFrame, degree=str, units=int):
        """Contructs attributes for the salary object.

        :salary_data: A pandas dataframe containing the annual salary.
        :degree: The degree held by the teacher, either 'Bachelor's' or 'Master's'
        :units: The number of units held by the teacher.
        """
        self.salary_data = salary_data
        self.degree = degree
        self.units = units

    def __repr__(self) -> str:
        return f"Salary(salary_data=DataFrame with shape: {self.salary_data.shape}, degree={self.degree}, units={self.units})"

    def __str__(self) -> str:
        return f"Salary with a {self.degree} and {self.units} units."

    def apply_proposed_raise(
        self,
        focus: str,
        raise_percent: float,
    ) -> Salary:
        """Apply a proposed raise to the district of focus.

        :salary_data: The dataframe that contains all the salary data.
        :focus: The district to which the proposed raise will be applied.
        :raise_percent: The proposed raise as a percentage.

        :returns: A new Salary object with the proposed raise applied.
        """
        salary_data = self.salary_data.copy(deep=True)
        salary_data[focus] = salary_data[focus] * (1 + raise_percent / 100)

        return Salary(salary_data, self.degree, self.units)

    def calc_career_earnings(
        self,
    ) -> dict[str, int]:
        """Calculates the carreer earnings for each district.

        :salary_data: The DataFrame used to calculate the career earnings
        :districts: the list of districts to include in the calculation.
        :returns: A dictionary with keys of the district abbreviations and values of the
            carreer earnings.
        """
        districts = self.salary_data.columns
        return {
            district: int(self.salary_data[district].sum()) for district in districts
        }
