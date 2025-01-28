import json
import csv
import re

# File path
file_path = r"TopT\TopT.txt"

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Regex pattern to extract JSON data
json_pattern = r'let region_\d+ = JSON\.parse\(`(.*?)`\);'

# Extract JSON data using regex
json_data_matches = re.findall(json_pattern, data)

# Parse JSON data
json_data = [json.loads(match) for match in json_data_matches]

# Save parsed data to CSV
output_file = "parsed_stores.csv"
with open(output_file, mode='w', encoding='utf-8', newline='') as csv_file:
    # Fields based on the JSON structure
    fieldnames = ["ID", "Slug", "Title", "Manager", "Telephone", "City", "Address Line 1", "Address Line 2", "Email", "Store Code", "Website", "Hours"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through JSON entries and write to CSV
    for entry in json_data:
        writer.writerow({
            "ID": entry.get("id", "Unknown"),
            "Slug": entry.get("slug", "Unknown"),
            "Title": entry.get("title", "Unknown"),
            "Manager": entry.get("manager", "Unknown"),
            "Telephone": entry.get("telephone", "Unknown"),
            "City": entry.get("city", "Unknown"),
            "Address Line 1": entry.get("address_line1", "Unknown"),
            "Address Line 2": entry.get("address_line2", "Unknown"),
            "Email": entry.get("email", "Unknown"),
            "Store Code": entry.get("store_code", "Unknown"),
            "Website": entry.get("website", "Unknown"),
            "Hours": entry.get("hours_default", "Unknown"),
        })

print(f"Data saved to {output_file}")
