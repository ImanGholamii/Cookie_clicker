from time import sleep, time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument('--window-size=600,700')
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')


def accept_cookies(time: int):
    """Accept the web cookies."""
    try:
        print("Looking for the cookie consent button...")
        # Wait for the cookie consent button to be clickable
        consent_btn = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p'))
        )

        # Click the button if it is found
        if consent_btn:
            print("Cookie consent button found! Clicking it...")
            consent_btn.click()
            sleep(1)
        else:
            print("Cookie consent button not found.")
    except Exception as e:
        print(f"Error while accepting cookies: {e}")


def send_alert(message):
    # Display a message to the user in the browser
    driver.execute_script(f'{message};')
    sleep(3)
    # Wait for the user to close the alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # Close the alert
    sleep(1)


def load_previous_game(code):
    """Loading previous game"""

    sleep(1)
    option_btn = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
    option_btn.click()
    sleep(1)
    import_code = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Import save'))
    )
    import_code.click()
    sleep(1)
    paste_code = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'textareaPrompt'))
    )
    paste_code.send_keys(code)
    sleep(1.5)
    load_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="promptOption0"]'))
    )
    load_btn.click()

    sleep(1)
    option_btn = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
    option_btn.click()
    sleep(1)


def save_game():
    """Copy and Save Recovery code"""
    sleep(1)
    option_btn = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
    option_btn.click()
    sleep(1.5)
    export_save_code = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Export save'))
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
    done_btn = WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="promptClose"]'))
    )
    done_btn.click()
    send_alert('alert("Your Save code has been copied to the clipboard and recovery_code.txt!")')
    option_btn = driver.find_element(By.XPATH, '//*[@id="prefsButton"]/div')
    option_btn.click()


def set_timeout():
    """Get code execution time(default 1 minute)"""
    script = '''
        var input = window.prompt('How many minutes do you want it to work?', '1');
        navigator.clipboard.writeText(input);
        return input
    '''
    driver.execute_script(script)
    sleep(5)
    user_input = pyperclip.paste()  # clipboard content
    sleep(2)
    print(f"User input: {user_input}")
    if user_input is None or user_input.strip() == '':
        print("No input provided, using default value of 1 minute.")
        duration_minutes = 1
        sleep(1)
    else:
        try:
            duration_minutes = int(user_input)
            sleep(1)
        except ValueError:
            print("Invalid input! Using default value of 1 minute.")
            duration_minutes = 1
            sleep(1)

    duration_seconds = duration_minutes * 60
    sleep(1)
    return duration_seconds


def click_on_cookie():
    """Find and click on cookie infinitely, and save process"""
    cookie = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'bigCookie'))
    )
    start_time = time()
    number = 0
    timeout = set_timeout()
    while time() < start_time + timeout:
        cookie.click()
        number += 1
        if number % 600 == 0:
            save_game()


def select_lng():
    eng_btn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.ID, 'langSelect-EN'))
    )
    eng_btn.click()


def main():
    accept_cookies(20)

    send_alert('alert("Privacy message Must be Close by Yourself!")')

    select_lng()

    send_alert('alert("Privacy message Must be Close by Yourself!")')

    accept_cookies(5)

    try:
        with open(file='recovery.txt', mode='r') as f:
            code = f.read()
            recovery_code = code.split('=')[1]
    except FileNotFoundError:
        save_game()

    load_previous_game(code=recovery_code)

    click_on_cookie()


if __name__ == '__main__':
    main()
