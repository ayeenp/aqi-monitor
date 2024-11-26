import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

try:
    response = requests.get('https://airnow.tehran.ir/', timeout=15)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    exit(1)

soup = BeautifulSoup(response.content, 'html.parser')

current_aqi = soup.select_one('#ContentPlaceHolder1_lblAqi3h').text

timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if not current_aqi:
    exit(1)

directory = '/tmp/aqi-collector'
os.makedirs(directory, exist_ok=True)

file_path = os.path.join(directory, 'last_aqi.txt')
with open(file_path, 'w') as file:
    file.write(f'{current_aqi}|{timestamp}')