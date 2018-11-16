# BME 590 Heart Rate Sentinel Server

[![Build Status](https://travis-ci.com/TinaHaitongWang/heart_rate_sentinel_server.svg?branch=master)](https://travis-ci.com/TinaHaitongWang/heart_rate_sentinel_server)

##### Author: Haitong Wang (Tina)
##### Date: Nov 15, 2018 

----

_This is a project for BME 590 Medical Device Development class. The goal of this 
project is to build a simple centralized heart rate sentinel server to allow user to post patient information 
including, patient id, age, heart rate at particular time and to get patient 
information like average heart rate, and whether the patient is tachycardic over time. This 
project features using flask to create web service, deployment on virtual machine, using sendgrid package to
send email, and basic python practice convention._

-----

**1.1 Content**

_Folders and Files Required to Run the Applications_

`bme590hrm` 
    
      |___average_heart_rate.py
 
      |___check_is_tachycardic.py 
  
      |___validate_input.py

      |___test_average_heart_rate.py
 
      |___test_check_is_tachycardic.py 
  
      |___test_validate_input.py      
      
      |___.travis.yml
      
      |___README.md
      
      |___requirement.txt
      
_Following table contains all functional files for this application_

 | Function name                             | Unit test/ Test                      |
 |-------------------------------------------|--------------------------------------|
 | average_heart_rate.py                     | test_average_heart_rate.py           |
 | check_is_tachycardic.py                   | test_check_is_tachycardic.py         |
 | validate_input.py                         | test_validate_input.py               |
 | server.py                                 | client.py                            |  
---

**1.2 Instruction for use the program**
        
        1.2.1 server.py is the main file host all activities. It is deployed on the 
              duke vm. In order to send post/get request to this server use/adapt the 
              following code, the server address is. 
              
              Please follow the format below to post and get: 
              
              POST  
                    /api/new_patient 
                        {
                          "patient_id": "1", # patient id number 
                          "attending_email": "findme@duke.edu", 
                          "user_age": 50 # in years
                        }
                    
                    /api/heart_rate
                    
                        {
                            "patient_id": "1", # patient id number 
                            "heart_rate": 100  # in bpm
                        }
                    
                    /api/heart_rate/interval_average
                        {
                            "patient_id": "1", # patient id number
                            "heart_rate_average_since": "2018-03-09 11:00:36.372339" # datetime
                        }
               
              Get 
                    /api/status/<patient_id>
                        Check if patient is having tachycardia
                    
                    /api/heart_rate/<patient_id>
                        Get patient's lastest heart rate 
                    
                    /api/heart_rate/average/<patient_id>
                        Get average of patient's heart rate untill this time
                               
        1.2.2 average_heart_rate.py, check_is_tachycardic.py, validate_input.py are 
              subfunctions used in the server.py to compute the average heart rate, 
              evaluate whether the patient is tachycardic, and validate if user has
              enter the correct input.
              
        1.2.3 Example client code 
       
```python
import requests
from random import randint
"""
this function is the client script for the server. It 
demonstrates how to correctly make post and get request to
the heart rate sentinel server."""

# make new patient post request
attending_email = "hw188@duke.edu"
user_age = [0.3, 1, 12, 19, 23, 32, 38, 41, 55, 70, 90]

for patient_id, user_age in enumerate(user_age):
    p1 = {
        "patient_id": str(patient_id +1),
        "attending_email": "hw188@duke.edu",
        "user_age": user_age,  # in years
    }
    r = requests.post("http://127.0.0.1:5000/api/new_patient", json=p1)
    print(r.text)


# post heart rate to patient
for num_heart_rate in range(20):
    for patient in range(10):
        p1 = {
            "patient_id": str(patient+1),
            "heart_rate": randint(40, 200)
        }
        r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=p1)
        print(r.text)


# get all heart rate to patient
for patient in range(10):
    r = requests.get("http://127.0.0.1:5000/api/heart_rate/{0}".format(patient+1))
    print(r.text)

# get status of patient
for patient in range(10):
    r = requests.get("http://127.0.0.1:5000/api/status/{0}".format(patient+1))
    print(r.text)

# get average heart rate of patient
for patient in range(10):
    r = requests.get("http://127.0.0.1:5000/api/heart_rate/average/{0}".format(patient+1))
    print(r.text)

# get /api/heart_rate/interval_average
for patient in range(10):
    p1 = {
            "patient_id": str(patient+1),
            "heart_rate_average_since": "2018-11-15 22:55:03"
        }
    r = requests.post("http://127.0.0.1:5000/api/heart_rate/interval_average", json=p1)
    print(r.text)

```
           
---

**1.3 Documentation for flask deployment**
        
        After log on to Virtual Machine, in command prompt, enter
        
        sudo apt-get install python3-pip screen
        pip3 install virtualenv
        git clone http 
        export SENDGRID_API_KEY='Your SENDGRID key'
        FLASK_APP=server.py flask run
        
        To test the server, open another terminal window 
        run client.py test script 
        
        
        