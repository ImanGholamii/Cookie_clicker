from time import sleep

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--window-size=600,700')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

# select lng
eng_btn = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
)
eng_btn.click()

# make a save address. COPY and Save it to use later
sleep(1)
option_btn = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
option_btn.click()
sleep(1)
export_save_code = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="menu"]/div[3]/div/div[4]/a[1]'))
)
export_save_code.click()

# Wait for the prompt and extract the save code
save_code = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="textareaPrompt"]'))
).text

# Copy recovery code to clipboard using pyperclip
pyperclip.copy(save_code)
code = pyperclip.paste()
with open(file='recovery.txt', mode='w') as f:
    f.write(f"recovery code={code}")
# Display a message to the user in the browser
sleep(1)
done_btn = WebDriverWait(driver, timeout=60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="promptClose"]'))
)
done_btn.click()
sleep(1)
driver.execute_script('alert("Your Save code has been copied to the clipboard and recovery_code.txt!");')
sleep(3)
cookie = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, 'bigCookie'))
)
for i in range(10):
    cookie.click()
## TODO1 write the code in a file
## TODO2 find cookie and write codes to click it for 5 minutes or a time
## TODO3 remove quit to manage it by user
# driver.quit()
