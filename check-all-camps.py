from consts import CAMP_MAP
from camp_checker import notify_when_available
from datetime import datetime

year = str(datetime.now().year)
month = f'{datetime.now().month:02}' # 0-padded month integer
day = '01' # NOTE: month query only accepts the first of the month

for key in CAMP_MAP:
    _args = {
        "camp_key": key,
        "year": year,
        "month": month,
        "day": day,
    };
    print(f'Campsite {key}')
    notify_when_available(**_args)

