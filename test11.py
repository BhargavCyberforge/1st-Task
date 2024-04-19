# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from openpyxl import Workbook
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import ActionChains


# # Set up Chrome WebDriver
# chrome_options = Options()
# chrome_driver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"
# driver = webdriver.Chrome(options=chrome_options)

# # Website URL
# url = "https://investors.confluence.vc/ar-vr"

# # Open the webpage
# driver.get(url)
# # Wait for the page to loa
# input("Enter to start Extracting")

# # Find the elements with the specified column ids
# column_elements1 = driver.find_elements(By.CSS_SELECTOR, f'h1[data-id="_i7sulsj9u"]')
# column_elements2 = driver.find_elements(By.CSS_SELECTOR, f'div[data-id="_i7sulsj9u12"]')
# column_elements3 = driver.find_elements(By.CSS_SELECTOR, f'div[data-id="_kbtr0o72812"]')
# column_elements4 = driver.find_elements(By.CSS_SELECTOR, f'div[data-type="staticImage"]')
# column_elements5 = driver.find_elements(By.CSS_SELECTOR, 'div.sw-js-single-item-elements.w-100 div.sw-pre-image-container')

# data1, data2,data3,data4,data5 = [],[],[],[],[]

# # Extract data from elements
# data1 = [element.text for element in column_elements1]
# data2 = [element.text for element in column_elements2]
# data3 = [element.text for element in column_elements3]
# data4 = [element.get_attribute('data-value') for element in column_elements4]

# print(len(column_elements5))
# data5 = []
# for element in column_elements5:
#     try:
#         x = element.find_element(By.CSS_SELECTOR, 'span[data-type="image"]')
#         data5.append(x.get_attribute('data-value'))
#     except Exception as e:
#         print('logo not found')
#         data5.append(' ')
# # Create a new Excel workbook
# wb = Workbook() 
# ws = wb.active

# # Write data to Excel sheet
# for i, (value1, value2, value3, value4, value5) in enumerate(zip(data1, data2, data3, data4, data5), start=1):
#     ws.cell(row=i, column=1, value=value1)
#     ws.cell(row=i, column=2, value=value2)
#     ws.cell(row=i, column=3, value=value3)
#     ws.cell(row=i, column=4, value=value4)
#     ws.cell(row=i, column=5, value=value5) 

# # Save the workbook
# wb.save("Ar-Vr.xlsx")
# # Quit the driv
# driver.quit()


# class="collection-list-item w-dyn-item"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
# Set up Chrome WebDriver
chrome_options = Options()
chrome_driver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"
driver = webdriver.Chrome(options=chrome_options)

# URL of the website containing the links to the person's profiles
url = "https://www.nycfounderguide.com/investors/usv"  # Replace "example.com" with the actual URL
driver.get(url)




name = driver.find_element(By.XPATH, "//h1").text.strip()
bio = driver.find_element(By.XPATH, "//div[@class='content-width-medium']").text.strip()
link = driver.find_element(By.XPATH, "//a").get_attribute("href")

data_elements = driver.find_elements(By.XPATH, "//div[@class='w-layout-grid grid-fifths']/div")

time.sleep(10)
# Organize data into a dictionary
data = {}
for element in data_elements:
    heading = element.find_element(By.XPATH, ".//h6").text.strip()
    value = element.find_element(By.XPATH, ".//div[@class='profile-info-column']").text.strip()
    data[heading] = value

# Combine name, bio, link, and data into a dictionary
output_data = {"Name": name, "Bio": bio, "Link": link}
output_data.update(data)

print(name, bio, data)
# Convert dictionary to DataFrame
df = pd.DataFrame([output_data])

# Write DataFrame to Excel file           wb.save(f"{url.split('/')[-1]}.xlsx"
#df.to_excel("founderguide.xlsx", index=False)
df.to_excel(f"{url.split('/')[-1]}.xlsx")

# Close the WebDriver
driver.quit()