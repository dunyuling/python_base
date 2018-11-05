import datetime 

def get_now():
    time_pattern = '%Y.%m.%d-%H:%M:%S'
    return datetime.datetime.now().strftime(time_pattern) 

