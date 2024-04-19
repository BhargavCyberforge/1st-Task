



'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time


chrome_options = Options()
chrome_driver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"
driver = webdriver.Chrome(options=chrome_options)

url = "https://climatescape.org/organizations/offsetra"

driver.get(url)
# Wait for the page to load here if necessary

# Find the elements with the specified column ids
name_f = driver.find_elements(By.CSS_SELECTOR, f'h1[class="flex-grow text-xl font-semibold"]')
brief_f = driver.find_elements(By.CSS_SELECTOR, f'p')
description_f = driver.find_elements(By.CSS_SELECTOR, f'div[class="my-6"]')
address_f = driver.find_elements(By.CSS_SELECTOR, f'ul')

links_text = driver.find_elements(By.CSS_SELECTOR, f'a[target="_blank"]')

links_f = driver.find_elements(By.CSS_SELECTOR, f'a[class="underline hover:text-gray-600 inline-flex"]')

  

# Extract data from elements
organisations_data = []
for element in zip(name_f, brief_f, description_f, address_f, links_text, links_f):
    name = element[0].text
    brief = element[1].text
    description = element[2].text
    address = element[3].text
    links_text = element[4].text
    links = element[5].get_attribute('href')
    organisations_data.append({"Name": name, "Brief": brief, "Description": description, "IN A SNAPSHOT": address, "Link": links_text, "Links": links})
    print(organisations_data)



# Create a new Excel workbook
wb = Workbook()
ws = wb.active

# Write data to Excel sheet
ws.append(["Name", "Brief", "Description", "IN A SNAPSHOT", "Link", "Links"])
for organisation in organisations_data:
    ws.append([organisation["Name"], organisation["Brief"], organisation["Description"], organisation["IN A SNAPSHOT"], organisation["Link"], organisation["Links"]])

# Save the workbook
wb.save(f"{url.split('/')[-1]}.xlsx")
input("done")

# Quit the driver
driver.quit()
'''




###




'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook

chrome_options = webdriver.ChromeOptions()
chrome_driver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"
driver = webdriver.Chrome(options=chrome_options)

url = "https://climatescape.org/organizations/offsetra"
driver.get(url)

# Find elements for each column
columns = driver.find_elements(By.CSS_SELECTOR, 'div.flex.flex-col.mb-8')

# Initialize a list to store the scraped data
data = []

# Iterate over each column
for column in columns:
    # Find all the items within the column
    items = column.find_elements(By.CSS_SELECTOR, 'a.underline.hover\:text-gray-600.inline-flex')
    
    # Extract and store data for each item
    for item in items:
        name = column.find_element(By.CSS_SELECTOR, 'h1.flex-grow.text-xl.font-semibold').text
        brief = column.find_element(By.CSS_SELECTOR, 'p').text
        description = column.find_element(By.CSS_SELECTOR, 'div.my-6').text
        snapshot = item.text
        link = item.get_attribute('href')
        
        # Append data to the list
        data.append({"Name": name, "Brief": brief, "Description": description, "IN A SNAPSHOT": snapshot, "Link": link})

# Create a new Excel workbook
wb = Workbook()
ws = wb.active

# Write data to Excel sheet
ws.append(["col1", "col2", "col3", "col4", "col5"])
for item in data:
    ws.append([item["Name"], item["Brief"], item["Description"], item["IN A SNAPSHOT"], item["Link"]])

# Save the workbook
wb.save("data.xlsx")

# Quit the driver
driver.quit()'''









from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import pandas as pd
import time

# Set up Chrome WebDriver
chrome_options = Options()
chrome_driver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"  # Path to chromedriver
driver = webdriver.Chrome(options=chrome_options)

# URL of the investor profile
url = "https://signal.nfx.com/investors/andrea-zurek"
driver.get(url)

time.sleep(10)
# Wait for the elements to be present
wait = WebDriverWait(driver, 10)
name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.f3.f1-ns.mv1')))
# Find the link element
link_element = driver.find_element(By.XPATH, "//span[@class='mr3']/a")
address_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.ml1')))
investing_profile_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "line-separated-row")]/div/span')))
sector_and_stage_rankings_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.vc-list-chip')))



# Extract data
name = name_element.text.strip()
link = link_element.get_attribute('href')
address = address_element.text.strip()
investing_profile = [elem.text.strip() for elem in investing_profile_elements]
sector_and_stage_rankings = [elem.text.strip() for elem in sector_and_stage_rankings_elements]

# Extract text from sector and stage ranking elements

# # Print the extracted text
# for ranking in sector_and_stage_rankings:
#     print(ranking)
print(link)
# for inve in investing_profile:
#     print(inve)
#print(sector_and_stage_rankings_elements)

investor_data = {
    'Name': name,
    'Link_URL': link,
    'Address': address,
    'Current Investing Position': investing_profile[1],#split(" ")[0],
    'Investment Range': investing_profile[3],
    'Sweet Spot': investing_profile[5],
    'Investments on Records': investing_profile[7],
    'Current Fund Size': investing_profile[9],
    'Sector and Stage Ranking': ', '.join(sector_and_stage_rankings),
}

# Convert scraped data into a DataFrame
df = pd.DataFrame([investor_data])

# Write DataFrame to Excel file
df.to_excel("investor_data.xlsx", index=False)

# Close the WebDriver
driver.quit()



