import pytest

from src.typographic.typographic_normalizer import TypographicNormalizer


class TypographicNormalizationTests:
    __test__ = True

    @pytest.mark.parametrize(
        "input_name, expected",
        [
            ("Monica Hirata Sant`anna", "M\u00f4nica Hirata Sant'anna"),
            ("Monica Hirata Sant\u2019anna", "M\u00f4nica Hirata Sant'anna"),
            ("M\u00f4nica Hirata Sant`anna", "M\u00f4nica Hirata Sant'anna"),
            ("Sergio Henrique Guaraldi", "S\u00e9rgio Henrique Guaraldi"),
            ("Raphael Goncalves Viana", "Raphael Gon\u00e7alves Viana"),
            ("Vanilda Cristina Junior", "Vanilda Cristina J\u00fanior"),
            ("Lilian Luiza Viana Vieira", "L\u00edlian Lu\u00edza Viana Vieira"),
        ],
    )
    def test_should_normalize_accents_cedilla_and_apostrophes(
        self,
        input_name,
        expected,
    ):
        normalizer = TypographicNormalizer()

        assert normalizer.normalize(input_name) == expected

    @pytest.mark.parametrize(
        "input_name, expected",
        [
            ("Sant`anna", "Sant'anna"),
            ("Sant\u2019anna", "Sant'anna"),
            ("Sant\u2018anna", "Sant'anna"),
            ("Sant\u00b4anna", "Sant'anna"),
        ],
    )
    def test_should_normalize_apostrophe_variants(
        self,
        input_name,
        expected,
    ):
        normalizer = TypographicNormalizer()

        assert normalizer.normalize(input_name) == expected

    @pytest.mark.parametrize(
        "input_name, expected",
        [
            ("  Sergio   Henrique   Guaraldi  ", "S\u00e9rgio Henrique Guaraldi"),
            ("Monica @ Hirata # Sant`anna!", "M\u00f4nica Hirata Sant'anna"),
            ("Raphael\tGoncalves\nViana", "Raphael Gon\u00e7alves Viana"),
        ],
    )
    def test_should_remove_special_characters_and_extra_spaces(
        self,
        input_name,
        expected,
    ):
        normalizer = TypographicNormalizer()

        assert normalizer.normalize(input_name) == expected

    @pytest.mark.parametrize("invalid_name", ["", "   "])
    def test_should_raise_when_name_is_empty(self, invalid_name):
        normalizer = TypographicNormalizer()

        with pytest.raises(ValueError):
            normalizer.normalize(invalid_name)
