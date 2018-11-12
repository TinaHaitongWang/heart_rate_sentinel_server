def check_tachycardic(user_age, latest_heart_rate):
    """
    this function check if the user currently is tachycardic
    using latest heart rate measure
    :param user_age: age in years
    :param latest_heart_rate: heart rate in bpm
    :return: string, tachycardic or not tachycardiac
    """
    is_tachycardia = False
    if user_age < 1:
        user_age_in_day = round(user_age * 365)
        if 1 <= user_age_in_day < 3:
            if latest_heart_rate > 159:
                is_tachycardia = True
        elif 3 <= user_age_in_day < 7:
            if latest_heart_rate > 166:
                is_tachycardia = True
        elif 7 <= user_age_in_day < 22:
            if latest_heart_rate > 182:
                is_tachycardia = True
        elif 22 <= user_age_in_day < 63:
            if latest_heart_rate > 179:
                is_tachycardia = True
        elif 63 <= user_age_in_day < 153:
            if latest_heart_rate > 186:
                is_tachycardia = True
        elif 153 <= user_age_in_day <= 365:
            if latest_heart_rate > 169:
                is_tachycardia = True
    elif 1 <= user_age < 3:
        if latest_heart_rate > 151:
            is_tachycardia = True
    elif 3 <= user_age < 5:
        if latest_heart_rate > 137:
            is_tachycardia = True
    elif 5 <= user_age < 8:
        if latest_heart_rate > 133:
            is_tachycardia = True
    elif 8 <= user_age < 12:
        if latest_heart_rate > 130:
            is_tachycardia = True
    elif 12 <= user_age <= 15:
        if latest_heart_rate > 119:
            is_tachycardia = True
    elif user_age > 15:
        if latest_heart_rate > 100:
            is_tachycardia = True

    if is_tachycardia:
        return "tachycardic"
    else:
        return "not tachycardic"