import pytest

from src.initials.initials_matcher import InitialsMatcher


@pytest.mark.parametrize(
    "full_name, abbreviated, expected",
    [
        ("Ana de Mattos Seabra", "Seabra A. M.", True),
        ("Ana de Mattos Seabra", "Seabra A M", True),
        ("Ana de Mattos Seabra", "Seabra AM", True),
        ("Cassius de Souza", "Souza C.", True),
        ("Cassius de Souza", "Souza C", True),

        ("Ana de Mattos Seabra", "Seabra A.", False),
        ("Ana de Mattos Seabra", "Souza A. M.", False),
        ("Cassius de Souza", "Souza A.", False),
    ],
)
def test_should_match_full_name_with_abbreviation(
    full_name,
    abbreviated,
    expected,
):
    matcher = InitialsMatcher()

    assert matcher.matches(full_name, abbreviated) is expected


@pytest.mark.parametrize(
    "abbreviated, full_names, expected",
    [
        (
            "Seabra A. M.",
            [
                "Ana de Mattos Seabra",
                "Cassius de Souza",
            ],
            "Ana de Mattos Seabra",
        ),
        (
            "Souza C.",
            [
                "Ana de Mattos Seabra",
                "Cassius de Souza",
            ],
            "Cassius de Souza",
        ),
        (
            "Seabra AM",
            [
                "Cassius de Souza",
                "Ana de Mattos Seabra",
            ],
            "Ana de Mattos Seabra",
        ),
    ],
)
def test_should_expand_abbreviation_to_full_name(
    abbreviated,
    full_names,
    expected,
):
    matcher = InitialsMatcher()

    assert matcher.expand(abbreviated, full_names) == expected


def test_should_return_none_when_no_full_name_matches():
    matcher = InitialsMatcher()

    result = matcher.expand(
        "Lima R.",
        [
            "Ana de Mattos Seabra",
            "Cassius de Souza",
        ],
    )

    assert result is None


def test_should_ignore_accents_on_comparison():
    matcher = InitialsMatcher()

    assert matcher.matches("Sérgio Henrique Guaraldi", "Guaraldi S. H.")


@pytest.mark.parametrize("invalid", ["", "   "])
def test_should_raise_when_name_is_empty(invalid):
    matcher = InitialsMatcher()

    with pytest.raises(ValueError):
        matcher.matches(invalid, "Souza C.")

    with pytest.raises(ValueError):
        matcher.matches("Cassius de Souza", invalid)
