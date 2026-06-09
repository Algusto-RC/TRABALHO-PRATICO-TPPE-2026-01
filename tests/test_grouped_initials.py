import pytest

from src.groupedinitials.grouped_initials_matcher import (
    GroupedInitialsMatcher
)


@pytest.mark.parametrize(
    "abbreviated, full_names, expected",
    [

        (
            "VC Junior",
            [
                "Vanilda Cristina Junior",
                "Sérgio Henrique Guaraldi",
                "Mônica Hirata Sant'anna"
            ],
            "Vanilda Cristina Junior"
        ),

        (
            "SH Guaraldi",
            [
                "Vanilda Cristina Junior",
                "Sérgio Henrique Guaraldi",
                "Mônica Hirata Sant'anna"
            ],
            "Sérgio Henrique Guaraldi"
        ),

        (
            "MHS Sant'anna",
            [
                "Vanilda Cristina Junior",
                "Sérgio Henrique Guaraldi",
                "Mônica Hirata Sant'anna"
            ],
            "Mônica Hirata Sant'anna"
        ),

        (
            "SH Guaraldi",
            [
                "Sergio Henrique Guaraldi"
            ],
            "Sergio Henrique Guaraldi"
        ),
    ]
)
def test_should_expand_grouped_initials(
    abbreviated,
    full_names,
    expected
):

    matcher = GroupedInitialsMatcher()

    result = matcher.expand(
        abbreviated,
        full_names
    )

    assert result == expected


def test_should_return_none_when_no_match_found():

    matcher = GroupedInitialsMatcher()

    result = matcher.expand(
        "AB Silva",
        [
            "Carlos Souza",
            "Maria Oliveira"
        ]
    )

    assert result is None


def test_should_ignore_accents():

    matcher = GroupedInitialsMatcher()

    result = matcher.expand(
        "SH Guaraldi",
        [
            "Sérgio Henrique Guaraldi"
        ]
    )

    assert result == "Sérgio Henrique Guaraldi"
