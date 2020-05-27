import requests
import pprint
import json
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
	return {'about': 'Welcome to my Coronameter'}
