import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&offer_type=flat&region=1&room1=1&room2=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
}
response = requests.get(url, headers=headers)
print("Статус запроса:", response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []
    
    items = soup.find_all('article', {'data-name': 'CardComponent'})
    
    for item in items[:10]:
        try:
            title_elem = item.find('span', {'data-mark': 'OfferTitle'})
            title = title_elem.text.strip() if title_elem else "Квартира"
            
            address_elem = item.find('a', {'data-name': 'GeoLabel'})
            address = address_elem.text.strip() if address_elem else "Адрес не указан"
            
            price_elem = item.find('span', {'data-mark': 'MainPrice'})
            price = price_elem.text.strip() if price_elem else "0"
            
            area_elem = item.find('span', string=lambda text: text and 'м²' in text)
            area = area_elem.text.strip() if area_elem else "0 м²"
            data.append({
                'Тип': title,
                'Адрес': address,
                'Цена': price,
                'Площадь': area
            })
        except Exception:
            continue
    df = pd.DataFrame(data)
    if not df.empty:
        print(df)
    else:
        print("Не удалось найти") 
else:
    print(f"Ошибка доступа: {response.status_code}")
