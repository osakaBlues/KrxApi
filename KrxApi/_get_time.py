import datetime as dt


def get_formatted_date():
    now = dt.datetime.now()
    return now.strftime("%Y%m%d")
