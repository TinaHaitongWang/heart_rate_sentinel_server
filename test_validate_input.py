from validate_input import is_patient_id_exist, validate_new_patient, \
    validate_interval_average_input, validate_heart_rate_input

import pytest

p1 = {"patient_id": "1",
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": 40}
p2 = {"patient_id": 1,
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": "3"}
p3 = {"patient_id": "5",
      "attending_email": "cdhdh.@",
      "user_age": 55}
p4 = {"patient_id": "5",
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": -11}


@pytest.mark.parametrize("r, expected", [
    (p1, True),
    (p2, False),
    (p3, False),
    (p4, False)
])
def test_validate_new_patient(r, expected):
    output = validate_new_patient(r)
    print(output)
    assert output == expected


p1 = {"patient_id": "1",
      "heart_rate": 100}
p2 = {"patient_id": "1",
      "heart_rate": '11'}
p3 = {"patient_id": "1",
      "heart_rate": 'haha'}
p4 = {"patient_id": 'a',
      "heart_rate": 100,
      "gg": 3}
p5 = {"patient_id": 1,
      "heart_rate": 100}


@pytest.mark.parametrize("r, expected", [
    (p1, True),
    (p2, False),
    (p3, False),
    (p4, False),
    (p5, False),
])
def test_validate_heart_rate_input(r, expected):
    output = validate_heart_rate_input(r)
    assert output == expected


p1 = {"patient_id": "1",
      "heart_rate_average_since": "2018-03-09 11:00:36.372339",
      "ddd": 5757}
p2 = {"patient_id": "1",
      "heart_rate_average_since": "11:00:36.372339"}
p3 = {"patient_id": 1,
      "heart_rate_average_since": "2018-03-09 11:00:36.372339"}
p4 = {"patient_id": 'a',
      "heart_rate_average_since": "2018-03-09 11:00:36.372339"}
p5 = {"patient_id": "1",
      "heart_rate_average_since": "2018-03-09 11:00:36.372339"}


@pytest.mark.parametrize("r, expected", [
    (p1, False),
    (p2, False),
    (p3, False),
    (p4, False),
    (p5, True),
])
def test_validate_interval_average_input(r, expected):
    output = validate_interval_average_input(r)
    assert output == expected


p4 = {"patient_id": "2",
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": 30}
patient_list = [p1, p4, p3]


@pytest.mark.parametrize("patient_id, patient_list, expected", [
    ("1", patient_list, True),
    ("4", patient_list, False),
    ("12", patient_list, False),
])
def test_is_patient_id_exist(patient_id, patient_list, expected):
    output = is_patient_id_exist(patient_id, patient_list)
    assert output == expected
