from districts_data import SALARY_PARAMETERS, DISTRICTS, MONTHLY_PREMIUMS
import salary_comparison
import pytest


@pytest.mark.parametrize(
    "district, expected",
    [
        ("VUSD", 2640309),
        ("CVUSD", 2832936),
        ("OUHSD", 3398180),
    ],
)
def test_earnings_BA_30(district, expected):
    salary_data = SALARY_PARAMETERS["Bachelor's and 30 units"][0]
    earnings = salary_comparison.calc_career_earnings(salary_data, DISTRICTS)
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
    salary_data = SALARY_PARAMETERS["Bachelor's and 45 units"][0]
    earnings = salary_comparison.calc_career_earnings(salary_data, DISTRICTS)
    actual = earnings[district]
    assert actual == expected


@pytest.mark.parametrize(
    "district, raise_percent, expected",
    [
        ("VUSD", 3, int(2640309 * 1.03)),
        ("CVUSD", 8, int(2832936 * 1.08)),
        ("OUHSD", 11, int(3398180 * 1.11)),
    ],
)
def test_apply_raise(district, raise_percent, expected):
    salary_data = SALARY_PARAMETERS["Bachelor's and 30 units"][0]
    earnings = salary_comparison.apply_proposed_raise(salary_data, district, raise_percent)
    earnings = salary_comparison.calc_career_earnings(salary_data, DISTRICTS)
    actual = earnings[district]
    assert actual == int(expected)


# def test_overall_expected_value():
#     salary_data = SALARY_PARAMETERS["Bachelor's and 30 units"][0]
