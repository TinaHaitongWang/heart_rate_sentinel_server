from flask import Flask, jsonify, request
import os
import sendgrid
import datetime
import logging
from validate_input import validate_new_patient
from check_is_tachycardic import check_tachycardic
from average_heart_rate import find_average_heart_rate
import timestring

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

    def __init__(self, patient_id, attending_email, user_age):
        self.patient_id = patient_id
        self.attending_email = attending_email
        self.user_age = user_age
        self.heart_rate = []
        self.heart_rate_time = []
        self.heart_rate_average_since = []

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
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
        p = Patient(r['patient_id'], r['attending_email'], r['user_age'])
        patient_list.append(p.to_dict())
        result = {
            "message": "Added patient {0} successfully to the "
                       "patient list".format(request.json["patient_id"])
        }

    except KeyError as error:
        logging.error(error)
        return jsonify({"message": error}), 500
    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def add_patient_heart_rate():
    """
    this function allow user to post heart rate data to designated patient
    :return: message whether this is successfully implemented
    """
    r = request.get_json()
    # add try and exception block to validate the user input from request
    try:
        for patient in patient_list:
            if r['patient_id'] == patient.get('patient_id'):
                patient.get('heart_rate').append(r['heart_rate'])
                patient.get('heart_rate_time').append(datetime.datetime.now())

    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500

    return jsonify({"message": "Added heart rate successfully to the patient "
                               "{0}".format(request.json["patient_id"])})


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def post_interval_average():
    """
    this method allow user to post a time and to calculate the
    average heart rate since that time for designated patient
    :return: whether it is successfully calculated the average
    heart rate for the patient
    """
    r = request.get_json()
    try:
        for patient in patient_list:
            if r['patient_id'] == patient.get('patient_id'):
                patient.get('heart_rate_average_since') \
                    .append(r['heart_rate_average_since'])
                index_time_since = [index for index, time in enumerate(
                    patient.get('heart_rate_time'))
                                    if time < timestring.
                                    Date(r['heart_rate_average_since']).date]
                list_heart_rate = []
                for n in index_time_since:
                    list_heart_rate.append(patient.get('heart_rate')[n])
                average_heartrate = find_average_heart_rate(list_heart_rate)

        return jsonify({"message": "Patient {0} average heart rate since {1} "
                                   "is {2}"
                       .format(r['patient_id'], r['heart_rate_average_since'],
                               average_heartrate)})
    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500


@app.route("/api/status/<patient_id>", methods=['GET'])
def get_status(patient_id):
    """
    This method allow user to get the status of designated
    patient, whether the patient is tachycardic or not
    :param patient_id: string, patient id number
    :return: whether it is successfully find the patient to
    be tachycardic or not, under the condition when the
    patient is tachycardic, the system will send a email to
    the attending doctor
    """
    is_tachycardic = False
    try:
        for patient in patient_list:
            if patient_id == patient.get('patient_id'):
                latest_heart_rate = patient.get('heart_rate')[-1]
                is_tachycardic = check_tachycardic(patient.get('user_age'),
                                                   latest_heart_rate)

                if is_tachycardic == "tachycardic":
                    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get(
                        'SENDGRID_API_KEY'))
                    from_email = "SOS@tachycardic.com"
                    to_email = patient.get('attending_email')
                    subject = "Your patient has tachycardia"
                    content = "Patient id {0} had tachycardia at {1}" \
                        .format(patient_id, patient.get('heart_rate_time')[-1])
                    data = {
                        "personalizations": [
                            {
                                "to": [
                                    {
                                        "email": to_email
                                    }
                                ],
                                "subject": subject
                            }
                        ],
                        "from": {
                            "email": from_email
                        },
                        "content": [
                            {
                                "type": "text/plain",
                                "value": content
                            }
                        ]
                    }
                    response = sg.client.mail.send.post(request_body=data)
                    print(response.status_code)

        return jsonify("patient {0} is {1}".format(patient_id, is_tachycardic))

    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500


@app.route("/api/heart_rate/<patient_id>", methods=['GET'])
def get_patient_heart_rate(patient_id):
    """
    this method allow user to retrieve all heart rate
    of a patient
    :param patient_id: string, patient id number
    :return: whether it the patient exist or successfully
    locate the information
    """
    try:
        for patient in patient_list:
            if patient_id == patient.get('patient_id'):
                list_heart_rate = patient.get('heart_rate')
        return jsonify(list(list_heart_rate))
    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500


@app.route("/api/heart_rate/average/<patient_id>", methods=['GET'])
def get_average_heart_rate(patient_id):
    """
    this method allow user to computer the latest average heart
    rate of a patient
    :param patient_id: string, patient id number
    :return:
    """
    try:
        for patient in patient_list:
            if patient_id == patient.get('patient_id'):
                average_heart_rate = find_average_heart_rate(
                    patient.get('heart_rate'))

        return jsonify("patient {0}'s average heart rate is {1} bpm"
                       .format(patient_id, average_heart_rate))
    except KeyError as error:
        logging.error(error)
        return jsonify({"message": "Error occurred, check your inputs"}), 500


if __name__ == '__main__':
    app.run(host="127.0.0.1")
