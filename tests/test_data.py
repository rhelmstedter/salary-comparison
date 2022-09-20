import pytest

from districts_data import DISTRICTS, SALARY_PARAMETERS
from salary_comparison import (
    apply_proposed_raise,
    calc_career_earnings,
    calc_overall_expected_value,
)


@pytest.mark.parametrize(
    "district, expected",
    [
        ("CVUSD", 2832936),
        ("OUHSD", 3398180),
        ("VUSD", 2640309),
    ],
)
def test_earnings_BA_30(district, expected):
    salary_data = SALARY_PARAMETERS["Bachelor's and 30 units"][0]
    earnings = calc_career_earnings(salary_data, DISTRICTS)
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
    earnings = calc_career_earnings(salary_data, DISTRICTS)
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
    salary_data = SALARY_PARAMETERS["Master's and 60 units"][0]
    earnings = calc_career_earnings(salary_data, DISTRICTS)
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
    salary_data = SALARY_PARAMETERS["Master's and 75 units"][0]
    earnings = calc_career_earnings(salary_data, DISTRICTS)
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
    earnings = apply_proposed_raise(salary_data, district, raise_percent)
    earnings = calc_career_earnings(salary_data, DISTRICTS)
    actual = earnings[district]
    assert actual == int(expected)


def test_overall_expected_value_small():
    actual = calc_overall_expected_value(["HESD", "VUSD"], "VUSD", 0)
    expected = -682000
    assert actual == expected


def test_overall_expected_value_all():
    actual = calc_overall_expected_value()
    expected = -337000
    assert actual == expected
