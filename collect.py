import requests
from bs4 import BeautifulSoup

response = requests.get('https://airnow.tehran.ir/')

soup = BeautifulSoup(response.content, 'html.parser')

last_day_aqi = soup.select_one('#ContentPlaceHolder1_lblAqi24h').text
current_aqi = soup.select_one('#ContentPlaceHolder1_lblAqi3h').text

if not last_day_aqi or not current_aqi:
    print('Could not find AQI data')
    exit(1)
    
print(f'Last day AQI: {last_day_aqi}')
print(f'Current AQI: {current_aqi}')
