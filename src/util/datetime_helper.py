from datetime import datetime, date

def get_current_dt_in_milliseconds_precision():
    dt= datetime.now()
    return dt

def calculate_difference_between_dates(new_date: date, past_date: date):
    diff = new_date - past_date
    print(diff.days)
    