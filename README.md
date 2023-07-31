# Web Scraping Bridgestone Tire Sizes

This Python script is used for web scraping tire sizes and the counts of each tire size from the Bridgestone website using the Selenium WebDriver and BeautifulSoup.

The script also uses multiprocessing to increase the speed of scraping by handling different tire diameters concurrently.

## Setup

1. Ensure Python 3 is installed on your system.

2. Install the required Python packages by running the following commands:

pip install beautifulsoup4
pip install selenium

# Web Scraping Bridgestone Tire Sizes

This Python script is used for web scraping tire sizes and the counts of each tire size from the Bridgestone website using the Selenium WebDriver and BeautifulSoup.

The script also uses multiprocessing to increase the speed of scraping by handling different tire diameters concurrently.

## Setup

1. Ensure Python 3 is installed on your system.

2. Install the required Python packages by running the following commands:

pip install beautifulsoup4
pip install selenium
Download the appropriate ChromeDriver from [this link](https://sites.google.com/a/chromium.org/chromedriver/downloads) and specify its path in the script.
Running the script
To run the script, use the following command in your terminal:
python bridgestone.py

Replace "script_name.py" with the name of your Python file.

Output
The script will create an output.csv file containing the tire sizes, counts, and corresponding URLs for each size.

The last row in the CSV file will contain the total time taken for the script to run, in the format "X minutes Y seconds".

Note
The script uses the Chrome browser in headless mode for web scraping. Ensure that the Chrome browser is installed on your system and the path to the Chrome binary in the script matches the installation path on your system.

This README.md will provide all the information needed to run your script properly.