# BME 590 heart_rate_sentinel_server

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

 | Function name                             | Unit test                            |
 |-------------------------------------------|--------------------------------------|
 | average_heart_rate.py                     | test_average_heart_rate.py           |
 | check_is_tachycardic.py                   | test_check_is_tachycardic.py         |
 | validate_input.py                         | test_validate_input.py               |
 | server.py                                 |                                      |  
---

**1.2 Instruction for use the program**

   

---
