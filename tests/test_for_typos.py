import pytest

from districts_data import SALARY_PARAMETERS


@pytest.mark.parametrize(
    "salary, district, expected",
    [
        (SALARY_PARAMETERS["Bachelor's and 30 units"], "CVUSD", 2832936),
        (SALARY_PARAMETERS["Bachelor's and 30 units"], "OUHSD", 3398180),
        (SALARY_PARAMETERS["Bachelor's and 30 units"], "VUSD", 2640309),
        (SALARY_PARAMETERS["Bachelor's and 45 units"], "OPUSD", 2834142),
        (SALARY_PARAMETERS["Bachelor's and 45 units"], "OSD", 3201259),
        (SALARY_PARAMETERS["Bachelor's and 45 units"], "OVSD", 3127890),
        (SALARY_PARAMETERS["Master's and 60 units"], "HESD", 3721746),
        (SALARY_PARAMETERS["Master's and 60 units"], "PVSD", 3166386 + 500 * 36),
        (SALARY_PARAMETERS["Master's and 60 units"], "SPUSD", 3606832),
        (SALARY_PARAMETERS["Master's and 75 units"], "RSD", 3463724),
        (SALARY_PARAMETERS["Master's and 75 units"], "FUSD", 3392456),
        (SALARY_PARAMETERS["Master's and 75 units"], "SVUSD", 3102034),
        (SALARY_PARAMETERS["Master's and 75 units"], "MUSD", 3088200),
        (SALARY_PARAMETERS["Master's and 75 units"], "VUSD", 3097190),
    ],
)
def test_earnings(salary, district, expected):
    """Confirm that \"Bachelor's and 30 units\" dataframe is constructed
    acurately
    """
    actual = salary.calc_career_earnings()[district]
    assert actual == expected
