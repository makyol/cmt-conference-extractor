# CMT Conference Extractor

This project provides a simple Python script to extract and structure conference data from the Microsoft Conference Management Toolkit (CMT) platform.

## Background

The [Conference Management Toolkit (CMT)](https://cmt3.research.microsoft.com/) is a popular platform used for managing academic conferences. While it hosts a vast list of conferences, the platform's interface for browsing these conferences has limitations regarding filtering and sorting capabilities.

## Purpose

The goal of this project is to convert the raw conference data (manually retrieved from CMT) into a structured CSV format. This allows researchers and potential attendees to:
- Sort conferences by date, name, or location.
- Filter conferences based on specific criteria (e.g., country, city).
- Easily view and analyze the available conferences in a spreadsheet application.

## How it Works

The project consists of a Python script `extract_conferences.py` that takes a raw text file containing JSON data (`conferences.txt`) and converts it into a CSV file (`conferences.csv`).

### Input Data
The `conferences.txt` file contains a JSON array of conference objects obtained from the CMT platform.

### Output Data
The script generates a `conferences.csv` file with the following columns:
- **Name**: The full name of the conference.
- **ShortName**: The abbreviated name or URL segment of the conference.
- **StartDate**: The start date of the conference.
- **City**: The city where the conference is held.
- **Country**: The country where the conference is held.
- **ExternalUrl**: The external website URL for the conference.

## Usage

1.  Ensure you have Python 3 installed.
2.  Place your raw data in a file named `conferences.txt` in the same directory as the script.
3.  Run the script:

```bash
python3 extract_conferences.py
```

4.  The `conferences.csv` file will be created in the same directory.

## Requirements

- Python 3.x
- Standard libraries: `json`, `csv`, `os`
