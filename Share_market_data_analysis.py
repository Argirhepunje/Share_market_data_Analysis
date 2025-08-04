import time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from playwright.sync_api import sync_playwright
import pandas as pd

# Convert 'YYYY-MM-DD' to UNIX timestamp
def date_to_unix(date_str):
    return int(time.mktime(time.strptime(date_str, "%Y-%m-%d")))

# Get the current date in 'YYYY-MM-DD' format
current_date = datetime.now()
current_date_str = current_date.strftime('%Y-%m-%d')
period2 = date_to_unix(current_date_str)
print(f"Current Date: {current_date} -> UNIX Timestamp: {period2}")

# Get the start date in 'YYYY-MM-DD' format
start_date = current_date - relativedelta(years=5)
start_date_str = start_date.strftime('%Y-%m-%d')
period1 = date_to_unix(start_date_str)
print(f"Start Date: {start_date} -> UNIX Timestamp: {period1}")

# Read the CSV file to get the list of stock symbols
file_path = "put tracker_data file path"        # Put tracker file path inside ("")
symbols_df = pd.read_csv(file_path)
trackers = symbols_df['Symbol'].tolist()
print("Stock Symbols:", trackers)
print('-'*50)

data_frames = []                               # Initialize a list to hold all data

for tracker in trackers:
    url = 'https://finance.yahoo.com/quote/JIOFIN.NS/history/?period1=1596209729&period2=1753976124'
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector('table.yf-1jecxey', timeout=60000)      # Increase or Decrease Timeout seconds as per network connection

        rows = page.query_selector_all('table.yf-1jecxey tbody tr')
        data = []
        for row in rows:
            cells = row.query_selector_all('td.yf-1jecxey')
            if len(cells) == 7:                                        # Only rows with 7 columns (date + 6 values)
                date = cells[0].inner_text().strip()
                open_ = cells[1].inner_text().strip()
                high = cells[2].inner_text().strip()
                low = cells[3].inner_text().strip()
                close = cells[4].inner_text().strip()
                adj_close = cells[5].inner_text().strip()
                volume = cells[6].inner_text().strip()
                data.append({
                    "symbol": tracker,
                    "Date": date,
                    "Open": open_,
                    "High": high,
                    "Low": low,
                    "Close": close,
                    "Adj Close": adj_close,
                    "Volume": volume
                })

        scrape_df = pd.DataFrame(data)
        print(scrape_df)
        data_frames.append(scrape_df)
        print('*'*50)

        combined_data = pd.concat(data_frames, ignore_index=True)
        combined_data.to_csv('Scrape_data.csv')     # CSV file name in which data is stored
        

