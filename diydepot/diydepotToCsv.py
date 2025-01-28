import re
import csv
from bs4 import BeautifulSoup

# File path for the HTML file
html_file_path = "diydepot/diydepot.txt"

# Read the HTML content from the file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Prepare CSV file
csv_filename = "store_data.csv"
csv_headers = [
    "Store Name",
    "Phone Number",
    "Address",
    "Latitude",
    "Longitude",
    "Trading Hours",
    "Contact URL"
]

# Open CSV file for writing
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)  # Write headers

    # Extract and process data
    for store in soup.find_all("div", class_="single-location"):
        # Store Name
        name_tag = store.find("h4")
        store_name = name_tag.get_text(strip=True) if name_tag else "N/A"

        # Phone Number
        phone_tag = store.find("a", href=re.compile(r"^tel:"))
        phone_number = phone_tag.get_text(strip=True) if phone_tag else "N/A"

        # Address
        address_div = store.find("div", class_="store-location")
        address = (
            " ".join(
                [p.get_text(strip=True) for p in address_div.find_all("p") if p.get_text(strip=True)]
            ) if address_div else "N/A"
        )

        # Latitude and Longitude
        hidden_marker = store.find("div", class_=re.compile(r"js-wpv-addon-maps-marker"))
        latitude = hidden_marker["data-markerlat"] if hidden_marker and "data-markerlat" in hidden_marker.attrs else "N/A"
        longitude = hidden_marker["data-markerlon"] if hidden_marker and "data-markerlon" in hidden_marker.attrs else "N/A"

        # Trading Hours
        trading_hours_div = store.find("div", class_="trading-hours")
        trading_hours = trading_hours_div.get_text(strip=True).replace("Trading Hours:", "").strip() if trading_hours_div else "N/A"

        # Contact URL
        contact_link = store.find("a", href=re.compile(r"diy-store"))
        contact_url = contact_link["href"] if contact_link else "N/A"

        # Write row to CSV
        writer.writerow([store_name, phone_number, address, latitude, longitude, trading_hours, contact_url])

print(f"Data successfully written to {csv_filename}")