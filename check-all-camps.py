from consts import CAMP_MAP
from yosemite_camping import notify_when_available

for key in CAMP_MAP:
    _args = {
        "camp_key": key,
        "year": '2020',
        "month": '09',
        "day": '01' # NOTE: month query only accepts the first of the month
    };
    print(f'Campsite {key}')
    notify_when_available(**_args)

