import random
import time


def get_random_int_id():
    now = time.localtime()
    day = now.tm_mday
    year = now.tm_year
    month = now.tm_mon
    hour = now.tm_hour
    mini = now.tm_min
    sec = now.tm_sec
    string1 = f'{day}{year - mini - sec - month - hour}'
    ran = random.random()
    ran = str(ran)
    ran = ran.split('.')
    ran = ran[1]
    str_ran = f'{ran[:5] + string1}'
    int_id = int(str_ran)
    return int_id - 50000000
