from camp_checker import notify_when_available
from datetime import datetime
# ---------------------------------------- #
# modify arguments here

year = str(datetime.now().year)
month = f'{datetime.now().month:02}'
day = '01' # NOTE: month query only accepts the first of the month

_args = {
    "camp_key": "upper_pines", # maps to CAMP_MAP value
    "year": year,
    "month": month,
    "day": day,
};
# ---------------------------------------- #

notify_when_available(**_args)
