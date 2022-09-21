import pytest

from districts_data import DISTRICTS, SALARY_PARAMETERS
from salary_comparison import (
    apply_proposed_raise,
    calc_career_earnings,
    calc_career_deltas,
    calc_expected_value,
    calc_overall_expected_value,
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
    salary_data = apply_proposed_raise(salary_data, district, raise_percent)
    earnings = calc_career_earnings(salary_data, DISTRICTS)
    actual = earnings[district]
    assert actual == int(expected)


@pytest.mark.parametrize(
    "deltas, insurance_deltas, expected",
    [
        ([20_000, 30_000, 50_000], [10_000, 20_000, 70_000], 33_333),
        ([1_000_000, -1_000_000], [1_000_000, -1_000_000], 0),
        ([-1_000_000, -1_000_000], [-1_000_000, -1_000_000], -1_000_000),
    ],
)
def test_expected_value(deltas, insurance_deltas, expected):
    actual = calc_expected_value(deltas, insurance_deltas)
    assert actual == expected


def test_overall_expected_value_small():
    actual = calc_overall_expected_value(["HESD", "VUSD"], "VUSD", 0)
    expected = -691792
    assert actual == expected


def test_overall_expected_value():
    actual = calc_overall_expected_value()
    expected = -336719
    assert actual == expected


def test_career_deltas_with_focus():
    actual = calc_career_deltas(
        TEST_EARNINGS,
        TEST_SAME_MONTHLY_PREMIUMS,
        "dist2",
    )
    expected = ([1_000_000, 0, -1_000_000], [1_000_000, 0, -1_000_000])
    assert actual == expected


def test_career_deltas_no_focus():
    actual = calc_career_deltas(
        TEST_EARNINGS,
        TEST_SAME_MONTHLY_PREMIUMS,
        "dist3",
        False,
    )
    expected = ([2_000_000, 1_000_000], [2_000_000, 1_000_000])
    assert actual == expected


def test_career_deltas_different_premiums():
    actual = calc_career_deltas(
        TEST_EARNINGS,
        TEST_DIFFERENT_MONTHLY_PREMIUMS,
        "dist1",
    )
    expected = ([0, -1_000_000, -2_000_000], [0, -1_004_320, -1_961_120])
    assert actual == expected
