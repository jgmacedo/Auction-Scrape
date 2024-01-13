import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.support.ui import Select
import time

# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Define the download directory (inside the script's directory)
download_directory = os.path.join(script_directory, "downloads")

# Create the download directory if it doesn't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Set Chrome options for automatic download
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Path to chromedriver (assuming it's in the same directory as the script)
driver_path = os.path.join(script_directory, 'chromedriver')

# Initialize the Chrome WebDriver using Service
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the webpage
driver.get('https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp')

# Locate the dropdown element
dropdown_element = driver.find_element(By.ID, 'cmb_estado')
dropdown = Select(dropdown_element)

states_list = ['DF', 'GO']

# Iterate through each option in the dropdown
for option in states_list:
    # Select the option
    dropdown.select_by_visible_text(option)

    # Find and click the 'Next' button to initiate the download
    next_button = driver.find_element(By.ID, 'btn_next1')
    next_button.click()

    # Wait for the download to start or complete
    time.sleep(0.5)  # Adjust the timing based on your network speed and file size

    # You might need to navigate back to the dropdown page after each download
    driver.get('https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp')
    dropdown_element = driver.find_element(By.ID, 'cmb_estado')
    dropdown = Select(dropdown_element)

# Close the browser after all downloads are initiated
driver.quit()
