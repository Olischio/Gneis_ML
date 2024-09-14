import pyautogui
import time
import pyperclip
import json
from bs4 import BeautifulSoup



# def copyDivToDict(div_count: int):
#     div_dict = {}
    
#     for i in range(div_count):
#         pyautogui.click()
#         time.sleep(0.1)
#         pyautogui.hotkey('ctrl', 'c')
#         time.sleep(0.1)
#         div_dict[i] = pyperclip.paste()
#         time.sleep(0.1)
#         pyautogui.moveRel(0, 15)
#         time.sleep(0.1)

#     return div_dict

def copy_body():

    pyautogui.click()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    bodyhtml = pyperclip.paste()

    return bodyhtml



Browser = 'Microsoft Edge'
pyperclip.copy(Browser)

# Open Windows Search and type "Microsoft Edge"
pyautogui.hotkey('win', 's')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Wait for the browser to open
time.sleep(1)

# Spotlight the URL bar
pyautogui.hotkey('ctrl', 'l')

url = "https://www.google.no/maps/place/Gneis+Lilleaker/@59.9554869,10.6472646,4606m/data=!3m1!1e3!4m6!3m5!1s0x46416d7ede736dad:0x20756fbfde86d2a!8m2!3d59.9174608!4d10.6318402!16s%2Fg%2F11y1ftg85x?entry=ttu&g_ep=EgoyMDI0MDkwMy4wIKXMDSoASAFQAw%3D%3D"
pyperclip.copy(url)
# Paste the URL from the clipboard
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Wait for the page to load
time.sleep(8)

# Scroll the scroll wheel 6 times on the leftmost side of the screen
screen_width, screen_height = pyautogui.size()
pyautogui.moveTo(200, screen_height // 2)
# pyautogui.scroll(-700)

# Open developer tools
pyautogui.hotkey('ctrl', 'shift', 'i')

# Activate the element picker
pyautogui.hotkey('ctrl', 'shift', 'c')
time.sleep(1)
pyautogui.moveTo(60, screen_height // 2)
pyautogui.moveRel(0, 25)
pyautogui.click()
              
time.sleep(2)
pyautogui.moveRel(920, 0)

pyautogui.scroll(2500)
pyautogui.moveTo(y=174)
htmlbody = copy_body()
#div_values_dict = copyDivToDict(18)
# print(htmlbody)

time.sleep(10)
pyautogui.hotkey('ctrl', 'w')


# Find the element containing "For øyeblikket"
# from bs4 import BeautifulSoup

# htmlbody = "your_html_content_here"
# soup = BeautifulSoup(htmlbody, 'html.parser')

# # Find the div with the specific aria-label
# current_popularity_element = soup.find('div', {'aria-label': lambda x: x and 'For øyeblikket' in x})

# # Extract the aria-label value
# if current_popularity_element:
#     current_time_popularity_value = current_popularity_element['aria-label']
#     print(current_time_popularity_value)
# else:
#     print("Element not found")


soup = BeautifulSoup(htmlbody, 'html.parser')
divs_with_aria_label = soup.find_all('div', {'aria-label': True})

for div in divs_with_aria_label:
    print(div['aria-label'])


