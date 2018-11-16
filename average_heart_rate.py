import numpy as np


def find_average_heart_rate(heart_rate):
    """
    this function calculate the average heart rate
    using mean function
    :param heart_rate: list of heart rate
    :return: average heart rate in bpm
    """
    average_heart_rate = np.mean(heart_rate)
    return average_heart_rate
