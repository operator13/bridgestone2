import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

# Function to get tire counts for a given diameter URL
def get_tire_counts(driver, diameter_url):
    driver.get(diameter_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all('a', class_='button button--secondary', href=True)  # Find all tire size links on the page
    tire_counts = []
    for link in links:
        tire_size = link.text.strip()  # Extract tire size from the link text
        if re.match(r'^\d+/\d+R\d+$', tire_size):  # Check if tire size matches pattern
            try:
                tire_size_url = 'https://www.bridgestonetire.com' + link['href']  # Append the base URL to the extracted link
                driver.get(tire_size_url)
                time.sleep(2)  # Wait for 2 seconds
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                count_section = soup.find('div', class_='tsr-profile__results')
                count_text = count_section.text.split() if count_section else []
                count = 0 if not count_text else int(count_text[0])
                tire_counts.append((tire_size, count, tire_size_url))
            except Exception as e:
                print(f"Failed to process tire size link: {link['href']}. Error: {e}")
    return tire_counts

def main():
    # Define path to Chrome binary
    chrome_options = Options()
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    # Enable Headless mode
    chrome_options.add_argument("--headless")

    # Specify the Chrome driver path
    driver_service = Service('/usr/local/bin/chromedriver')  # replace with your path
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    # Define initial URL
    initial_url = 'https://www.bridgestonetire.com/size/'

    # Define a list of diameters
    diameters = ['22-inch', '21-inch', '20-inch', '19-inch', '18-inch', '17-inch', '16-inch', '15-inch', '14-inch']

    # Open CSV file to write the output
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tire Size", "Tire Count", "URL"])  # Write header

        # Iterate through each diameter
        for diameter in diameters:
            diameter_url = initial_url + diameter
            tire_counts = get_tire_counts(driver, diameter_url)  # Get tire counts for this diameter
            for tire_size, tire_count, tire_size_url in tire_counts:
                writer.writerow([tire_size, tire_count, tire_size_url])  # Write to CSV

    # Close the driver after we're done
    driver.close()

if __name__ == "__main__":
    main()