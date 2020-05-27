import requests
import pprint
import json
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
	return {'about': 'Welcome to my Coronameter'}

@app.route('/<country>', methods=['GET'])
def get(country):
	return {country: country_data[country]}


URL = 'https://www.worldometers.info/coronavirus/#countries'
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
count_table = soup.find(id='main_table_countries_today')
table_rows = count_table.find_all('tr')

state = {}

for tr in table_rows:
	td = tr.find_all('td')
	row = [cell.text.strip() for cell in td]
	res = [val for idx, val in enumerate(row)
		if val or (not val and row[idx-1])]

	if len(res) > 0:
		state[res[0]] = res

country_data = {}

for key, value in state.items():
	key = value[1]
	country_data[key] = {
		'total cases': value[2],
		'new cases': value[3],
		'total deaths': value[4],
		'new-deaths': value[5],
		'total-recovered': value[6],
	}

if __name__ == '__main__':
	app.run(debug=True)