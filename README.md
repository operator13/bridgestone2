**Bridgestone Tire Scraper**
This Python script is used to scrape tire count data from the Bridgestone website. The script uses Selenium WebDriver with Google Chrome in headless mode and BeautifulSoup to parse the HTML.

**How it Works**
The script iterates through a predefined list of tire diameters and navigates to each respective page on the Bridgestone website. On each diameter page, it finds all tire sizes and navigates to each tire size page. The script then finds the count of tires available for that size and records this along with the tire size and URL. This information is written to a CSV file.

**Requirements**
Python 3
Selenium WebDriver
BeautifulSoup
Google Chrome
ChromeDriver

**Instructions:**
1. Install the required Python packages if you haven't already:
    **pip install selenium beautifulsoup4**

2. Download the ChromeDriver that matches your installed Google Chrome version. Place the chromedriver binary in a location of your choosing.

3. Update the path to the chromedriver binary in the script:
    **driver_service = Service('/usr/local/bin/chromedriver')**  # replace with your path

4. Run the bridgestone.py

5. After the script has finished, you will find an output.csv file in the same directory as the script. This file contains the tire size, tire count, and URL for each tire size for each tire diameter.

**Note**
The script uses headless mode for Chrome, meaning it runs the browser in the background without a user interface. If you wish to disable this, simply comment out or remove the line:

**chrome_options.add_argument("--headless")**


