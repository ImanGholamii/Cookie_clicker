from time import sleep

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from decouple import config

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

# select lng
eng_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
)
eng_btn.click()

# make a save address. COPY and Save it to use later
option_btn = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
option_btn.click()
export_save_code = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[1]'))
)
export_save_code.click()

# Wait for the prompt and extract the save code
save_code = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="textareaPrompt"]'))
).text

# Copy save code to clipboard using pyperclip
pyperclip.copy(save_code)
# Display a message to the user in the browser
driver.execute_script('alert("Your Save code has been copied to the clipboard!Save it to use it later.");')
sleep(5)

done_btn = driver.find_element(By.XPATH, '//*[@id="promptOption0"]')
done_btn.click()

driver.quit()
