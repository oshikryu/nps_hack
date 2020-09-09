import requests
import json
import time
import subprocess
from datetime import date, datetime
import dateutil.parser
from consts import BAD_STATUSES, CAMP_MAP, ISO_WEEKDAY_MAPPING

def filter_available_campsite_days(all_campsites):
    available_camp_list = []
    for key, camp in all_campsites.items():
        for date_str, reserve_status in camp['availabilities'].items():
            if reserve_status not in BAD_STATUSES:
                date_obj = dateutil.parser.parse(date_str)
                day_of_week = ISO_WEEKDAY_MAPPING[date_obj.isoweekday()]
                available_camp_list.append({
                    "status": reserve_status,
                    "date": date_str,
                    "day_of_week": day_of_week,
                    "site_id": camp['campsite_id'],
                    "site": camp['site'],
                    "loop": camp['loop'],
                })
    open_site_len = len(available_camp_list)
    print(f'Number of available campsites: {open_site_len}')
    return available_camp_list

def _print_available_sites(formatted_campsite_list=[]):
    for camp in formatted_campsite_list:
        print(camp)


def _get_reservable_dates_for_camp(camp_key, year, month, day):
    '''Returns the number of yosemite available day passes on a given day of the year.

    Arguments:
        year (str): The year, ie, 2020
        month (str): The month, ie, 09
        day (str): The day, ie, 04
    '''
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    headers={'user-agent': user_agent}

    # lazy html escaped timestamp
    start_date = f'{year}-{month}-{day}T00%3A00%3A00.000Z'
    loc = CAMP_MAP[camp_key]

    camp_url = f'https://www.recreation.gov/api/camps/availability/campground/{loc}/month?start_date={start_date}'

    response = requests.get(
        camp_url,
        headers=headers
    )
    if response.status_code == 400:
        print(f'{response.content}')

    resp = json.loads(response.content)
    available = filter_available_campsite_days(resp['campsites'])
    _print_available_sites(available)
    return available


def notify_when_available(camp_key, year=2020, month=9, day=1):
    # counter = 0
    # while len(_get_reservable_dates_for_camp(camp_key, year, month, day)) == 0:
        # counter += 1
        # print(f'Still unavailable on {year}, {month}, {day}. Trying again... attempt #{counter}')
        # Check every 5 minutes
        # time.sleep(300)

    if len(_get_reservable_dates_for_camp(camp_key, year, month, day)) == 0:
         print(f'Still unavailable on {year}, {month}, {day}. Try again later...')
    else:
        print(f'Campsites are available for {month}/{year}')
        loc = CAMP_MAP[camp_key]
        print(f'Recreation.gov url: https://www.recreation.gov/camping/campgrounds/{loc}')

        applescript = """
        display dialog "Yosemite camp site available, check the dates you wanted." ¬
        with title "Campsite reservation" ¬
        with icon caution ¬
        buttons {"OK"}
        """

        subprocess.call("osascript -e '{}'".format(applescript), shell=True)
