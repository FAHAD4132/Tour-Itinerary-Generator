from bs4 import BeautifulSoup
import requests

def scrape_tour_data(url):
    page_content = requests.get(url)
    soup = BeautifulSoup(page_content.text, 'html.parser')

    # Extract Tour Name
    tour_name = soup.find('h1').text.strip() if soup.find('h1') else "Not found"

    # Extract basic info
    info_items = soup.find_all(class_='g-tour-feature')[0].find_all(class_='item')
    duration = info_items[0].find(class_='value').text.strip() if len(info_items) > 0 else "Not found"
    tour_type = info_items[1].find(class_='value').text.strip() if len(info_items) > 1 else "Not found"
    trip_category = info_items[2].find(class_='value').text.strip() if len(info_items) > 2 else "Not found"
    location = info_items[3].find(class_='value').text.strip() if len(info_items) > 3 else "Not found"

    # Extract Included/Excluded items
    included = [item.text.strip() for item in soup.find_all(class_='col-lg-6 col-md-6')[0].find_all(class_='item')]
    excluded = [item.text.strip() for item in soup.find_all(class_='col-lg-6 col-md-6')[1].find_all(class_='item')]

    # Extract Tour Price
    price = "Not found"
    price_element = soup.find(class_='text-lg')
    if price_element:
        price = price_element.text.strip()

    return {
        "tour_name": tour_name,
        "duration": duration,
        "tour_type": tour_type,
        "trip_category": trip_category,
        "location": location,
        "included": included,
        "excluded": excluded,
        "price": price
    }