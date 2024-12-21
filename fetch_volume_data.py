import yfinance as yf
import pandas as pd
import datetime

# Define the list of NSE 500 tickers (example tickers, replace with actual NSE 500 tickers)
tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS']  # Add all NSE 500 tickers here

# Define the start and end dates
end_date = datetime.datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime('%Y-%m-%d')

# Generate the date range
date_range = pd.date_range(start=start_date, end=end_date)

# Initialize an empty DataFrame to store the volume data with dates as rows
volume_data = pd.DataFrame(index=date_range)

# Initialize a list to store failed tickers
failed_tickers = []

# Loop through each ticker and get the volume data
for ticker in tickers:
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if not data.empty:
            volume_data[ticker] = data['Volume']
        else:
            print(f"No data found for ticker: {ticker}. Considering volume as 0.")
            volume_data[ticker] = [0] * len(date_range)
    except Exception as e:
        print(f"Error retrieving data for ticker: {ticker}. Error: {e}. Considering volume as 0.")
        volume_data[ticker] = [0] * len(date_range)
        failed_tickers.append(ticker)

# Save the volume data to an Excel file
volume_data.to_excel('nse_500_volume_data.xlsx')

# Print the list of failed tickers
if failed_tickers:
    print("Failed to retrieve data for the following tickers:")
    for ticker in failed_tickers:
        print(ticker)
else:
    print("Successfully retrieved data for all tickers.")
