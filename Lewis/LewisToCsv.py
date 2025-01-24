import json
import csv

# Your JSON data (This is just an example, you can read it from a file)
data = [
    {
        "AdditionalInfo": "NULL",
        "Address": "86 Hibernia Street George  ",
        "City": "George",
        "CountryId": 73,
        "Email": "NULL",
        "Id": "0205",
        "Latitude": "-33.95920482",
        "Longitude": "22.45799055",
        "Phone": "043 054 0412",
        "Phone2": "",
        "Phone3": "",
        "Point": "George",
        "StateProvinceId": 84,
        "StoreId": "Lewis Stores",
        "StoreLocatorName": "George",
        "ZipCode": "6530",
        "TradingMonFri": "08:00 - 17:00",
        "TradingSat": "08:00 - 13:00",
        "TradingSunPub": "CLOSED"
    },
    {
        "AdditionalInfo": "NULL",
        "Address": "Shop 7, Ratsoma Shp Cntr The farm Battle 519 KS Tshehlwaneng Village Magnet Heights",
        "City": "Magnet Heights",
        "CountryId": 73,
        "Email": "NULL",
        "Id": "1152",
        "Latitude": "-24.790097",
        "Longitude": "29.973827",
        "Phone": "013 007 9290",
        "Phone2": "",
        "Phone3": "",
        "Point": "Magnet Heights",
        "StateProvinceId": 80,
        "StoreId": "Lewis Stores",
        "StoreLocatorName": "Magnet Heights",
        "ZipCode": "1435",
        "TradingMonFri": "08:00 - 18:00",
        "TradingSat": "08:00 - 15:00",
        "TradingSunPub": "CLOSED"
    }
    # Add the rest of your data here
]

# Define the CSV file path
csv_file = 'stores.csv'

# Open the CSV file and write data
with open(csv_file, mode='w', newline='') as file:
    # Create a CSV dict writer object
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    
    # Write the header (field names)
    writer.writeheader()
    
    # Write the rows (data)
    writer.writerows(data)

print(f"Data has been saved to {csv_file}")
