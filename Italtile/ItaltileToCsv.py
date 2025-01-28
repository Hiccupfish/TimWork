import re
import json
import csv

def extract_json_objects(script_content):
    """
    Extracts JSON objects from a script's content using regex.
    """
    json_pattern = re.compile(r"JSON\.parse\((['`\"])(.*?)\1\);", re.DOTALL)
    matches = json_pattern.findall(script_content)

    json_objects = []
    for _, match in matches:
        try:
            # Clean up the JSON string (remove extra spaces, newlines, etc.)
            cleaned_match = match.replace("\\", "").strip()
            json_objects.append(json.loads(cleaned_match))  # Parse JSON string and append
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {cleaned_match}\nError: {e}")
    
    return json_objects

def write_json_to_csv(json_data, output_file):
    """
    Writes a list of JSON objects to a CSV file.
    """
    if not json_data:
        print("No data to write to CSV.")
        return

    # Use keys from the first JSON object as headers
    headers = list(json_data[0].keys())
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        csvwriter.writeheader()
        for row in json_data:
            # Ensure all keys are present in the row, even if some are missing in the JSON
            row = {key: row.get(key, "") for key in headers}
            csvwriter.writerow(row)

def process_script_to_csv(input_file, output_file):
    """
    Reads script content from a file, extracts JSON objects, and writes them to a CSV file.
    """
    # Read the content from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        script_content = file.read()

    # Extract JSON objects from the script content
    json_objects = extract_json_objects(script_content)

    # Write JSON objects to the CSV file
    write_json_to_csv(json_objects, output_file)

# Example Usage
if __name__ == "__main__":
    # Input file containing the script content
    input_file = "Italtile\Italtile.txt"  # Replace with the path to your file

    # Output CSV file
    output_csv_file = 'output.csv'

    # Process the script and write the JSON objects to CSV
    process_script_to_csv(input_file, output_csv_file)
    print(f"Data written to {output_csv_file}")