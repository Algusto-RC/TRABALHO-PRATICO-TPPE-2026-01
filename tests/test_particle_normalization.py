import pytest

from src.particles.particle_normalizer import ParticleNormalizer


@pytest.fixture
def normalizer():
    return ParticleNormalizer()


@pytest.fixture
def full_names():
    return [
        "Luiz de Oliveira de Souza",
        "Ana de Mattos Seabra"
    ]


@pytest.mark.parametrize(
    "variant, expected",
    [
        ("Luiz Oliveira Souza", "Luiz de Oliveira de Souza"),
        ("Luiz de O. de Souza", "Luiz de Oliveira de Souza"),
    ]
)
def test_should_expand_with_omitted_particles_and_dots(
    normalizer,
    full_names,
    variant,
    expected
):
    assert normalizer.expand(variant, full_names) == expected


@pytest.mark.parametrize(
    "full, variant, expected_result",
    [
        ("Luiz de Oliveira de Souza", "Luiz Oliveira Souza", True),
        ("Luiz de Oliveira de Souza", "Luiz de O. de Souza", True),
        ("Luiz de Oliveira de Souza", "Luiz de O Souza", True),
        ("Luiz de Oliveira de Souza", "Luiz de Sousa", False),
        ("Ana de Mattos Seabra", "Ana Mattos Seabra", True),
    ]
)
def test_should_match_particles_parameterized(
    normalizer,
    full,
    variant,
    expected_result
):
    assert normalizer.matches(full, variant) is expected_result


@pytest.mark.parametrize("invalid", ["", "   "])
def test_should_raise_when_name_is_empty(normalizer, full_names, invalid):
    with pytest.raises(ValueError):
        normalizer.matches(invalid, "Luiz Oliveira")

    with pytest.raises(ValueError):
        normalizer.expand(invalid, full_names)