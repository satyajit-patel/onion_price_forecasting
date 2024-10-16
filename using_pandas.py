import pandas as pd

url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=23&Tx_State=0&Tx_District=0&Tx_Market=0&DateFrom=01-Jan-2024&DateTo=16-Oct-2024&Fr_Date=01-Jan-2024&To_Date=16-Oct-2024&Tx_Trend=0&Tx_CommodityHead=Onion&Tx_StateHead=--Select--&Tx_DistrictHead=--Select--&Tx_MarketHead=--Select--'
allTable = pd.read_html(url)
print(len(allTable))

df = allTable[0];
df.head()

df.to_csv('onion_price_2024.csv')