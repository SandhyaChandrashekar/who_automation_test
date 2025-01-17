import time
import os
from selenium import webdriver
path = os.getcwd()
root_path = os.path.abspath(os.path.join(path, os.pardir))

# define the browser path
webpage = webdriver.Chrome(executable_path=root_path + "/drivers/chromedriver.exe")

# to maximise the window
webpage.maximize_window()

# navigating to the webpage
webpage.get("https://the-internet.herokuapp.com/add_remove_elements/")

#capture the screen
webpage.save_screenshot(root_path + "/resources/ui/screencaptures/add_element.png")

# verify Add Element and Delete buttons
webpage.find_element_by_xpath("//button[contains(text(),'Add Element')]").click()
time.sleep(2)

# capture the screen
webpage.save_screenshot(root_path +"/resources/ui/screencaptures/delete_button.png")

# check Delete button is added
webpage.find_element_by_xpath("//button[contains(text(),'Add Element')]").click()
time.sleep(2)

# check Delete button is removed
webpage.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
time.sleep(1)
webpage.find_element_by_xpath("//button[contains(text(),'Delete')]").click()

# close the webpage
webpage.close()