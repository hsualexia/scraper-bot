import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM

import pandas as pd

# Complete these 2 fields ==================
USERNAME = ''
PASSWORD = ''
# ==========================================

TIMEOUT = 15

def scrape():
    usr = input('[Required] - Whose followers do you want to scrape: ')

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--log-level=3")
    mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    bot = webdriver.Chrome(executable_path=CM().install(), options=options)
    bot.set_window_size(600, 1000)

    bot.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    print("Logging in...")

    user_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

    user_element.send_keys(USERNAME)

    pass_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(5)

    bot.get('https://www.instagram.com/{}/'.format(usr))

    time.sleep(3.5)
    
    follower_number = WebDriverWait(bot, TIMEOUT).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "a[href$='/followers/'] > div > span"))).text

    follower_number = follower_number.replace(',', '')

    time.sleep(3.5)

    WebDriverWait(bot, TIMEOUT).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, "a[href$='/followers/'] > div"))).click()

    time.sleep(5)

    total_time = 3.5 * int(follower_number) // 600

    print('Grab a cup of coffee, we are going to scroll to the end! It will take approx. {} minutes'.format(total_time))

    data = []
    reached_scroll_end = False
    last_height = bot.execute_script("return document.body.scrollHeight")

    while not reached_scroll_end:
        ActionChains(bot).send_keys(Keys.END).perform()
        time.sleep(3.5)
        new_height = bot.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
            reached_scroll_end = True
        else:
            last_height = new_height

    followers = bot.find_elements_by_tag_name('a')

    for i in followers:
        handle = i.get_attribute('href').split("/")[3]
        data.append(handle)
    
    cleanedList = list(dict.fromkeys(data))
    cleanedList.remove('accounts')
    cleanedList.remove('')
    cleanedList.remove('jdoejdoe1423')
    cleanedList.remove('explore')

    dictionary = {'userhandles': cleanedList}

    pd.DataFrame(dictionary).to_csv('{}.csv'.format(usr))

if __name__ == '__main__':
    scrape()
