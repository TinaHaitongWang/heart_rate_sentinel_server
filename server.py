from flask import Flask, jsonify, request
import os
import sendgrid
import datetime
import logging

"""
    This is the serve for this heart rate 
    sentinel serve project 
"""

app = Flask(__name__)
patient_list = []

class Patient(object):
    """
    this is a class for new patient with arguments of patient id,
    attending_email, user_age, and a list of heart_rate with time
    """
    def __int__(self, patient_id, attending_email, user_age, heart_rate=None,
                heart_rate_time=None, heart_rate_average_since=None):
        self.patient_id = patient_id
        self.attending_email = attending_email
        self.user_age = user_age
        self.heart_rate = []
        self.heart_rate_time = []
        self.heart_rate_average_since = []

    def to_dict(self):
        return{
            "patient_ide": self.patient_id,
            "attending_email": self.attending_email,
            "user_age": self.user_age,
            "heart_rate": self.heart_rate,
            "heart_rate_time": self.heart_rate_time,
            "heart_rate_average_since": self.heart_rate_average_since
        }


@app.route("/api/new_patient", methods=["POST"])
def add_patient():
    """
    this function add new patient from user post
    :return: verfied result
    """
    r = request.get_json()

    try:
        validate_new_patient(r)
    except ValidationError as inst:
        return jsonify({"message": inst.message}), 500

    p = Patient(r['patient_id'], r['attending_email'], r['user_age'])
    patient_list.append(p.to_dict())
    result = {
        "message": "Added user {0} successfully to the class list".format(request.json["patient_id"])
    }
    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def add_patient_heart_rate():
    r = request.get_json()
    # add try and exception block to validate the user input from request
    try:
        is_patient_id_exist(r['patient_id'])
        for patient in patient_list:
            if r['patient_id'] == patient.get('patient_ide'):
                patient.get('heart_rate').append(r['heart_rate'])
                patient.get('heart_rate_time').append(datetime.datetime.now())

    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500

    return jsonify({"message": "Added heart rate successfully to the patient {0}".format(request.json["patient_id"])})


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def post_interval_average():
    r = request.get_json()
    try:
        is_patient_id_exist(r['patient_id'])
        for patient in patient_list:
            if r['patient_id'] == patient.get('patient_ide'):
                patient['heart_rate_average_since'] = r['heart_rate_average_since']
    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500

    return jsonify({"message": "Added heart rate average time successfully to the patient {0}"
                   .format(request.json["patient_id"])})


@app.route("/api/status/<patient_id>", methods=['GET'])
def get_status(patient_id):
    for patient in patient_list:
        if patient_id == patient.get('patient_ide'):
            latest_heart_rate = patient.get('heart_rate')[-1]
            is_tachycardic = check_tachycardic(patient.user_age, latest_heart_rate)

    return {"patient is {} at {}".format(is_tachycardic, patient.get['heart_rate_time'][-1])}


@app.route("/api/heart_rate/<patient_id>", methods=['GET'])
def get_patient_heart_rate(patient_id):
    for patient in patient_list:
        if patient_id == patient.get('patient_ide'):
            list_heart_rate = patient.get('heart_rate')
    return jsonify(list_heart_rate)


@app.route("/api/heart_rate/average/<patient_id>", methods=['GET'])
def get_average_heart_rate(patient_id):
    for patient in patient_list:
        if patient_id == patient.get('patient_ide'):
            average_heart_rate = find_average_heart_rate(patient.get('heart_rate'))

    return jsonify(average_heart_rate)
















