import pytest

from src.ids.author_id_resolver import AuthorIdResolver


@pytest.mark.parametrize(
    "records, expected",
    [
        (
            [
                {"id": 31298, "name": "Raphael Goncalves Viana"},
                {"id": 433094, "name": "Raphael Goncalves Viana"},
                {"id": 549243, "name": "Raphael Goncalves Viana"},
                {"id": 608297, "name": "Raphael Goncalves Viana"},
                {"id": 746938, "name": "Raphael Goncalves Viana"},
            ],
            [
                {"id": 31298, "name": "Raphael Goncalves Viana"},
                {"id": 31298, "name": "Raphael Goncalves Viana"},
                {"id": 31298, "name": "Raphael Goncalves Viana"},
                {"id": 31298, "name": "Raphael Goncalves Viana"},
                {"id": 31298, "name": "Raphael Goncalves Viana"},
            ],
        ),
        (
            [
                {"id": 8042, "name": "Maria Silva"},
                {"id": 97, "name": "Maria Silva"},
                {"id": 1500, "name": "Maria Silva"},
            ],
            [
                {"id": 97, "name": "Maria Silva"},
                {"id": 97, "name": "Maria Silva"},
                {"id": 97, "name": "Maria Silva"},
            ],
        ),
    ],
)
def test_should_map_same_author_to_lowest_id(records, expected):
    resolver = AuthorIdResolver()

    result = resolver.resolve(records)

    assert result == expected


def test_should_resolve_different_authors_independently():
    records = [
        {"id": 40, "name": "Ana Souza"},
        {"id": 300, "name": "Bruno Lima"},
        {"id": 12, "name": "Ana Souza"},
        {"id": 80, "name": "Bruno Lima"},
    ]

    result = AuthorIdResolver().resolve(records)

    assert result == [
        {"id": 12, "name": "Ana Souza"},
        {"id": 80, "name": "Bruno Lima"},
        {"id": 12, "name": "Ana Souza"},
        {"id": 80, "name": "Bruno Lima"},
    ]


def test_should_not_modify_original_records():
    records = [
        {"id": 20, "name": "Carla Alves"},
        {"id": 10, "name": "Carla Alves"},
    ]

    AuthorIdResolver().resolve(records)

    assert records == [
        {"id": 20, "name": "Carla Alves"},
        {"id": 10, "name": "Carla Alves"},
    ]
