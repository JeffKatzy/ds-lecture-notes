import bs4
import requests

class CraigsList:

    def __init__(self):
        self.text = requests.get('https://newyork.craigslist.org/search/aap').text
        self.soup = bs4.BeautifulSoup(self.text)

    def apartment_rows(self):
        return self.soup.find_all(class_='rows')

    def apartment_row(self):
        return self.apartment_rows()[0]

    def apartment_row_info(self):
        return self.apartment_row().find(class_="result-info")

    def apartment_row_date(self):
        from datetime import datetime
        time = datetime.strptime(time, '%Y-%m-%d %H:%M')
        
        return self.apartment_row_info().find(class_="result-date")

    def apartment_row_title(self):
        return self.apartment_row_info().find(class_="result-title").text

    def apartment_row_price(self):
        return self.apartment_row_info().find(class_="result-price").text

    def apartment_row_hood(self):
        return self.apartment_row_info().find(class_="result-hood").text
