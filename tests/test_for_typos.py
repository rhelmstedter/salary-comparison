from copy import deepcopy

import pytest

from districts_data import DISTRICTS, SALARY_PARAMETERS
from salary import Salary


@pytest.mark.parametrize(
    "district, expected",
    [
        ("CVUSD", 2832936),
        ("OUHSD", 3398180),
        ("VUSD", 2640309),
    ],
)
def test_earnings_BA_30(district, expected):
    """Confirm that \"Bachelor's and 30 units\" dataframe is constructed
    acurately
    """
    data, degree, units = SALARY_PARAMETERS["Bachelor's and 30 units"]
    salary = Salary(deepcopy(data), degree, units)
    earnings = salary.calc_career_earnings(DISTRICTS)
    actual = earnings[district]
    assert actual == expected


@pytest.mark.parametrize(
    "district, expected",
    [
        ("OPUSD", 2834142),
        ("OSD", 3201259),
        ("OVSD", 3127890),
    ],
)
def test_earnings_BA_45(district, expected):
    """Confirm that \"Bachelor's and 45 units\" dataframe is constructed
    acurately
    """
    data, degree, units = SALARY_PARAMETERS["Bachelor's and 45 units"]
    salary = Salary(deepcopy(data), degree, units)
    earnings = salary.calc_career_earnings(DISTRICTS)
    actual = earnings[district]
    assert actual == expected


@pytest.mark.parametrize(
    "district, expected",
    [
        ("HESD", 3721746),
        ("PVSD", 3166386 + 500 * 36),
        ("SPUSD", 3606832),
    ],
)
def test_earnings_MA_60(district, expected):
    """Confirm that \"Master's and 60 units\" dataframe is constructed
    acurately
    """
    data, degree, units = SALARY_PARAMETERS["Master's and 60 units"]
    salary = Salary(deepcopy(data), degree, units)
    earnings = salary.calc_career_earnings(DISTRICTS)
    actual = earnings[district]
    assert actual == expected


@pytest.mark.parametrize(
    "district, expected",
    [
        ("RSD", 3463724),
        ("FUSD", 3392456),
        ("SVUSD", 3102034),
        ("MUSD", 3088200),
        ("VUSD", 3097190),
    ],
)
def test_earnings_MA_75(district, expected):
    """Confirm that \"Master's and 75 units\" dataframe is constructed
    acurately
    """
    data, degree, units = SALARY_PARAMETERS["Master's and 75 units"]
    salary = Salary(deepcopy(data), degree, units)
    earnings = salary.calc_career_earnings(DISTRICTS)
    actual = earnings[district]
    assert actual == expected