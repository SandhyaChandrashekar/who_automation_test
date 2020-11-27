import time

from selenium import webdriver

# define the browser path
webpage = webdriver.Chrome(executable_path="C:\\Users\Sandhyarani.BS\drivers\chromedriver.exe")

# to maximise the window
webpage.maximize_window()

# navigating to the webpage
webpage.get("https://the-internet.herokuapp.com/add_remove_elements/")

#capture the screen
webpage.save_screenshot("C:/Users/Sandhyarani.BS/PycharmProjects/PythonTesting/WHO_Automation_Test/resources/ui/screencaptures/add_element.png")

# verify Add Element and Delete buttons
webpage.find_element_by_xpath("//button[contains(text(),'Add Element')]").click()
time.sleep(2)

# capture the screen
webpage.save_screenshot("C:/Users/Sandhyarani.BS/PycharmProjects/PythonTesting/WHO_Automation_Test/resources/ui/screencaptures/delete_button.png")

# check Delete button is added
webpage.find_element_by_xpath("//button[contains(text(),'Add Element')]").click()
time.sleep(2)

# check Delete button is removed
webpage.find_element_by_xpath("//button[contains(text(),'Delete')]").click()
time.sleep(1)
webpage.find_element_by_xpath("//button[contains(text(),'Delete')]").click()

# close the webpage
webpage.close()