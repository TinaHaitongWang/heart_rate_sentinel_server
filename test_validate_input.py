from validate_input import is_patient_id_exist, validate_new_patient
import pytest

p1 = {"patient_id": "1",
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": 40}
p2 = {"patient_id": 1,
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": "3"}
p3 = {"patient_id": "5",
      "attending_email": "comehelpme@bestdoc.com",
      "user_age": 55}


@pytest.mark.parametrize("r, expected", [
    (p1, True),
    (p2, False),
    (p3, True),
])
def test_validate_new_patient(r, expected):
    output = validate_new_patient(r)
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
