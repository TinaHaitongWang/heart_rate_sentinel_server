from average_heart_rate import find_average_heart_rate
import pytest
heart_rate1 = [155, 167, 178, 196, 133, 145, 124]
heart_rate2 = [133, 134, 120, 110, 97, 123]
heart_rate3 = [166, 100, 177, 155, 144, 156, 178, 167, 179, 156]


@pytest.mark.parametrize("heart_rate, expected", [
    (heart_rate1, 157),
    (heart_rate2, 120),
    (heart_rate3, 158)
])
def test_check_aveg_heart_rate(heart_rate, expected):
    output = find_average_heart_rate(heart_rate)
    assert round(output) == expected
