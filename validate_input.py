import logging


def validate_new_patient(r):
    """
    this function validate if the user input patient data is in the correct
    format
    :param r: test data/ user input
    :return: is_validate, boolean, True or False
    """
    is_validate = False
    try:
        is_validate = (r['patient_id']).isalpha()
        is_validate = r['patient_id'].isdigit()
    except ValueError:
        logging.error("Please enter a number")
    except AttributeError:
        logging.error("Please enter a string")
    except TypeError:
        logging.error("Please input string")

    try:
        is_validate = (r['attending_email']).isalpha()
    except ValueError:
        logging.error("Empty attending email")
    except TypeError:
        logging.error("Please input string")

    try:
        if (r['user_age']) > 0:
            is_validate = True
        else:
            logging.error("Please enter the valid age")
    except ValueError:
        logging.error("Please enter a number")
    except TypeError:
        logging.error("Please enter a number")

    return is_validate


def is_patient_id_exist(patient_id, patient_list):
    """
    this function checks if patient id exists in the patient list
    :param patient_id: string, in number
    :param patient_list: list of patient dictionaries
    :return: is_patient_id_exist, boolean
    """
    try:
        for patient in patient_list:
            if patient_id == patient['patient_id']:
                is_patient_id_exist = True
                break
            else:
                is_patient_id_exist = False
    except ValueError:
        logging.error("Please enter the valid id in string")
    return is_patient_id_exist
# if __name__ == '__main__':
#     p1 = {"patient_id": "1",
#           "attending_email": "comehelpme@bestdoc.com",
#           "user_age": 40}
#     p2 = {"patient_id": 1,
#           "attending_email": "comehelpme@bestdoc.com",
#           "user_age": "3"}
#     p3 = {"patient_id": "5",
#           "attending_email": "comehelpme@bestdoc.com",
#           "user_age": 55}
#     patient_list = [p1, p2, p3]
#     patient_id = "4"
#     out = validate_new_patient(p2)
#     print(out)
