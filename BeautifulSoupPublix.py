import requests
from bs4 import BeautifulSoup

# Assign url to variable
page_url = 'https://www.publix.com/pd/publix-chicken-tender-sub/BMO-DSB-100011'
# Request publix page
page = requests.get(page_url)

# Create an object
soup = BeautifulSoup(page.text, 'html.parser')

# Check for presence of the 'on-sale' class
if soup.find(class_='on-sale'):
    print("Tag Found")
else:
    print('No sale found')
