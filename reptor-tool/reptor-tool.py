from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

print('Starting Rep+')

def check_exists_by_xpath(xpath):
  try:
    browser.find_element_by_xpath(xpath)
  except NoSuchElementException:
    return False
  return True

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
options.add_argument("--disable-logging")
options.add_argument("--log-level=3")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)

custom_fig = Figlet(font='slant')
print(custom_fig.renderText('Reptor'))

purl = input('\nSearch SteamRep: ')
print(f'\nSearching... This might take a while...\n')

def load_page(search_for):
  browser.get('https://steamrep.com/search?q=' + search_for)
  WebDriverWait(browser, 8).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="profileloading"]'))) # Waiting to page to load...

  main_info = browser.find_elements_by_xpath('//*[@id="steamids"]')[0].text.split("| ")

  username = main_info[1][11:]
  steam3id = main_info[2][11:]
  steamID32 = main_info[3][11:]
  steamID64 = main_info[4][11:]
  customURL = main_info[5][11:]
  steamrep = main_info[6][11:]

  acc_creation = browser.find_elements_by_xpath('//*[@id="membersince"]')[0].text
  steamlevel = browser.find_element_by_xpath('//*[@id="steamlevel"]').text
  acc_privacy = browser.find_element_by_xpath('//*[@id="privacystate"]').text
  special_rep = browser.find_element_by_xpath('//*[@id="repshield"]/img').get_attribute("alt")
  trade_ban = browser.find_element_by_xpath('//*[@id="tradebanstatus"]').text
  vac_ban = browser.find_element_by_xpath('//*[@id="vacbanned"]').text
  community_ban = browser.find_element_by_xpath('//*[@id="communitybanstatus"]').text

  info = [username, steam3id, steamID32, steamID64, customURL, steamrep, 
  acc_creation, steamlevel, acc_privacy, special_rep, trade_ban, vac_ban, community_ban]

  if any(x == '--' for x in info): # if page isn't loaded, try again, i know, it's a stupid method
    load_info(search_for)
  browser.quit()
  return info

info_out = load_page(purl)
print('Results: \n')

print(f'Steam Name: {info_out[0]}', end='')
print(f'Joined Steam: {info_out[6]}')
print(f'Steam Level: {info_out[7]}')
print(f'Profile Privacy: {info_out[8]}')
print(f'Reputation Status: {info_out[9]}')
print(f'Trade Ban: {info_out[10]}')
print(f'VAC Ban: {info_out[11]}')
print(f'Community Ban: {info_out[12]}')
