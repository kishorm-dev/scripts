import os
import json

# Function to sort JSON files in a directory
def sort_json_files(directory):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            # Read the JSON data from the file
            with open(file_path, 'r') as file:
                json_data = json.load(file)
            # Sort the JSON keys
            sorted_keys = sorted(json_data.keys())
            # Create a new dictionary with sorted keys
            sorted_json_data = {key: json_data[key] for key in sorted_keys}
            # Create a new filename with "sorted" suffix
            new_filename = os.path.splitext(filename)[0] + '_sorted.json'
            new_file_path = os.path.join(directory, new_filename)
            # Write the sorted JSON data to a new file
            with open(new_file_path, 'w') as new_file:
                json.dump(sorted_json_data, new_file, indent=4)
            print(f"Sorted JSON saved to: {new_file_path}")

# Specify the directory containing JSON files
directory_path = '/Users/kmuruganandham/Documents/FWSS/EUW'

# Call the function to sort JSON files in the directory
sort_json_files(directory_path)
