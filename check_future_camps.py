from consts import CAMP_MAP
from camp_checker import notify_when_available
from datetime import datetime

def main():
    year = str(datetime.now().year)
    month = f'{datetime.now().month:02}' # 0-padded month integer
    day = '01' # NOTE: month query only accepts the first of the month
    if int(month) < 11:
        END_MONTH = datetime.now().month + 1
    else:
        END_MONTH = 1

    while int(month) < END_MONTH:
        for key in CAMP_MAP:
            _args = {
                "camp_key": key,
                "year": year,
                "month": month,
                "day": day,
            };
            print(f'Campsite {key}')
            notify_when_available(**_args)
        month = int(month) + 1
        month = f'{month:02}'

if __name__ == "__main__":
    # execute only if run as a script
    main()
