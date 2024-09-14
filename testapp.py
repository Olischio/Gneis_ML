import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://www.google.com/maps/place/Gneis+Lilleaker/@59.9174608,10.6292653,17z/data=!3m1!4b1!4m6!3m5!1s0x46416d7ede736dad:0x20756fbfde86d2a!8m2!3d59.9174608!4d10.6318402!16s%2Fg%2F11y1ftg85x?entry=ttu&g_ep=EgoyMDI0MDkwMi4wIKXMDSoASAFQAw%3D%3D'
response = requests.get(url, headers=headers)

with open('response.html', 'w', encoding='utf-8') as file:
    file.write(response.text)

print("HTML file saved as 'response.html'")
    
# print(response.text)  # This will print the raw HTML content of the page

# Check the response status code
print(f'Status Code: {response.status_code}')

# Print a portion of the response content
print(response.text[:500])  # Print the first 1000 characters of the response

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all div elements with the aria-label attribute containing "hektisk"
hektisk_divs = soup.find_all('div', {'aria-label': lambda x: x and 'hektisk' in x})

# Extract and print the values
for div in hektisk_divs:
    print(div['aria-label'])
