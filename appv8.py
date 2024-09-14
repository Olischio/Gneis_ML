import pyautogui
import time
import pyperclip
import json
from bs4 import BeautifulSoup
from datetime import datetime

def copy_body():
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    bodyhtml = pyperclip.paste()
    if '<body' in bodyhtml:
        return bodyhtml
    else:
        raise ValueError("Copied content does not contain a body tag")

Browser = 'Microsoft Edge'
pyperclip.copy(Browser)

# Open Windows Search and type "Microsoft Edge"
pyautogui.hotkey('win', 's')
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Wait for the browser to open
time.sleep(2)

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
pyautogui.scroll(-700)

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

time.sleep(10)
pyautogui.hotkey('ctrl', 'w')

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(htmlbody, 'html.parser')

# Find the div with the specific aria-label
current_popularity_element = soup.find('div', {'aria-label': lambda x: x and 'For øyeblikket' in x})

# Store the data in a list of dictionaries
data = []

# Get the current date
current_date = datetime.now().strftime("%d.%m.%Y")

# Go up one layer in the tree structure
if current_popularity_element:
    parent_div = current_popularity_element.find_parent('div')
    
    # Extract all div values from the parent div
    if parent_div:
        child_divs = parent_div.find_all('div', {'aria-label': True})
        for div in child_divs:
            aria_label = div['aria-label']
            parts = aria_label.split(' ')
            if len(parts) >= 5:
                popularity = parts[0]  # Extract the popularity percentage
                time_label = parts[-1].strip('.')  # Extract the time and remove the trailing period
                data.append({
                    "date": current_date,
                    "time": time_label,
                    "popularity": popularity
                })

# Save the data to a JSON file
with open('popularity_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data saved to popularity_data.json")