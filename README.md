# Real-Time Property Data for Cary, NC

This project provides real-time property data for single-family homes and townhomes for sale in Cary, North Carolina. It leverages web scraping techniques to gather up-to-date listings and presents the information in a structured format.

## Features

* **Real-Time Data:** Fetches the latest property listings.
* **Location Specific:** Targets properties specifically in Cary, NC.
* **Property Type Filter:** Focuses on single-family homes and townhomes.
* **For Sale Listings:** Retrieves only properties currently for sale.
* **Data Export:** Exports the collected data to a CSV file for easy analysis.

## Technologies Used

* **Python:** The core programming language.
* **`homeharvest`:** Web scraping library for property data.
* **`requests`:** For making HTTP requests.
* **`beautifulsoup4`:** For parsing HTML content.
* **`pandas`:** For data manipulation and CSV export.
* **`datetime`:** For generating timestamped filenames.

## Setup

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/msucse2004/realtor.git
   cd realtor
   ```

2. **Create a virtual environment (recommended):**
   
   ```bash
   conda env create -f env_morrisville.yml
   ```

## Usage

1. **Run the script:**
   
   ```bash
   python main.py
   ```

2. **Output:**
   
   * The script will output the number of properties found.
   * A CSV file named `HomeHarvest_[timestamp].csv` will be created in the project directory, containing the property data.
   * The first few rows of the pandas dataframe will be printed to the terminal.

## Code Explanation

```python

```

# Git Usages

1. **Update the latest codes:**
   
   ```bash
   git stash
   git pull
   git stash pop
   ```

2. **Push the codes:**
   
   ```bash
   git status
   git add .
   git commit -m "comments"
   git push
   ```