

#this is for manually printing the links


# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# # URL of the webpage
# url = "https://signal.nfx.com/investor-lists/top-marketplaces-seed-investors"

# try:
#     # Add headers to mimic a real browser request
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
#     }

#     # Send a GET request to the webpage with headers
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         print("Webpage retrieved successfully.")

#         # Parse the HTML content
#         soup = BeautifulSoup(response.content, "html.parser")

#         # Find all <a> tags with href attribute
#         links = soup.find_all("a", href=True)

#         # List to store the found links
#         found_links = []

#         if links:
#             print("Links found on the page:")
#             for link in links:
#                 href = link.get("href")
#                 print(href)
#                 found_links.append(href)
#         else:
#             print("No links found on the page.")

#         # Create a DataFrame with the found links
#         df = pd.DataFrame({"Links": found_links})

#         # Save the DataFrame to an Excel file
#         excel_filename = "found_links.xlsx"
#         df.to_excel(excel_filename, index=False)
#         print(f"Links saved to {excel_filename}")

#     else:
#         print("Failed to retrieve the webpage. Status code:", response.status_code)

# except Exception as e:
#     print("An error occurred:", e)



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


# Path to your ChromeDriver executable
chromedriver_path = r"/home/bhargav/Downloads/chromedriver-linux64 (1)/chromedriver-linux64"

# Create a Service object with the Chrome driver path
service = Service(chromedriver_path)
chrome_options = Options()

# Open a new Chrome window
driver = webdriver.Chrome(options=chrome_options)

# Open the login page
login_url = "https://auth.nfx.com/login?state=hKFo2SB4dVBnT0RVX1NXTkNWN0RZYkJjNEw3d3ctc1loLUpqeaFupWxvZ2luo3RpZNkgQW9lQU9CTzFfaExHbHRpN1ZYZjhDYXplTktFLXlxMFKjY2lk2SBWaTJFd28wblc2ZmxLUXpPME5CYzhFMFl2ZUJqaktsVQ&client=Vi2Ewo0nW6flKQzO0NBc8E0YveBjjKlU&protocol=oauth2&audience=https%3A%2F%2Fnfxsignal-production.auth0.com%2Fapi%2Fv2%2F&scope=openid%20email%20profile&response_type=token%20id_token&redirect_uri=https%3A%2F%2Fsignal.nfx.com%2Flogin&connection=username-password&login_hint=&connection_scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fgmail.metadata&access_type=offline&nonce=qRKhIyTOyYpyL9zEvzBLr._S65juHQqS&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMC4xIn0%3D"
driver.get(login_url)

# Wait for login to complete (Manually)
print("Please complete the login manually. After login, press enter here.")

input("Press enter to continue...")

print("Login completed. Navigating to investors page...")

# URL of the webpage
url = "https://signal.nfx.com/investors"

# Open the webpage
driver.get(url)

# Set a timeout for link retrieval
timeout = 30  # seconds

# Wait for all anchor tags (links) to be present
wait = WebDriverWait(driver, timeout)

try:
    print(f"Waiting for links to load (timeout: {timeout} seconds)...")
   
    # Retry mechanism to handle stale element reference error
    retries = 3
    for _ in range(retries):
        try:
            links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@href]")))
            links_list = [link.get_attribute("href") for link in links]
            break
        except Exception as e:
            print(f"Encountered a stale element reference. Retrying...")
            time.sleep(2)  # Wait for a moment before retrying
            # Refresh the list of links and retry
            links = driver.find_elements(By.XPATH, "//a[@href]")
    else:
        raise RuntimeError("Error occurred while retrieving links: Max retries exceeded")
    
    # Continue with the rest of the code as before
    all_links = []  # List to store all links found
   
    if links_list:
        print("Links found after manual login:")
        for link in links_list:
            print(link)
            all_links.append(link)
           
            # Navigate to the link and find links within it
            driver.get(link)
            try:
                inner_links = driver.find_elements(By.XPATH, "//a[@href]")
                if inner_links:
                    print("Links found within this link:")
                    for inner_link in inner_links:
                        inner_link_url = inner_link.get_attribute("href")
                        print(inner_link_url)
                        all_links.append(inner_link_url)
                else:
                    print("No links found within this link.")
            except Exception as e:
                print(f"Error occurred while retrieving inner links: {e}")
               
            print()  # Add a newline for readability
           
            # Sleep for a moment to avoid being detected as a bot
            time.sleep(1)
    else:
        print("No links found after manual login.")
       
    # Print all links found
    print("All links found:")
    for link in all_links:
        print(link)
        print(len(all_links))

    # Save links to Excel file
    wb = Workbook()
    ws = wb.active

    for i, link in enumerate(all_links, start=1):
        ws.cell(row=i, column=1, value=link)

    wb.save("ALL_LINKS.xlsx")
    print("Links saved to ALL_LINKS.xlsx")
    
except Exception as e:
    print(f"Error occurred while retrieving links: {e}")

# Quit the driver
driver.quit()









