from datetime import date, datetime

date_today = datetime.now()


def cur_date():
    c_date = date.today()
    return c_date


def cur_day():
    c_day = datetime.now().strftime("%d")
    return c_day


def cur_month():
    c_month = datetime.now().strftime("%m")
    return c_month


def cur_year():
    c_year = datetime.now().strftime("%Y")
    return c_year
