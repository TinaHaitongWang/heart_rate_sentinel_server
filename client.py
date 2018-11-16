import requests
from random import randint
"""
this function is the client script for the server
It demonstrates how to correctly make post and get request to
the heart rate sentinel server.
this is hitting from local machine, http://127.0.0.1"""

# make new patient post request
attending_email = "hw188@duke.edu"
user_age = [0.3, 1, 12, 19, 23, 32, 38, 41, 55, 70, 90]

for patient_id, user_age in enumerate(user_age):
    p1 = {
        "patient_id": str(patient_id + 1),
        "attending_email": attending_email,
        "user_age": user_age,  # in years
    }
    r = requests.post("http://vcm-7385.vm.duke.edu:5000/api/new_patient",
                      json=p1)
    print(r.text)


# post heart rate to patient
for num_heart_rate in range(20):
    for patient in range(10):
        p1 = {
            "patient_id": str(patient + 1),
            "heart_rate": randint(40, 200)
        }
        r = requests.post("http://vcm-7385.vm.duke.edu:5000/api/heart_rate",
                          json=p1)
        print(r.text)


# get all heart rate to patient
for patient in range(10):
    r = requests.get("http://vcm-7385.vm.duke.edu:5000/api/heart_rate/{0}"
                     .format(patient+1))
    print(r.text)

# get status of patient
for patient in range(10):
    r = requests.get("http://vcm-7385.vm.duke.edu:5000/api/status/"
                     "{0}"
                     .format(patient+1))
    print(r.text)

# get average heart rate of patient
for patient in range(10):
    r = requests.get("http://vcm-7385.vm.duke.edu:5000/api/heart_rate/average/"
                     "{0}"
                     .format(patient+1))
    print(r.text)

# get /api/heart_rate/interval_average
for patient in range(10):
    p1 = {
            "patient_id": str(patient+1),
            "heart_rate_average_since": "2018-11-15 22:55:03"
        }
    r = requests.post("http://vcm-7385.vm.duke.edu:5000/api/heart_rate"
                      "/interval_average",
                      json=p1)
    print(r.text)
