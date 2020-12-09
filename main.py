from os import name, system
from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class page:
  info = None

print('Starting Rep+')

def check_exists_by_xpath(xpath):
  try:
    browser.find_element_by_xpath(xpath)
  except NoSuchElementException:
    return False
  return True

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--loglevel=3')

browser = webdriver.Chrome(options=options)

system('cls')
custom_fig = Figlet(font='univers')
print(custom_fig.renderText('Rep+'))

purl = input('\nSearch SteamRep: ')
print(f'\nSearching... This may take a while...\n')

def load_page():
  browser.get('https://steamrep.com/search?q=' + purl)
  WebDriverWait(browser, 20).until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="profileloading"]')))
  page.info = [
    browser.find_elements_by_xpath('//*[@id="steamids"]')[0].text.split("| "),
    browser.find_elements_by_xpath('//*[@id="membersince"]')[0].text,
    browser.find_element_by_xpath('//*[@id="steamlevel"]').text,
    browser.find_element_by_xpath('//*[@id="privacystate"]').text,
    browser.find_element_by_xpath('//*[@id="repshield"]/img').get_attribute("alt"),
    browser.find_element_by_xpath('//*[@id="tradebanstatus"]').text,
    browser.find_element_by_xpath('//*[@id="vacbanned"]').text,
    browser.find_element_by_xpath('//*[@id="communitybanstatus"]').text]
  
  if any(x == '--' for x in page.info):
    load_info()

load_page()
print('Results: \n')

print(f'Steam Name: {page.info[0][1][11:]}', end='')
print(f'Joined Steam: {page.info[1]}')
print(f'Steam Level: {page.info[2]}')
print(f'Profile Privacy: {page.info[3]}')
print(f'Reputation Status: {page.info[4]}')
print(f'Trade Ban: {page.info[5]}')
print(f'VAC Ban: {page.info[6]}')
print(f'Community Ban: {page.info[7]}')

browser.quit()