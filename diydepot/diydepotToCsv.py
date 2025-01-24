import csv
from bs4 import BeautifulSoup

# Example HTML data (this would usually come from a file or request)
html_data = '''[Paste your HTML content here]'''

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

# Open a CSV file for writing
with open('diydepottocsv.csv', 'w', newline='') as csvfile:
    fieldnames = ['Store Name', 'Contact Number', 'Email', 'Address', 'Trading Hours', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Extract store details
    stores = soup.find_all('div', class_='single-location')
    
    for store in stores:
        store_name = store.find('h4').text.strip()
        store_url = store.find('a', href=True)['href']
        
        # Extract contact details
        contact_number = store.find('a', href=True, text=True)
        if contact_number and 'tel:' in contact_number['href']:
            contact_number = contact_number.text.strip()
        else:
            contact_number = ''
        
        email = store.find('a', href=True, title=True)
        if email and 'mailto:' in email['href']:
            email = email.text.strip()
        else:
            email = ''
        
        # Extract address
        address_elements = store.find_all('p')
        address = ' '.join([element.text.strip() for element in address_elements if element.text.strip()])
        
        # Extract trading hours
        trading_hours = store.find('div', class_='trading-hours')
        trading_hours_text = trading_hours.get_text(strip=True) if trading_hours else ''
        
        # Write to CSV
        writer.writerow({
            'Store Name': store_name,
            'Contact Number': contact_number,
            'Email': email,
            'Address': address,
            'Trading Hours': trading_hours_text,
            'URL': store_url
        })

print('Data written to store_locations.csv')
