
Google har ingen måte å hente location history data på, men dette finnes
https://besttime.app/api/v1/query/details?venue_id=ven_4977425774665f6f336d4b5259555174356e337a3157724a496843&api_key_public=pub_e33c6ae3952440588934b5c6f4fc793e

Problemet er at det koster penger
Dette burde ikke koste penger, men ser jææævelig komplisert ut
https://github.com/m-wrzr/populartimes?tab=readme-ov-file

Så jeg tror beste metoden vil være computer vision data entry inn i excel fil for å få historisk data

på denne måten vil jeg ettersom dagene går få den historiske dataen jeg trenger imens jeg kan jobbe videre på prosjektet

Her er tankene til GPT på den fremgangsmåten:

Got it! Using pyautogui for navigation and pytesseract for OCR (Optical Character Recognition) is a great approach. Here’s a step-by-step guide to achieve this:

Steps to Extract “Popular Times” Data Using pyautogui and pytesseract
Set Up Environment:
Install necessary libraries: pyautogui, opencv-python, pytesseract, Pillow, and openpyxl.
Automate Navigation with pyautogui:
Use pyautogui to open Google Maps, search for “Gneis Lilleaker”, and navigate to the “Popular Times” section.
Capture Screenshot:
Take a screenshot of the “Popular Times” data using pyautogui.
Extract Data Using Computer Vision:
Use opencv and pytesseract to process the screenshot and extract the text data.
Save Data to Excel File:
Append the extracted data to an Excel file using openpyxl.
Sample Python Script
Python

import pyautogui
import time
import cv2
import pytesseract
from PIL import Image
from openpyxl import Workbook, load_workbook
from datetime import datetime

# Function to automate navigation
def navigate_to_popular_times():
    # Open Google Maps
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('https://www.google.com/maps\n')
    time.sleep(5)
    
    # Search for Gneis Lilleaker
    pyautogui.typewrite('Gneis Lilleaker\n')
    time.sleep(5)
    
    # Scroll to the "Popular Times" section
    pyautogui.scroll(-500)
    time.sleep(2)

# Function to capture screenshot
def capture_screenshot():
    screenshot_path = "popular_times.png"
    pyautogui.screenshot(screenshot_path)
    return screenshot_path

# Function to extract data using OCR
def extract_data_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'  # Update this path as needed
    text = pytesseract.image_to_string(gray)
    return text

# Function to append data to Excel file
def append_to_excel(day, time, status):
    file_path = "popular_times_data.xlsx"
    try:
        workbook = load_workbook(file_path)
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Date", "Day", "Time", "Status"])
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    sheet.append([current_date, day, time, status])
    workbook.save(file_path)

# Main function
def main():
    navigate_to_popular_times()
    screenshot_path = capture_screenshot()
    extracted_text = extract_data_from_image(screenshot_path)
    
    # Extract specific data (example: "Not very busy now", "Monday", "14")
    status = "Not very busy now"  # Example, you need to parse this from extracted_text
    day = "Monday"  # Example, you need to parse this from extracted_text
    time = "14"  # Example, you need to parse this from extracted_text
    
    append_to_excel(day, time, status)
    print("Data extraction and saving complete.")

if __name__ == "__main__":
    main()
AI-generated code. Review and use carefully. More info on FAQ.
Notes:
Tesseract Path: Ensure pytesseract is correctly installed and the path to the Tesseract executable is set correctly.
Data Parsing: You will need to parse the extracted text to get the specific data like “Not very busy now”, “Monday”, and “14”. This can be done using regular expressions or string manipulation.
Error Handling: Add error handling to manage potential issues like element not found or page load timeouts.
This script provides a basic framework. You can enhance it by refining the data extraction logic and adding more robust error handling. Let me know if you need further assistance!






url = "https://www.yr.no/en/forecast/daily-table/11-6479/Norway/Oslo/Oslo/CC%20vest"
husk = "https://besttime.app/api/v1/query/details?venue_id=ven_4977425774665f6f336d4b5259555174356e337a3157724a496843&api_key_public=pub_e33c6ae3952440588934b5c6f4fc793e"
husk2 = "https://github.com/m-wrzr/populartimes?tab=readme-ov-file"
