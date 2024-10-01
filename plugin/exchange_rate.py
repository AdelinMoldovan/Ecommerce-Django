from decimal import Decimal
import requests

import requests
from decimal import Decimal

def fetch_exchange_rates():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')  # or use another API that supports your needs
    data = response.json()
    return {
        'RON': Decimal(data['rates']['RON']),  # Fetching the RON exchange rate
    }

exchange_rates = fetch_exchange_rates()
"""
def get_usd_to_inr_rate():
    return exchange_rates['INR']

def get_usd_to_ngn_rate():
    return exchange_rates['NGN']

def convert_usd_to_inr(usd_amount):
    inr_rate = get_usd_to_inr_rate()
    return usd_amount * inr_rate

def convert_usd_to_kobo(usd_amount):
    ngn_rate = get_usd_to_ngn_rate()
    ngn_amount = usd_amount * ngn_rate
    return int(ngn_amount * 100)  # Convert NGN to Kobo

def convert_usd_to_ngn(usd_amount):
    ngn_rate = get_usd_to_ngn_rate()
    return usd_amount * ngn_rate"""
def get_usd_to_ron_rate():
    return exchange_rates['RON']

def convert_usd_to_ron(usd_amount):
    ron_rate = get_usd_to_ron_rate()
    return usd_amount * ron_rate


