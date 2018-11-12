from check_is_tachycardic import check_tachycardic
import pytest


@pytest.mark.parametrize("age, heart_rate, expected", [
    (4, 160, "tachycardic"),
    (10, 120, "not tachycardic"),
    (0.3, 188, "tachycardic"),
])
def test_check_tachycardic(age, heart_rate, expected):
    output = check_tachycardic(age, heart_rate)
    assert output == expected
