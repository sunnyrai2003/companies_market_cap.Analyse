import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Prepare lists to hold the data
ranks = []
names = []
earnings = []
price_today = []
price_30_days = []
countries = []

# Step 2: Send a GET request to the website
url = 'https://companiesmarketcap.com/most-profitable-companies'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Step 4: Find the relevant data
    table = soup.find('div',class_="table-container shadow")  # Find the first table on the page
    rows = table.find_all('tr')  # Skip the header row

    # Step 5: Extract the data
    for row in rows:
        columns = row.find_all('td')  # Get all columns in the row
        if len(columns) >= 6:  # Ensure there are enough columns
            rank = columns[0].text
            name = columns[1].text
            earning = columns[2].text
            today_price = columns[3].text
            price_30_day = columns[4].text
            country = columns[5].text
            
            # Append the data to the respective lists
            ranks.append(rank)
            names.append(name)
            earnings.append(earning)
            price_today.append(today_price)
            price_30_days.append(price_30_day)
            countries.append(country)
    
    # Step 6: Create a DataFrame
    df = pd.DataFrame({
        'Rank': ranks,
        'Company': names,
        'Earnings': earnings,
        'Price Today': price_today,
        'Price (30 Days)': price_30_days,
        'Country': countries
    })
    
    # Step 7: Save the DataFrame to a CSV file
    df.to_csv('largest_companies_by_market_cap.csv', index=False)
    print("Data saved to 'largest_companies_by_market_cap.csv'")
else:
    print(f'Failed to retrieve data: {response.status_code}')