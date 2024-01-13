from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Base URL of the website
base_url = 'https://www.leilaoimovel.com.br/encontre-seu-imovel?s=&estado=53,52&pag='
driver = webdriver.Firefox()  # Ensure chromedriver is in your PATH or specify the path

# Open the CSV file to write the data
with open('properties.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link', 'Last Price', 'Discount Price', 'Address'])

    # Iterate over the pages
    for page in range(1, 11):  # Update the range as needed
        url = base_url + str(page)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all 'place-box' elements
        place_boxes = soup.find_all('div', class_='place-box')

        for box in place_boxes:
            link_element = box.find('a', class_='Link_Redirecter')
            link = link_element['href'] if link_element else 'No link found'

            last_price_element = driver.find_element(By.CSS_SELECTOR, '.last-price')
            last_price = last_price_element.text.strip() if last_price_element else 'No last price found'

            discount_price_element = box.find('div', class_='discount-price font-1')
            discount_price = discount_price_element.text.strip() if discount_price_element else 'No discount price found'

            address_element = box.find('span', class_='address')
            address = address_element.text.strip() if address_element else 'No address found'

            # Write the extracted information to the CSV file
            writer.writerow([link, last_price, discount_price, address])

driver.quit()
print("Data extraction complete. Check the 'properties.csv' file.")
