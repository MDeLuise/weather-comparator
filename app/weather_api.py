from datetime import datetime
import os
import pytz
import requests


API_KEY = os.environ.get('API_KEY')
API_PREF = 'mode=json&units=metric'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&' + API_PREF
API_ADV_URL = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&' + API_PREF
DEFAULT_TIME = 'Europe/Italy'
TIME_FMT = '%H:%M:%S %Z%z'


def get_local_time(utstamp, country, city):
    utc_dt = datetime.utcfromtimestamp(int(utstamp)).replace(tzinfo=pytz.utc)

    timezones = pytz.country_timezones.get(country.upper(), [])
    closest_timezone = [tz for tz in timezones if city.lower() in tz.lower()]

    if closest_timezone:
        tz = closest_timezone[0]
    elif timezones:
        tz = timezones[0] 
    else:
        tz = DEFAULT_TIME

    loc_tz = pytz.timezone(tz)
    dt = utc_dt.astimezone(loc_tz)
    return dt.strftime(TIME_FMT)


def query_api(city):
    return requests.get(API_URL.format(city, API_KEY)).json()


def query_advanced_api(city):
    return requests.get(API_ADV_URL.format(city, API_KEY)).json()