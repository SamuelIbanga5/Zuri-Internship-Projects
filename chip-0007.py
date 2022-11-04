import csv
import json
import hashlib
from data import data

def convert_to_json(input, output):

    # Create dictionary to include json data
    obj = data
    
    # Open a csv reader called DictReader
    with open(input, encoding='utf-8', newline="") as csvf:
        csvReader = csv.DictReader(csvf, delimiter=',', quotechar='|')
        row_count = sum(1 for line in csvReader)

    # Open a csv reader and read the csv files into dictionaries
    # Open the output csv file to write dictionary into file
    # Write header of csv file into output file
    with open(input, newline="") as file, open(output, "w", newline="\n") as output_file:
        reader = csv.DictReader(file, delimiter=",", quotechar="|")
        writer = csv.DictWriter(output_file, delimiter=",", quotechar="|", fieldnames=["TEAM NAMES", "Series Number", "Filename", "Name", "Description", "Gender", "Attributes", "UUID", "Hashed", None])
        writer.writeheader()

        # Looping through reader object and converting each rows to dictionaries
        # and adding it to data
        for rows in reader:
            obj["name"]= rows["Filename"]
            obj["description"] = rows["Description"]
            obj["minting_tool"] = rows["TEAM NAMES"]
            obj["collection"]["id"] = rows["UUID"]
            obj["series_number"] = rows["Series Number"]
            obj["series_total"] = row_count
            obj["gender"] = rows["Gender"]
            obj["attributes"] = rows["Attributes"].split("; ")

            # Convert dictionary objects into json format and store in json_file
            json_file = json.dumps(obj, sort_keys=False, indent=4)

            # Calculating has for the json_file
            hashed = hashlib.sha256(json_file.encode("utf-8")).hexdigest()

            # Adding hash field with values to each line of the new output csv file
            rows["Hashed"] = hashed

            # Write rows of csv files into output csv file
            writer.writerow(rows)

# Prompt user for filename to read from and to be used for output csv file
input = input("Enter the name of your CSV file: ")
output = input
input += ".csv"
output += f".output.csv"

# Function call
convert_to_json(input, output)