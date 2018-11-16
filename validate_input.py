import logging
import datetime


def validate_new_patient(r):
    """
    this function validate if the user input patient data is in the correct
    format
    :param r: test data/ user input
    :return: is_validate, boolean, True or False
    """
    is_validate = [False, False, False, False, False]
    try:
        is_validate[0] = r['patient_id'].isdigit()
        if len(r) == 3:
            is_validate[1] = True
        else:
            is_validate[1] = False
    except ValueError:
        logging.error("Please enter a number")
    except AttributeError:
        logging.error("Please enter a string")
    except TypeError:
        logging.error("Please input string")

    try:
        for index, char in enumerate(r['attending_email']):
            if char == '@':
                index1 = index
            elif char == '.':
                index2 = index

        if index1 < index2:
            is_validate[2] = True
        else:
            is_validate[2] = False

    except ValueError:
        logging.error("Empty attending email")
    except TypeError:
        logging.error("Please input string")

    try:
        if (r['user_age']) > 0:
            is_validate[3] = True
        else:
            is_validate[3] = False
            logging.error("Please enter the valid age")
    except ValueError:
        logging.error("Please enter a number")
    except TypeError:
        logging.error("Please enter a number")

    try:
        if isinstance(r['patient_id'], str) and \
                isinstance(r['attending_email'], str):
            is_validate[4] = True
        else:
            is_validate[4] = False
    except ValueError:
        logging.error("Please enter a string")

    return all(element for element in is_validate)


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


def validate_heart_rate_input(r):
    """
    this function validate if the post request input heart_rate is
    in the correct format
    :param r: post request input
    :return: is_validate, boolean
    """
    is_validate = [False, False, False, False]
    try:
        is_validate[0] = r['patient_id'].isdigit()
        is_validate[1] = isinstance(r['heart_rate'], int)
        if not is_validate[1]:
            is_validate[1] = isinstance(r['heart_rate'], float)
        if len(r) == 2:
            is_validate[2] = True
        else:
            is_validate[2] = False
    except KeyError:
        logging.error("Please enter a valid input")
    except ValueError:
        logging.error("Please enter a number")
    except AttributeError:
        logging.error("Please enter a string")
    except TypeError:
        logging.error("Please input string")

    try:
        if isinstance(r['patient_id'], str):
            is_validate[3] = True
        else:
            is_validate[3] = False
    except ValueError:
        logging.error("Please enter a string")

    return all(element for element in is_validate)


def validate_interval_average_input(r):
    """
    this function test whether input for interval average
    is in the correct format
    :param r: post request input
    :return: is_validate, boolean
    """
    is_validate = [False, False, False, False]
    try:
        is_validate[0] = r['patient_id'].isdigit()
        fmt = '%Y-%m-%d %H:%M:%S.%f'
        try:
            datetime.datetime.strptime(r['heart_rate_average_since'], fmt)
            is_validate[1] = True
        except ValueError:
            logging.error("Please enter a number")
            is_validate[1] = False
        if len(r) == 2:
            is_validate[2] = True
        else:
            is_validate[2] = False
    except AttributeError:
        logging.error("Please enter a string")
    except TypeError:
        logging.error("Please input string")

    try:
        if isinstance(r['patient_id'], str) and \
                isinstance(r['heart_rate_average_since'], str):
            is_validate[3] = True
        else:
            is_validate[3] = False
    except ValueError:
        logging.error("Please enter a string")

    return all(element for element in is_validate)
