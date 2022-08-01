import datetime as dt


def get_formatted_date_today():
    now = dt.datetime.now()
    return now.strftime("%Y%m%d")


def get_formatted_date_week_before():
    now = dt.datetime.now()
    one_week = dt.timedelta(weeks=1)
    now -= one_week
    return now.strftime("%Y%m%d")
