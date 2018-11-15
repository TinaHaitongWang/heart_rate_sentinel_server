import requests

p1 = {
    "patient_id": "1", # usually this would be the patient MRN
    "attending_email": "hw188@duke.edu",
    "user_age": 50,  # in years
    }
r = requests.post("http://127.0.0.1:5000/api/new_patient", json=p1)
print(r.text)


p1 = {
    "patient_id": "2", # usually this would be the patient MRN
    "attending_email":  "hw188@duke.edu",
    "user_age": 50,  # in years
}
r = requests.post("http://127.0.0.1:5000/api/new_patient", json=p1)
print(r.text)

p1 = {
    "patient_id": "2", # usually this would be the patient MRN
    "heart_rate": 100
    }
r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p1)
print(r.text)

p1 = {
    "patient_id": "2", # usually this would be the patient MRN
    "heart_rate": 120
}
r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p1)
print(r.text)

p1 = {
    "patient_id": "2", # usually this would be the patient MRN
    "heart_rate": 300
}
r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p1)
print(r.text)

r = requests.get("http://127.0.0.1:5000/api/status/2")
print(r.text)