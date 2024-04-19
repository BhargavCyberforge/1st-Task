
'''
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

# List of investor profile URLs
profile_urls = [
    "https://signal.nfx.com/investor-lists/top-agtech-pre-seed-innvestors",
    # Add more profile URLs here...
]

# Create an empty DataFrame to store scraped data
all_investor_data = pd.DataFrame(columns=[
    'Name', 'Link_URL', 'Address', 'Current Investing Position',
    'Investment Range', 'Sweet Spot', 'Investments on Records',
    'Current Fund Size', 'Sector and Stage Ranking'
])

# Loop through each profile URL
for url in profile_urls:
    # Navigate to the investor profile URL
    driver.get(url)
    
    time.sleep(20)  # Add a short delay to ensure page loads completely
    
    # Wait for the elements to be present
    wait = WebDriverWait(driver, 20)
    name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.f3.f1-ns.mv1')))
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

    # Create a dictionary to store the scraped data
    investor_data = {
        'Name': name,
        'Link_URL': link,
        'Address': address,
        'Current Investing Position': investing_profile[1],
        'Investment Range': investing_profile[3],
        'Sweet Spot': investing_profile[5],
        'Investments on Records': investing_profile[7],
        'Current Fund Size': investing_profile[9],
        'Sector and Stage Ranking': ', '.join(sector_and_stage_rankings),
    }

    # Append the investor data to the DataFrame
    all_investor_data = all_investor_data.append(investor_data, ignore_index=True)

# Write DataFrame to Excel file
all_investor_data.to_excel("all_investor_data.xlsx", index=False)

# Close the WebDriver
driver.quit()
'''







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


'''
time.sleep(10)
# Wait for the elements to be present
wait = WebDriverWait(driver, 10)
name_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.content-width-medium')))
Bio_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.content-width-medium')))
link_element = driver.find_element(By.CSS_SELECTOR, f'a[class="margin-top"]')
stage_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "profile-info-column")]/div/div')))
# location_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.profile-info-column')))
# Avg_check_size_elements = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.profile-info-column')))
# sectors_elements = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.profile-info-column')))
# Lead_follow = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.profile-info-column')))

# Extract data
name = name_element.text.strip()
Bio = Bio_element.text.strip()
link = link_element.get_attribute('href')
#Location = location_element.text.strip()
investing_profile = [elem.text.strip() for elem in stage_element]
#sector_and_stage_rankings = [elem.text.strip() for elem in sector_and_stage_rankings_elements]


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
    'Link': link,
    'Stage': investing_profile[1],
    'Location': investing_profile[3],#split(" ")[0],
    'Average_Check_SIze': investing_profile[5],
    'Sectors': investing_profile[7],   ###', '.join(sector_and_stage_rankings)
    'Lead_Follow': investing_profile[9]
}

# Convert scraped data into a DataFrame
df = pd.DataFrame([investor_data])
'''


# link = ['https://www.nycfounderguide.com/investors/primary-venture-partners',
#         'https://www.nycfounderguide.com/investors/lerer-hippeau',
#         'https://www.nycfounderguide.com/investors/work-bench',
#         'https://www.nycfounderguide.com/investors/notation-capital',
#         'https://www.nycfounderguide.com/investors/firstmark',
#         'https://www.nycfounderguide.com/investors/operator-partners',
#         'https://www.nycfounderguide.com/investors/bleu-capital',
#         'https://www.nycfounderguide.com/investors/animo-ventures',
#         'https://www.nycfounderguide.com/investors/sterling-vc',
#         'https://www.nycfounderguide.com/investors/first-round-capital',
#         'https://www.nycfounderguide.com/investors/h-l-ventures',
#         'https://www.nycfounderguide.com/investors/riverpark-ventures',
#         'https://www.nycfounderguide.com/investors/boldstart-ventures',
#         'https://www.nycfounderguide.com/investors/inspired-capital',
#         'https://www.nycfounderguide.com/investors/645-ventures',
#         'https://www.nycfounderguide.com/investors/red-sea-ventures',
#         'https://www.nycfounderguide.com/investors/rosecliff-ventures',
#         'https://www.nycfounderguide.com/investors/usv',
#         'https://www.nycfounderguide.com/investors/differential-venture-partners',
#         'https://www.nycfounderguide.com/investors/nextview-ventures',
#         'https://www.nycfounderguide.com/investors/story-ventures',
#         'https://www.nycfounderguide.com/investors/bbg-ventures',
#         'https://www.nycfounderguide.com/investors/boxgroup',
#         'https://www.nycfounderguide.com/investors/greycroft',
#         'https://www.nycfounderguide.com/investors/torch-capital',
#         'https://www.nycfounderguide.com/investors/valia-ventures',
#         'https://www.nycfounderguide.com/investors/gabby-slome',
#         'https://www.nycfounderguide.com/investors/great-oaks',
link = ['https://www.nycfounderguide.com/investors/scott-belsky',#####
        'https://www.nycfounderguide.com/investors/female-founders-fund',
        'https://www.nycfounderguide.com/investors/schlaf',
        'https://www.nycfounderguide.com/investors/dan-teran',
        'https://www.nycfounderguide.com/investors/dash-fund',
        'https://www.nycfounderguide.com/investors/eniac-ventures',
        'https://www.nycfounderguide.com/investors/jenny-fleiss',
        'https://www.nycfounderguide.com/investors/nyca',
        'https://www.nycfounderguide.com/investors/supernode-ventures',
        'https://www.nycfounderguide.com/investors/tribeca-venture-partners',
        'https://www.nycfounderguide.com/investors/indicator-ventures',
        'https://www.nycfounderguide.com/investors/the-venture-collective',
        'https://www.nycfounderguide.com/investors/good-friends',
        'https://www.nycfounderguide.com/investors/alpaca',
        'https://www.nycfounderguide.com/investors/bfv',
        'https://www.nycfounderguide.com/investors/brand-project',
        'https://www.nycfounderguide.com/investors/fj-labs',
        'https://www.nycfounderguide.com/investors/metaprop',
        'https://www.nycfounderguide.com/investors/harlem-capital',
        'https://www.nycfounderguide.com/investors/third-prime',
        'https://www.nycfounderguide.com/investors/human-ventures',
        'https://www.nycfounderguide.com/investors/alleycorp',
        'https://www.nycfounderguide.com/investors/bertelsmann-digital-media-investments',
        'https://www.nycfounderguide.com/investors/iaventures',
        'https://www.nycfounderguide.com/investors/michael-katz',
        'https://www.nycfounderguide.com/investors/new-york-angels',
        'https://www.nycfounderguide.com/investors/new-york-venture-partners',
        'https://www.nycfounderguide.com/investors/josh-hix',
        'https://www.nycfounderguide.com/investors/anthemis',
        'https://www.nycfounderguide.com/investors/courtside-ventures',
        'https://www.nycfounderguide.com/investors/equal-ventures',
        'https://www.nycfounderguide.com/investors/tech-council-ventures',
        'https://www.nycfounderguide.com/investors/vast-ventures',
        'https://www.nycfounderguide.com/investors/overton',
        'https://www.nycfounderguide.com/investors/dune-ventures',
        'https://www.nycfounderguide.com/investors/ocean-ventures',
        'https://www.nycfounderguide.com/investors/cowboy',
        'https://www.nycfounderguide.com/investors/expansion-vc',
        'https://www.nycfounderguide.com/investors/kw-angel-fund',
        'https://www.nycfounderguide.com/investors/ldv-capital',
        'https://www.nycfounderguide.com/investors/fintech-ventures-fund',
        'https://www.nycfounderguide.com/investors/gvc-partners',
        'https://www.nycfounderguide.com/investors/ground-up-ventures',
        'https://www.nycfounderguide.com/investors/loeb-nyc',
        'https://www.nycfounderguide.com/investors/reshape',
        'https://www.nycfounderguide.com/investors/revel-partners',
        'https://www.nycfounderguide.com/investors/ff-venture-capital',
        'https://www.nycfounderguide.com/investors/ben-zises',
        'https://www.nycfounderguide.com/investors/brooklyn-bridge-ventures',
        'https://www.nycfounderguide.com/investors/5-to-9-ventures',
        'https://www.nycfounderguide.com/investors/elizabeth-street-ventures',
        'https://www.nycfounderguide.com/investors/silicon-badia',
        'https://www.nycfounderguide.com/investors/maveron',
        'https://www.nycfounderguide.com/investors/pjc',
        'https://www.nycfounderguide.com/investors/irrvrntvc',
        'https://www.nycfounderguide.com/investors/advancit-capital',
        'https://www.nycfounderguide.com/investors/bill-tyndall',
        'https://www.nycfounderguide.com/investors/jonathan-wasserstrum',
        'https://www.nycfounderguide.com/investors/kyle-widrick',
        'https://www.nycfounderguide.com/investors/mark-rosner',
        'https://www.nycfounderguide.com/investors/mike-constantiner',
        'https://www.nycfounderguide.com/investors/moralis-capital',
        'https://www.nycfounderguide.com/investors/overeasy-ventures',
        'https://www.nycfounderguide.com/investors/sam-huleatt',
        'https://www.nycfounderguide.com/investors/techstars-sports-accelerator',
        'https://www.nycfounderguide.com/investors/black-jays',
        'https://www.nycfounderguide.com/investors/blue-collective',
        'https://www.nycfounderguide.com/investors/camber-creek',
        'https://www.nycfounderguide.com/investors/company-ventures',
        'https://www.nycfounderguide.com/investors/michael-salmasi']


for url in link:
    driver.get(url)

    try:
        # Try to find the elements with specified XPaths
        name = driver.find_element(By.XPATH, "//h1").text.strip()
        bio = driver.find_element(By.XPATH, "//div[@class='content-width-medium']").text.strip()
        link = driver.find_element(By.XPATH, "//a").get_attribute("href")

        # Extract data elements
        data_elements = driver.find_elements(By.XPATH, "//div[@class='w-layout-grid grid-fifths']/div")

        # Organize data into a dictionary
        data = {}
        for element in data_elements:
            heading = element.find_element(By.XPATH, ".//h6").text.strip()
            value = element.find_element(By.XPATH, ".//div[@class='profile-info-column']").text.strip()
            data[heading] = value

        # Combine name, bio, link, and data into a dictionary
        output_data = {"Name": name, "Bio": bio, "Link": link}
        output_data.update(data)

        # Convert dictionary to DataFrame
        df = pd.DataFrame([output_data])

        # Write DataFrame to Excel file
        df.to_excel(f"{url.split('/')[-1]}.xlsx")
    except Exception as e:
        print(f"An error occurred for URL: {url}")
        print(f"Error message: {str(e)}")
        continue  # Skip to the next URL

# Close the WebDriver
driver.quit()