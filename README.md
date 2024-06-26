# Security-Intelligence-Analysis

## Project Overview
This project aims to analyze and correlate security threats between Security Intelligence logs pulled from Cisco Firepower Management Center and logs from Cisco Umbrella for user site access. The goal is to identify any common security threats and list them along with their associated CVEs (Common Vulnerabilities and Exposures).

## Features
- **Data Extraction**: Extracts data from PDF reports using `tabula-py`.
- **Data Cleaning**: Cleans and organizes the extracted data using `pandas`.
- **Threat Correlation**: Identifies and correlates security threats between the two data sources.
- **CVE Lookup**: Searches for CVEs associated with identified threats.

## Project Structure
- `script.py`: The main script that processes and correlates the data.
- `README.md`: Project documentation (this file).
- `requirements.txt`: List of Python dependencies required for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/Jillian2003/Security-Intelligence-Analysis.git
   cd Security-Intelligence-Analysis
2. **Install the required Python packages**:
   ```sh
   pip install -r requirements.txt


## Usage
1. Convert the PDF reports from Cisco Firepower and Umbrella to CSV using tabula-py:
   - Place the PDF files in the project directory.
   - Run the tabula-py commands to convert the PDFs to CSVs.
    
2. Run the script:

    ```sh
    python script.py

## Dependencies
   - pandas: Data manipulation and analysis library.
   - tabula-py: Library for extracting tables from PDF files.

You can install these dependencies using:
    ```sh
    pip install pandas tabula-py 

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
