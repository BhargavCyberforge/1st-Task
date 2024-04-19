
'''
from bs4 import BeautifulSoup
import requests
import time
import warnings
import re

# Suppress BeautifulSoup warning messages
warnings.filterwarnings("ignore", category=UserWarning, message="':sw-box-shadow-m' pseudo-class is not implemented at this time")
warnings.simplefilter("ignore", UserWarning)


try:
# URL of the page to extract HTML content from
    url = "https://investors.confluence.vc/advertising-marketing"

# Function to extract data from HTML content
    response = requests.get(url)
    #response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')


    #soup.div.text
    
    #soup.find_all('div')
    #print()

    #soup.get_text()
    #print()

#  #for images and the links
#   for link in soup.find_all('a'):
#      print(link.get('href'))
    


    #person1 = BeautifulSoup('<div class=js-list-item position-relative overflow-hidden p-0 flex-1 justify-content-center box sw-background-color-ffffff sw-margin-bottom-none sw-border-style-solid sw-border-width-s sw-border-color-e6e6e6 sw-border-radius-l sw-box-shadow-none hover:sw-box-shadow-m sw-cursor-default  left >', 'html.parser')
    #person_div = soup.find('div', class_='js-list-item position-relative overflow-hidden p-0 flex-1 justify-content-center box sw-background-color-ffffff sw-margin-bottom-none sw-border-style-solid sw-border-width-s sw-border-color-e6e6e6 sw-border-radius-l sw-box-shadow-none hover:sw-box-shadow-m sw-cursor-default  left')
   
    # for person in person1:
    #     txt_content = person.text.strip()
    #     print(person)
    # # if person1:
    #     div_elements = person1.find_all('div')
    #     print(div_elements)
    # else:
    #     print("Element not found")




    #tag = soup.div
    #print(tag.text)


    #all_divs = soup.find_all('div')


    #soup.find("head")
    #print()


    #soup.html.strings
    # for string in soup.strings:
    #     print(repr(string))
    #     '\n'




      #for getting only text without whitespaces
    #for string in soup.stripped_strings:
        #print(repr(string))
    #     (names = [name.text.strip() for name in soup.select('.sw-pre-need-container')]
    #     break
    # print("Names:", names))
        

    #     (locations = [location.text.strip() for location in soup.select('.sw-pre-text-container')]
    #     break
    # print("Locations:", locations))





    #sibling_soup = BeautifulSoup('<div class=sw-js-single-item-elements w-100 >', 'html.parser')
    #print(soup.div.next_siblings)


    first_element = soup.find(string=re.compile("d-flex flex-column sw-js-list-item-header"))
    for element in first_element:
        name = element.find_all_next('div', class_="sw-pre-text-container")
        print(name)
    #print(first_element)
    

except Exception as e:
    print(e)
'''  



'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from openpyxl import Workbook
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import pandas as pd


# Set up Chrome WebDriver
chrome_options = Options()
chrome_driver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"  # Path to chromedriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(options=chrome_options)


# URL of the investor profile
url = "https://signal.nfx.com/investors/eric-chen"

# Initialize Selenium WebDriver (you may need to specify the path to your webdriver executable)

driver.get(url)

# Scraping investor details
name = driver.find_element(By.CSS_SELECTOR, f'h1[class="f3.f1-ns mv1"]').text()  #).strip()
#link = driver.find_element(By.CSS_SELECTOR, f'a[class="mr3"]').text()#.strip()
address = driver.find_element(By.CSS_SELECTOR, f'span[class="ml1"]').text() #.strip()
current_investing_position = driver.find_element(By.CSS_SELECTOR, f'div[class="line-separated-row row"]').text()#.strip()
invest_range = driver.find_element(By.CSS_SELECTOR,f'div[class="line-separated-row row"]').text()
sweet_spot = driver.find_element(By.CSS_SELECTOR, f'div[class="line-separated-row row"]').text()
investments_on_record = driver.find_element(By.CSS_SELECTOR, f'div[class="line-separated-row row"]').text()
current_fund_size = driver.find_element(By.CSS_SELECTOR, f'div[class="line-separated-row row"]').text()
sector_and_stage_rankings = driver.find_elements(By.CSS_SELECTOR, f'a[class="vc-list-chip"]')#.text()

# Close the WebDriver
driver.quit()

# Create a dictionary with scraped data
investor_data = {
    'Name': name,
    'Link': link,
    'Address': address,
    'Current Investing Position': current_investing_position,
    'Investment Range': invest_range,
    'Sweet Spot': sweet_spot,
    'Investments On Record': investments_on_record,
    'Current Fund Size': current_fund_size,
    'Sector and Stage Rankings': sector_and_stage_rankings
}

# Convert scraped data into a DataFrame
df = pd.DataFrame([investor_data])

# Write DataFrame to Excel file
df.to_excel("investor_data.xlsx", index=False)
'''



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Path to your ChromeDriver executable
chromedriver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"

# URL of the webpage
url = "https://signal.nfx.com/investors"

# Initialize ChromeDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get(url)

# Wait for all anchor tags (links) to be present
wait = WebDriverWait(driver, 10)
links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@href]")))

# Extract href attribute from each link
links_list = [link.get_attribute("href") for link in links]

# Print the list of links
print(links_list)

# Close the browser
driver.quit()