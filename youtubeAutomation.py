from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Automatically download and install the correct version of ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open YouTube
driver.get("https://www.youtube.com")

# Wait for page load
time.sleep(3)

# Locate the search bar
search_bar = driver.find_element(By.NAME, "search_query")

# Enter the search query
search_query = "recent development in python"
search_bar.send_keys(search_query)

# Press Enter
search_bar.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(5)

# Find the first video in the search results
first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')

# Click on the first video
first_video.click()

# Wait for the video to load
time.sleep(5)

# Switch to fullscreen
try:
    # Locate the fullscreen button
    fullscreen_button = driver.find_element(By.CSS_SELECTOR, 'button.ytp-fullscreen-button')
    fullscreen_button.click()
except Exception as e:
    print(f"Error while trying to click fullscreen button: {e}")

# Optional: Wait for a while to observe fullscreen (e.g., 10 seconds)
time.sleep(10)

# Close the browser
driver.quit()
