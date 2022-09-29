from copy import deepcopy

import pytest

from districts_data import SALARY_PARAMETERS
from salary import Salary
from salary_comparison import (
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
    "district, raise_percent, expected",
    [
        ("VUSD", 3, int(2640309 * 1.03)),
        ("CVUSD", 8, int(2832936 * 1.08)),
        ("OUHSD", 11, int(3398180 * 1.11)),
    ],
)
def test_apply_raise(district, raise_percent, expected):
    """Confirm that the raise is being applied to the correct district and
    increases by the correct amount
    """

    actual = int(
        Salary(*SALARY_PARAMETERS["Bachelor's and 30 units"])
        .apply_proposed_raise(district, raise_percent)
        .salary_data[district]
        .sum()
    )
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
    """Calculate the expected value"""
    actual = calc_expected_value(deltas, insurance_deltas)
    assert actual == expected


def test_overall_expected_value():
    """Calculate the overall expected value for all districts
    with VUSD as the focus
    """
    actual = calc_overall_expected_value()
    expected = -336719
    assert actual == expected


def test_career_deltas_with_focus():
    """Calculate the pay difference using fake data.

    Monthly premiums are the same for all districts and it includes
    the focus district in the results.
    """
    actual = calc_career_deltas(
        TEST_EARNINGS,
        TEST_SAME_MONTHLY_PREMIUMS,
        "dist2",
    )
    expected = ([1_000_000, 0, -1_000_000], [1_000_000, 0, -1_000_000])
    assert actual == expected


def test_career_deltas_no_focus():
    """Calculate the pay difference using fake data.

    Monthly premiums are the same for all districts and it excludes
    the focus district in the results.
    """
    actual = calc_career_deltas(
        TEST_EARNINGS,
        TEST_SAME_MONTHLY_PREMIUMS,
        "dist3",
        False,
    )
    expected = ([2_000_000, 1_000_000], [2_000_000, 1_000_000])
    assert actual == expected


def test_career_deltas_different_premiums():
    """Calculate the pay difference using fake data.

    Monthly premiums are the different for all districts and it includes
    the focus district in the results.
    """
    actual = calc_career_deltas(
        TEST_EARNINGS,
        TEST_DIFFERENT_MONTHLY_PREMIUMS,
        "dist1",
    )
    expected = ([0, -1_000_000, -2_000_000], [0, -1_004_320, -1_961_120])
    assert actual == expected
