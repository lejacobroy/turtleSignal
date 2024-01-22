import urllib.request
import sys
import os
from datetime import datetime     
from .models import MarketData  
from app import db                  

def download_market_data(ticker, interval, starting_date, ending_date):
    valid_intervals = {'1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'}
    if interval not in valid_intervals:
        print("Invalid interval. Valid intervals are: {}".format(valid_intervals))
        sys.exit()
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    start_date_obj = datetime.strptime(starting_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(ending_date, '%Y-%m-%d')
    
    # Edit the end date timestamp to be a multiple of the interval
    interval_seconds = 0
    if interval == '1m':
        interval_seconds = 60
    elif interval == '2m':
        interval_seconds = 120
    elif interval == '5m':
        interval_seconds = 300
    elif interval == '15m':
        interval_seconds = 900
    elif interval == '30m':
        interval_seconds = 1800
    elif interval == '60m':
        interval_seconds = 3600
    elif interval == '90m':
        interval_seconds = 5400
    elif interval == '1h':
        interval_seconds = 3600
    elif interval == '1d':
        interval_seconds = 86400
    elif interval == '5d':
        interval_seconds = 432000
    elif interval == '1wk':
        interval_seconds = 604800
    elif interval == '1mo':
        interval_seconds = 2592000
    elif interval == '3mo':
        interval_seconds = 7776000
        
    end_timestamp = int(end_date_obj.timestamp())
    start_timestamp = int(start_date_obj.timestamp())
    end_timestamp = int(end_timestamp / interval_seconds) * interval_seconds
    start_timestamp = int(start_timestamp / interval_seconds) * interval_seconds
    
    url="https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval={}&events=history".format(ticker,start_timestamp,end_timestamp, interval)
    print(url)
    try:
        response = urllib.request.urlopen(url)
        lines = response.read().decode('utf-8').split('\n')
        data_list = []
        for line in lines[1:]:
            unique = ticker+"_"+interval+"_"+line.split(',')[0]
            existing = MarketData.query.get(unique)
            if not existing:
                data = MarketData(
                    unique = unique,
                    id = ticker,
                    date = datetime.strptime(line.split(',')[0], '%Y-%m-%d'),
                    open = float(line.split(',')[1]),
                    high = float(line.split(',')[2]),
                    low = float(line.split(',')[3]),
                    close = float(line.split(',')[4]),
                    volume = float(line.split(',')[5])
                )
                data_list.append(data)
        try:
            db.session.bulk_save_objects(data_list) 
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
            

        print("Downloaded {} data to db".format(ticker))
        
    except Exception as e:
        print("Error downloading data for {}: {}".format(ticker, e))

