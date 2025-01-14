import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def fetch_airnow_aqi():
    try:
        response = requests.get('https://airnow.tehran.ir/', timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    current_aqi = soup.select_one('#ContentPlaceHolder1_lblAqi3h').text

    return current_aqi

def fetch_iqair_aqi():
    api_key = os.getenv('IQAIR_API_KEY')
    url = f"http://api.airvisual.com/v2/city?city=Tehran&state=Tehran&country=Iran&key={api_key}"

    payload={}
    headers = {}

    try:
        response = requests.request("GET", url, headers=headers, data=payload, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    current_aqi = response.json()['data']['current']['pollution']['aqius']

    return current_aqi


current_aqi = fetch_iqair_aqi()
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if not current_aqi:
    exit(1)

directory = '/tmp/aqi-collector'
os.makedirs(directory, exist_ok=True)

file_path = os.path.join(directory, 'last_aqi.txt')
with open(file_path, 'w') as file:
    file.write(f'{current_aqi}|{timestamp}')