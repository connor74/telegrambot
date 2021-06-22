import datetime
import requests


def get_weather(token):
    params = {
        'lat': '55.156154',
        'lon': '61.417799',
        'exclude': 'alerts',
        'lang': 'ru',
        'units': 'metric',
        'appid': token

    }
    r = requests.get('https://api.openweathermap.org/data/2.5/onecall', params)
    if r.status_code == 200:
        jsn = r.json()
        return {'current': {
            'date': datetime.datetime.fromtimestamp(jsn['current']['dt']),
            'Температура воздуха': jsn['current']['temp'],
            'temp_feel': jsn['current']['feels_like'],
            'description': jsn['current']['weather'][0]['description']
        }

        }
    else:
        return None
