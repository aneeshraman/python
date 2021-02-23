import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.minimize_window()

# TODO: Enter a url
driver.get(
    "https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZWEzODY5ZDEtOTA3Zi00YmZlLTlmYTQtYjRkMDA0YzIxZWQ3%40thread"
    ".v2/0?context=%7b%22Tid%22%3a%225fd10a7a-9625-46f7-b7f9-551a2760c887%22%2c%22Oid%22%3a%220c8f5f65-1a12-43cd-9b92"
    "-d805a692fcfc%22%7d "
)
driver.maximize_window()
pyautogui.hotkey("esc")
driver.minimize_window()
driver.find_element(By.CSS_SELECTOR, "#buttonsbox > button:nth-child(2)").click()
driver.maximize_window()
pyautogui.sleep(5)
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")
driver.minimize_window()
