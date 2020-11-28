import os
from PIL import Image, ImageChops
from selenium import webdriver

path = os.getcwd()
root_path = os.path.abspath(os.path.join(path, os.pardir))

base_image = open(root_path + "/resources/ui/screencaptures/default_webpage.png", "rb").read()

# define the browser path
ui = webdriver.Chrome(executable_path=root_path + "/drivers/chromedriver.exe")

# to maximise the window
ui.maximize_window()


# Scenario 1 : To verify the UI alignment with Mode=Random
print("Scenario 1 : checking Screen Alignment with random mode ")
# navigating to the webpage
ui.get("https://the-internet.herokuapp.com/shifting_content/menu?mode=random")

# capture the screen
ui.save_screenshot(root_path + "/resources/ui/screencaptures/mode_random.png")

if(open(
        root_path + "/resources/ui/screencaptures/mode_random.png",
        "rb").read() == base_image):
    print("screen alignment matched")
else:
    print("screen alignment mismatch")


# *******************************************************************************************************

# Scenario 2: To verify the UI alignment with pixel_shift=100

print("Scenario 2 :checking Screen Alignment with pixel shifting")
# navigating to the webpage
ui.get("https://the-internet.herokuapp.com/shifting_content/menu?pixel_shift=100")

# capture the screen
ui.save_screenshot(root_path + "/resources/ui/screencaptures/pixel_shift_100.png")

if (open(
        root_path + "/resources/ui/screencaptures/pixel_shift_100.png",
        "rb").read() == base_image):
    print("screen alignment matched")
else:
    print("screen alignment mismatch")


# *******************************************************************************************************

# Scenario 3: To verify the UI alignment with mode=random&pixel_shift=100
print("Scenario 3 :checking Screen Alignment with random mode and pixel shifting")
# navigating to the webpage
ui.get("https://the-internet.herokuapp.com/shifting_content/menu?mode=random&pixel_shift=100")

# capture the screen
ui.save_screenshot(root_path + "/resources/ui/screencaptures/random_pixel_shift_100.png")

if (open(
        root_path + "/resources/ui/screencaptures/random_pixel_shift_100.png",
        "rb").read() == base_image):
    print("screen alignment matched")
else:
    print("screen alignment mismatch")

ui.close()
