
# import re
# import json

# def extract_json_objects_from_script(script_content):
#     # Regex to match JSON inside JSON.parse('...') or JSON.parse("...") or JSON.parse(`...`)
#     json_pattern = re.compile(r"JSON\.parse\((['`\"])(.*?)\1\);", re.DOTALL)
    
#     matches = json_pattern.findall(script_content)  # Finds all matches
    
#     json_objects = []
#     for _, match in matches:
#         try:
#             # Parse each JSON string and append it to the list
#             json_data = json.loads(match)
#             json_objects.append(json_data)
#         except json.JSONDecodeError as e:
#             print(f"Failed to decode JSON: {match}\nError: {e}")
    
#     return json_objects





# # Step 1: Extract headers (keys from the first dictionary)
# headers = data[0].keys()

# # Step 2: Write to a CSV file
# with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(headers)  # Write headers
#     for row in data:
#         csvwriter.writerow([row[key] for key in headers])  # Write values





import re
import json
import csv

def extract_json_objects(script_content):
    """
    Extracts JSON objects from a script's content using regex.
    
    Parameters:
        script_content (str): The input script content containing JSON.parse().
    
    Returns:
        list: A list of parsed JSON objects.
    """
    # Regex to match JSON inside JSON.parse('...') or JSON.parse("...") or JSON.parse(`...`)
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
    
    Parameters:
        json_data (list): A list of dictionaries (JSON objects).
        output_file (str): The output CSV file path.
    """
    if not json_data:
        print("No data to write to CSV.")
        return

    headers = json_data[0].keys()  # Extract headers (keys from the first JSON object)
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)  # Write headers
        for row in json_data:
            csvwriter.writerow([row[key] for key in headers])  # Write values


def process_script_to_csv(script_content, output_file):
    """
    Extracts JSON objects from a script and writes them to a CSV file.
    
    Parameters:
        script_content (str): The script content containing JSON.parse() calls.
        output_file (str): The output CSV file path.
    """
    json_objects = extract_json_objects(script_content)
    write_json_to_csv(json_objects, output_file)


# Example Usage
if __name__ == "__main__":
    # Example script content
    script_content = """
        JSON.parse('{"name": "John", "age": 30, "city": "New York"}');
        JSON.parse('{"name": "Jane", "age": 25, "city": "San Francisco"}');
    """
    
    # Process script and write JSON objects to CSV
    process_script_to_csv(script_content, 'output.csv')
