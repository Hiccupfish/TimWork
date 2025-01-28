import json
import csv

# Function to read data from the JSON file
def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)  # Parse the JSON file
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not valid JSON.")
        return []

# Path to the JSON file
json_file = 'Lewis\Lewis.txt'

# Read the JSON data from the file
data = read_json_file(json_file)

# Define the CSV file path
csv_file = 'Lewis.csv'

if data:
    # Open the CSV file and write data
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        # Create a CSV dict writer object
        writer = csv.DictWriter(file, fieldnames=data[0].keys())

        # Write the header (field names)
        writer.writeheader()

        # Write the rows (data)
        writer.writerows(data)

    print(f"Data has been saved to {csv_file}")
else:
    print("No data available to write to CSV.")
