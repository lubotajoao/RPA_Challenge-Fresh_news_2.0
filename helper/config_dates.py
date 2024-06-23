from datetime import datetime

date_today = datetime.now()


def cur_day():
    c_day = datetime.now().strftime("%d")
    return c_day


def cur_month():
    c_month = datetime.now().strftime("%m")
    return c_month


def cur_year():
    c_year = datetime.now().strftime("%Y")
    return c_year


def cur_date() -> str:
    current_day = cur_day()
    current_month = cur_month()
    current_year = cur_year()

    current_date = f"{current_year}_{current_month}_{current_day}"

    return current_date
