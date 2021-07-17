import requests
import json
import time
import subprocess
from datetime import date, datetime
import dateutil.parser
from consts import BAD_STATUSES, CAMP_MAP, ISO_WEEKDAY_MAPPING
import webbrowser
from twilio_utils import send_sms

def filter_available_campsite_days(all_campsites):
    available_camp_list = []
    for key, camp in all_campsites.items():
        for date_str, reserve_status in camp['availabilities'].items():
            if reserve_status not in BAD_STATUSES:
                date_obj = dateutil.parser.parse(date_str)
                day_of_week = ISO_WEEKDAY_MAPPING[date_obj.isoweekday()]
                available_camp_list.append({
                    "day_of_week": day_of_week,
                    "date": date_str,
                    "status": reserve_status,
                    "site_id": camp['campsite_id'],
                    "site": camp['site'],
                    "loop": camp['loop'],
                })
    return available_camp_list

def _print_available_sites(formatted_campsite_list=[]):
    for camp in formatted_campsite_list:
        print(camp)


def _get_reservable_dates_for_camp(camp_key, year, month, day):
    '''Returns yosemite campsites available for a given month.

    Arguments:
        camp_key (str): string according to CAMP_MAP
        year (str): The year, ie, 2020
        month (str): The month, ie, 09
        day (str): The day, ie, 01
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
    if (not resp or not resp['campsites']):
        print('No valid response'.format(resp))
        return []

    available = filter_available_campsite_days(resp['campsites'])
    _print_available_sites(available)

    open_site_len = len(available)
    print(f'Number of available campsites: {open_site_len}')

    return available


def notify_when_available(camp_key, year=datetime.now().year, month=datetime.now().month, day=datetime.now().day):
    results = _get_reservable_dates_for_camp(camp_key, year, month, day)
    if len(results) == 0:
        print(f'None available for {month}/{year}. Try again later...')
    else:
        print(f'Campsites are available for {month}/{year}')
        print(results)

        # format and send message
        loc = CAMP_MAP[camp_key]
        website_url = f'https://www.recreation.gov/camping/campgrounds/{loc}'
        message_body = f'Campsites available for {camp_key}! Go here: {website_url}'
        send_sms(message_body)

        # TODO: uncomment to enable direct website opening
        # webbrowser.open(website_url, new=2)
