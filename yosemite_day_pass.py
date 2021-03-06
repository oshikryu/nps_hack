import requests
import json
import time
import subprocess
from datetime import datetime
from calendar import monthrange

def _get_number_of_available_day_passes_on_given_day(year, month, day):
    '''Returns the number of yosemite available day passes on a given day of the year.

    Arguments:
        year (str): The year, ie, 2020
        month (str): The month, ie, 09
        day (str): The day, ie, 04
    '''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    response = requests.get(
        f'https://www.recreation.gov/api/ticket/availability/facility/300015/monthlyAvailabilitySummaryView?year={year}&month={month}&inventoryBucket=FIT', headers={'user-agent': user_agent}
    )
    dates_json = json.loads(response.text)

    return dates_json['facility_availability_summary_view_by_local_date'][f'{year}-{month}-{day}']['tour_availability_summary_view_by_tour_id']['3000']['reservable']

def notify_when_day_pass_is_available(year=2020, month=9, day=1):
    counter = 0
    while _get_number_of_available_day_passes_on_given_day(year, month, day) == 0:
        counter += 1
        print(f'Still unavailable on {year}, {month}, {day}. Trying again... attempt #{counter}')
        # Check every 5 minutes
        time.sleep(300)

    print(f'Day passes are available on {year}, {month}, {day}')

    applescript = """
    display dialog "Yosemite day pass available, check the dates you wanted." ¬
    with title "Day pass" ¬
    with icon caution ¬
    buttons {"OK"}
    """

    subprocess.call("osascript -e '{}'".format(applescript), shell=True)

def main():
    year = str(datetime.now().year)
    month = f'{datetime.now().month:02}' # 0-padded month integer
    day = '01'
    date_args = {
        "year": year,
        "month": month,
        "day": day,
    }
    month, END_MONTH = monthrange(datetime.now().year, datetime.now().month)

    while int(day) < END_MONTH:
        notify_when_day_pass_is_available(**date_args)
        day = int(day) + 1
        day = f'{day:02}'

if __name__ == "__main__":
    # execute only if run as a script
    main()
