# Flask Api to communicate with http://api.nbp.pl/
import requests
import json
import datetime as dt
from flask import Flask, request
nbp_url = "http://api.nbp.pl/api/exchangerates/rates/A/"

# Communication with NBP Api
def get_data(url):
    response = requests.get(url)
    try:
        return json.loads(response.text)
    except json.JSONDecodeError:
        return None

def prepareUrl(currency, start_date, end_date):
    url = nbp_url + currency + "/" + start_date + "/" + end_date + '?format=json'
    return url

# Finding the longest streak

def find_days_with_currency_increase(data):
    streaks = {}
    streakNo = 0
    def currency_rate_increased(data, i ):
        return data['rates'][i]['mid'] > data['rates'][i-1]['mid']

    for i in range(len(data['rates'])):
        if i == 0:
            continue
        if currency_rate_increased(data, i):
            if streakNo in streaks:
                streaks[streakNo].append({
                    'start': data['rates'][i-1]['effectiveDate'],
                    'end': data['rates'][i]['effectiveDate'],
                    'rate': data['rates'][i]['mid']
                })
            else:
                streaks[streakNo] = [{
                    'start': data['rates'][i-1]['effectiveDate'],
                    'end': data['rates'][i]['effectiveDate'],
                    'rate': data['rates'][i]['mid']
                }]
        else:
            streakNo += 1
    return streaks

def get_longest_streak(streaks):
    longest_streak = None
    for (i, streak) in streaks.items():
        start = dt.datetime.strptime(streak[0]['start'], '%Y-%m-%d')
        end = dt.datetime.strptime(streak[-1]['end'], '%Y-%m-%d')
        delta = (end - start).days
        if not longest_streak or delta > longest_streak['length']:
            longest_streak = {
                'streak': streak,
                'length': delta
            }
    return longest_streak

def getDataForCurrency(currency, start_date, end_date):
    url = prepareUrl(currency, start_date, end_date)
    print('CALLING URL', url)
    return get_data(url)

# Flask Api

app = Flask(__name__, static_folder='public', static_url_path='')

def validate_params(payload):
    missing_params = []
    if not payload.get('currency'):
        missing_params.append('currency')
    if not payload.get('startDate'):
        missing_params.append('startDate')
    if not payload.get('endDate'):
        missing_params.append('endDate')
    if len(missing_params):
        return False, missing_params
    return True, None

@app.route("/api/v1/streak/")
def longest_streak():
    request_data = request.args.to_dict()
    valid, params = validate_params(request_data)
    if not valid:
        # return 400 bad request with message
        return "You have to send all required parameters, missing: " + ', '.join(params), 400
    data = getDataForCurrency(request_data['currency'], request_data['startDate'], request_data['endDate'])
    if not data:
        return "No data found for given parameters", 404
    streaks = find_days_with_currency_increase(data)
    longest_streak = get_longest_streak(streaks)
    return json.dumps(longest_streak)



@app.route('/')
def static_file():
    return app.send_static_file('index.html')

@app.route('/currencies')
def currencies():
    return app.send_static_file('currencies.json')

# Main
if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='localhost', port=5000)

