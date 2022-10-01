import pytest
import pandas as pd

from salary import Salary
from salary_comparison import (
    calc_career_deltas,
    calc_expected_value,
    calc_overall_expected_value,
    construct_analysis_content,
    construct_hovertemplate,
)


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
TEST_CAREER_DELTAS = ([-10_000, -3_000, 0, 9_000, -2_000, 11_000, 4_000], [-8_000, -5_000, 0, 8_000, 1_000, 12_000, -7_000])


def test_hover_template(capfd):
    print(construct_hovertemplate(TEST_CAREER_DELTAS[0], TEST_CAREER_DELTAS[1], "dist1"))
    output = capfd.readouterr()[0]
    assert "$-9k to $-8k difference with dist1" in output
    assert "$3k to $5k difference with dist1" in output
    assert "$8k to $10k difference with dist1" in output
    assert "$0k difference with dist1" in output
    assert "$-1k to $2k difference with dist1" in output
    assert "$-12k to $-11k difference with dist1" in output
    assert "$-4k to $7k difference with dist1" in output


def test_analysis_content(capfd):
    """Confirm expected value, focus district, and salary parameters are displayed
    correctly
    """
    print(construct_analysis_content(-234699, 3700, TEST_SALARY, "dist1"))
    output = capfd.readouterr()[0]
    assert "dist1" in output
    assert "expected value of $-235,000" in output
    assert "expected value of $4,000" in output
    assert "Bachelor's" in output
    assert "15 units" in output


@pytest.mark.parametrize(
    "district, raise_percent, expected",
    [
        ("dist1", 3, 1_030_000),
        ("dist2", 8, 2_160_000),
        ("dist3", 11, 3_330_000),
    ],
)
def test_apply_raise(district, raise_percent, expected):
    """Confirm that the raise is being applied to the correct district and
    increases by the correct amount
    """

    actual = int(
        # SALARY_PARAMETERS["Bachelor's and 30 units"]
        TEST_SALARY.apply_proposed_raise(district, raise_percent)
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


def test_salary_repr():
    """Test __repr__ output."""
    actual = TEST_SALARY.__repr__()
    expected = (
        "Salary(salary_data=DataFrame with shape: (6, 3), degree=Bachelor's, units=15)"
    )
    assert actual == expected


def test_salary_str():
    """Test __str__ output."""
    actual = TEST_SALARY.__str__()
    expected = "Salary with a Bachelor's and 15 units."
    assert actual == expected
