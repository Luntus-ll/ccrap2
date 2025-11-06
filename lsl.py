import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.cian.ru/cat.php?currency=2&deal_type=rent&engine_version=2&offer_type=flat&region=1&room1=1&room2=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3'
}
