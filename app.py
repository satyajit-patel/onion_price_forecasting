# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import pandas as pd

# chrome_driver_path = r'D:\MERN\webScrapingAgmarknet\chromeDriver\chromedriver-win64\chromedriver.exe'
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

# # Open the URL
# driver.get("https://agmarknet.gov.in/")

# # Select "Onion" in the Commodity dropdown
# commodity_select = Select(driver.find_element(By.ID, "ddlCommodity"))
# commodity_select.select_by_visible_text("Onion")

# # Input date range
# driver.find_element(By.ID, "txtDate").send_keys("14-Oct-2024")
# driver.find_element(By.ID, "txtDateTo").send_keys("14-Oct-2024")

# # Click the "Go" button
# driver.find_element(By.ID, "btnGo").click()

# try:
#     # Wait for the table to load
#     print("wating")
#     # time.sleep(20)
#     WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.ID, "cphBody_GridPriceData")))
#     time.sleep(10)  # Additional wait for loading
#     print("waiting finish")

#     # Locate table body and rows
#     table = driver.find_element(By.XPATH, ".//cphBody_GridPriceData")
#     rows = table.find_elements(By.XPATH, ".//tbody/tr")

#     # Extract and store data
#     data = []
#     for row in rows[1:]:  # Skip the header
#         cols = row.find_elements(By.TAG_NAME, "td")
#         data.append([col.text for col in cols])

#     # Convert to DataFrame
#     df = pd.DataFrame(data, columns=['Sl No.', 'District Name', 'Market Name', 'Commodity', 'Variety', 'Grade', 'Min Price', 'Max Price', 'Modal Price', 'Price Date'])
#     df.to_csv("onion_prices.csv", index=False)
#     print("Data saved to onion_prices.csv")

# except Exception as e:
#     print(f"Error occurred: {e}")

# finally:
#     driver.quit()

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the onion price data (Check if there's a direct URL after form submission)
# url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=15-Oct-2024&DateTo=15-Oct-2024&Fr_Date=15-Oct-2024&To_Date=15-Oct-2024&Tx_Trend=0&Tx_CommodityHead=Onion&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--"
url = "https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=01-Jan-2024&DateTo=15-Oct-2024&Fr_Date=01-Jan-2024&To_Date=15-Oct-2024&Tx_Trend=0&Tx_CommodityHead=Onion&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--"
# Make a GET request to fetch the page content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Assuming the data is already present in a table without form interaction
# Find the table with onion prices (adjust according to the HTML structure)
table = soup.find('table', {'id': 'cphBody_GridPriceData'})

# Extract rows from the table
rows = table.find_all('tbody/tr')

# Initialize a list to store data
data = []

# Loop through the rows to extract columns
for row in rows[1:]:  # Skip header row
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Convert the data into a DataFrame
df = pd.DataFrame(data, columns=['Sl No.', 'District Name', 'Market Name', 'Commodity', 'Variety', 'Grade', 'Min Price', 'Max Price', 'Modal Price', 'Price Date'])

# Save to CSV
df.to_csv('onion_prices_24.csv', index=False)
print("Data saved to onion_prices.csv")
