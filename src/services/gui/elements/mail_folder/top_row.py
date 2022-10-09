import datetime
from src.gui.config import TODAY_TIME, LAST_WEEK_TIME, LONG_AGO


def generate_ouput_time(time: datetime.datetime) -> str:
    if time == datetime.datetime.now():
        return time.strftime(TODAY_TIME)

    elif (datetime.datetime.now() - datetime.timedelta(days=7)) < time < datetime.datetime.now():
        return time.strftime(LAST_WEEK_TIME)

    else:
        return time.strftime(LONG_AGO)
