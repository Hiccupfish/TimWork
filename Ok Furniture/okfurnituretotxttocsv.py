import re
import csv
import json

# Read the .txt file
with open("data.txt", "r") as file:
    text = file.read()

# Regex to extract JavaScript object-like data (i.e., the list of markers)
pattern = r"\[\{(.*?)\}\]"

matches = re.findall(pattern, text, re.DOTALL)

# Extract fields from each marker object
markers = []

# Define a helper function to clean and convert the string to a dictionary
def parse_marker(marker_str):
    # Remove unnecessary HTML tags and clean up the string
    marker_str = marker_str.replace("</br>", " ").replace("\n", "")
    
    # Parse the key-value pairs inside the marker string
    marker_dict = {}
    key_value_pattern = r"(\w+):\s*['\"](.*?)['\"]"
    for key, value in re.findall(key_value_pattern, marker_str):
        marker_dict[key] = value
    return marker_dict

# Loop through each marker and convert it into a dictionary
for match in matches:
    markers.append(parse_marker(match))

# Save the markers list as a CSV file
csv_file = "markers.csv"
csv_columns = markers[0].keys()

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(markers)

print(f"Data has been saved to {csv_file}")
