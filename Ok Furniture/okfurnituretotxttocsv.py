import re
import csv

# Function to read data from a file
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Parsing logic for markers1 data
def parse_markers(data):
    if not data:
        return []

    markers = []

    # Match the entire markers1 array (including all objects inside it)
    marker_pattern = r"markers1\s*=\s*\[(.*?)\];"
    marker_matches = re.findall(marker_pattern, data, re.DOTALL)

    # Process each marker object (should now get all objects in the array)
    for marker in marker_matches:
        # Split the individual markers by "},"
        individual_markers = marker.split("},")
        
        for individual_marker in individual_markers:
            marker_dict = {}

            # Match key-value pairs in the marker object
            key_value_pattern = r"(\w+):\s*['\"](.*?)['\"]|(\w+):\s*([-]?\d+\.\d+|\d+)"

            for key, value, numeric_key, numeric_value in re.findall(key_value_pattern, individual_marker):
                if key:  # For string key-value pairs
                    if key == "address" or key == "contact":
                        # Clean HTML tags in the address and contact fields
                        value = re.sub(r"<.*?>", " ", value).strip()  # Remove HTML tags
                        value = re.sub(r"\s+", " ", value)  # Remove extra spaces

                        if key == "contact":
                            # Extract the phone number from the 'tel:' link (if it exists)
                            phone_match = re.search(r"tel:\s*([^\"]+)", value)  # Match the number inside 'tel:'
                            if phone_match:
                                marker_dict["contact"] = phone_match.group(1).strip()  # Clean the phone number
                            else:
                                marker_dict["contact"] = None  # If no phone number is found
                    marker_dict[key] = value

                elif numeric_key:  # For numeric key-value pairs
                    marker_dict[numeric_key] = float(numeric_value) if "." in numeric_value else int(numeric_value)

            markers.append(marker_dict)
    
    return markers

# Function to write parsed data to CSV
def write_to_csv(parsed_markers, output_file):
    if parsed_markers:
        # Extract column headers from the keys of the first marker
        fieldnames = parsed_markers[0].keys()

        # Remove 'tel' if it exists in the fieldnames
        if 'tel' in fieldnames:
            fieldnames.remove('tel')

        # Remove 'tel' field from each dictionary in parsed_markers
        for marker in parsed_markers:
            if 'tel' in marker:
                del marker['tel']

        # Open the CSV file and write the data
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            writer.writerows(parsed_markers)  # Write the data rows

        print(f"Data has been saved to {output_file}")
    else:
        print("No data available to write to CSV.")

# File name containing markers1 data
file_path = "Ok Furniture/OK Furniture.txt"  # Your specified file path
output_csv = "okfurniture.csv"  # Output CSV file name

# Read input data from the file
input_data = read_file(file_path)

# Parse the markers from the input data
parsed_markers = parse_markers(input_data)

# Write the parsed data to CSV
write_to_csv(parsed_markers, output_csv)
