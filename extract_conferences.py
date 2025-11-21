import json
import csv
import os

def extract_conferences(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Name', 'ShortName', 'StartDate', 'City', 'Country', 'ExternalUrl']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for conference in data:
                name = conference.get('Name', '')
                short_name = conference.get('UrlSegmentName', '')
                start_date = conference.get('StartDate', '')
                city = conference.get('City', '')
                country = conference.get('Country', '')
                external_url = conference.get('ExternalUrl', '')

                writer.writerow({
                    'Name': name,
                    'ShortName': short_name,
                    'StartDate': start_date,
                    'City': city,
                    'Country': country,
                    'ExternalUrl': external_url
                })
        
        print(f"Successfully extracted conference data to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from {input_file}. Details: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_path = 'conferences.txt'
    output_path = 'conferences.csv'
    extract_conferences(input_path, output_path)
