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
            json_objects.append(json.loads(match))  # Parse JSON string and append
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {match}\nError: {e}")
    
    return json_objects

def write_json_to_csv(json_data, output_file):
    """
    Writes a list of JSON objects to a CSV file.
    """
    if not json_data:
        print("No data to write to CSV.")
        return

    headers = list(json_data[0].keys())  # Use keys from the first JSON object as headers
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=headers)
        csvwriter.writeheader()
        csvwriter.writerows(json_data)

def process_script_to_csv(script_content, output_file):
    """
    Extracts JSON objects from a script and writes them to a CSV file.
    """
    json_objects = extract_json_objects(script_content)
    write_json_to_csv(json_objects, output_file)

# Example Usage
if __name__ == "__main__":
    # Your HTML content containing JSON.parse()
    script_content = """
        let region_39 = JSON.parse('{"id":"39","slug":"italtile-walmer","title":"Italtile Walmer","manager":"Johan Kemper","telephone":"041 612 0202","address_line1":"Corner Martin Road & 17th Avenue, Springfield, Gqeberha","city":"Gqeberha","longitude":"25.553106900296235","latitude":"-33.9837497645373","hours_mon":"8am - 5pm"}');
        let region_14 = JSON.parse('{"id":"14","slug":"italtile-boksburg","title":"Italtile Boksburg","manager":"Marku Gouws","telephone":"011 255 1060","address_line1":"Corner North Rand and Trichardt Road, Beyers Park, Boksburg","city":"Boksburg","longitude":"28.25489357301113","latitude":"-26.17841956297405","hours_mon":"8am - 5pm"}');
    """
    
    # Output CSV file
    output_csv_file = 'output.csv'

    # Process the script and write the JSON objects to CSV
    process_script_to_csv(script_content, output_csv_file)
    print(f"Data written to {output_csv_file}")
