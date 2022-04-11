# Import the required libraries and dependencies
import os
import sys
import datetime
import requests
import json
import numpy as np
import pandas as pd
import panel as pn
from panel.interact import interact
from panel import widgets
from dotenv import load_dotenv
import hvplot.pandas
%matplotlib inline
pn.extension("plotly")

# Make an API call to access the current prices for BEKE, OPEN, RDFN, Z, EXPI, AMT, CBRE, WY, ESS, AVB, ARE and SPY. (Credits: Binoy Das - Slack post)
def fetch_stock_aggregates(tickers, multiplier=1, timespan="day", start_date='', end_date='', columns=['Close'], key=polygon_api_key):

    column_mappings = {'c': 'Close', 'h': 'High', 'l':'Low', 'n':'Transactions', 'o':'Open', 'v':'Volume', 'vw':'Adjusted'}
    data_frames = {}    
    if end_date == '':
        end_date = datetime.date.today().strftime('%Y-%m-%d')
    if start_date == '':
        start_date = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')    
        
    for ticker in tickers:
        if 'polygon' in sys.modules:                
            with RESTClient(key) as polygon_client:
                response_json = polygon_client.stocks_equities_aggregates(ticker, multiplier, timespan, start_date, end_date, limit=50000)
                stock_df = pd.DataFrame(response_json.results)
                print(f"{timespan.capitalize()} aggregates for {response_json.ticker} between {start_date} and {end_date} fetched.")
        else:
            url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{start_date}/{end_date}?sort=asc&limit=50000&apiKey={key}"
            print(url)
            response_json = requests.get(url).json()
            stock_df = pd.DataFrame(response_json['results'])
            print(f"{timespan.capitalize()} aggregates for {response_json['ticker']} between {start_date} and {end_date} fetched.")
        
        stock_df["Date"] = pd.to_datetime(stock_df["t"].div(1000), unit='s')
        stock_df = stock_df.drop(['t'], axis=1)
        stock_df = stock_df.set_index("Date")
        
        column_names = []
        for column in stock_df.columns:
            if column in column_mappings.keys():
                column_name = column_mappings[column]
            if column_name in columns:
                column_names.append(column_name)
            else:
                stock_df = stock_df.drop([column], axis=1)
        stock_df.columns = column_names
        data_frames[ticker] = stock_df
        
    merged_df = pd.concat(data_frames.values(), axis=1, keys=data_frames.keys())
    merged_df=merged_df.dropna()
    
    return merged_df

# Function to convert df to pct change
def fetch_pct(stock_df):
    df = pd.DataFrame()
    for col in stock_df.columns:
    df[col[0]] = stock_df[col[0]][col[1]]
    pct_change_df = df.pct_change()
    
    return pct_change_df


def cum_returns(df):
    cumulative_returns = (1 + stock_df).cumprod()
    
    return cumulative_returns


def std_dev(stock_df):
    std_dev_srtd = stocks_df.std().sort_values()
    
    return std_dev_srtd


def run():
    print("Loading the enviroment & verifying Polygon Key")
    
    # Load enviroment variables
    load_dotenv()
    # Set Polygon API key
    polygon_api_key = os.getenv("POLYGON_API")
    
    # Verifying Polygon key load 
    if type(polygon_api_key) == str:
        print("Polygon Key failed to load")
        real_estate_cli = True
    else:
        print("Polygon Key failed to load")
        real_estate_cli = False
    
    
    while real_estate_cli:
        # Initializing tickers chosen for analysis
        tickers = ['BEKE', 'OPEN', 'RDFN', 'Z', 'EXPI']
        # Initializing earliest possible start date given real estate IPO dates
        start_date = '2021-01-01'
        
        print(f"The tickers chosen for analysis are: {', '.join(tickers)}")
        print(f"Analysis on ticker data starting {start_date}")
        
        
        # Fetching stock data
        stock_df = fetch_stock_aggregates(tickers, start_date)
        
        # TEST: Reviewing stock DF
        stock_df
        
        choice = questionary.select(
            "Which scope of analysis would you prefer?",
            choices=["Complete", "Specific"]
        ).ask()
        
        if choice == "Specific":
            
            choice = questionary.select(
                "Which analysis method would you like to view for the given real estate stocks?",
                choices=["Daily Returns", "Cumulative Returns", "YTD Returns", "Standard Deviation", "Sharpe Ratio", "Beta"]
            ).ask()
            
            
        
        