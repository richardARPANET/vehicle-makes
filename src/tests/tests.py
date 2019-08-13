import pytest

from vehicle_makes import get_makes_and_models


def test_get_makes_and_models():
    result = get_makes_and_models()

    assert len(result) > 100
    assert isinstance(result, dict)
    for make in result:
        assert isinstance(result[make], tuple)
        assert all(model for model in result[make])
