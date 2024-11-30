import pytest

from rules_engine.rules_engine import calculate_supplement


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            {
                "id": "test1",
                "numberOfChildren": 2,
                "familyComposition": "single",
                "familyUnitInPayForDecember": False,
            },
            {
                "id": "test1",
                "isEligible": False,
                "baseAmount": 0.0,
                "childrenAmount": 0.0,
                "supplementAmount": 0.0,
            },
        ),
        (
            {
                "id": "test2",
                "numberOfChildren": 0,
                "familyComposition": "single",
                "familyUnitInPayForDecember": True,
            },
            {
                "id": "test2",
                "isEligible": True,
                "baseAmount": 60.0,
                "childrenAmount": 0.0,
                "supplementAmount": 60.0,
            },
        ),
        (
            {
                "id": "test3",
                "numberOfChildren": 0,
                "familyComposition": "couple",
                "familyUnitInPayForDecember": True,
            },
            {
                "id": "test3",
                "isEligible": True,
                "baseAmount": 120.0,
                "childrenAmount": 0.0,
                "supplementAmount": 120.0,
            },
        ),
        (
            {
                "id": "test4",
                "numberOfChildren": 3,
                "familyComposition": "single",
                "familyUnitInPayForDecember": True,
            },
            {
                "id": "test4",
                "isEligible": True,
                "baseAmount": 60.0,
                "childrenAmount": 60.0,
                "supplementAmount": 120.0,
            },
        ),
        (
            {
                "id": "test5",
                "numberOfChildren": 2,
                "familyComposition": "couple",
                "familyUnitInPayForDecember": True,
            },
            {
                "id": "test5",
                "isEligible": True,
                "baseAmount": 120.0,
                "childrenAmount": 40.0,
                "supplementAmount": 160.0,
            },
        ),
        (
            {
                "id": "test5",
                "numberOfChildren": 2,
                "familyComposition": "",
                "familyUnitInPayForDecember": True,
            },
            {
                "id": "test5",
                "isEligible": True,
                "baseAmount": 0.0,
                "childrenAmount": 0.0,
                "supplementAmount": 0.0,
            },
        ),
        (
            {
                "id": "test5",
                "numberOfChildren": 2,
                "familyComposition": "",
                "familyUnitInPayForDecember": False,
            },
            {
                "id": "test5",
                "isEligible": False,
                "baseAmount": 0.0,
                "childrenAmount": 0.0,
                "supplementAmount": 0.0,
            },
        ),
    ],
)
def test_calculate_supplement(input_data, expected_output):
    """Using paramaterized testing to test the calculate_supplement function"""
    result = calculate_supplement(input_data)
    assert result == expected_output
