# Library imports
from bs4 import BeautifulSoup
import requests
import lxml
import html5lib



tracked_url = "https://www.amazon.co.uk/COSORI-Electric-Temperature-Reminder-Function/dp/B07N8QY3YH?ref=dlx_deals_gd_dcl_tlt_14_36be5466_dt_sl16_8a"
amazon_headers ={
        "Accept-Language":"en-GB,en;q=0.9",
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"
}
tracked_url_markup = requests.get(url=tracked_url, headers=amazon_headers)
tracked_url_markup.raise_for_status()
tracked_url_markup = tracked_url_markup.text
url_soup = BeautifulSoup(tracked_url_markup, "lxml")
tracked_price = url_soup.find(class_="a-offscreen").text
current_price = float(tracked_price.split("£")[1]) # should be number 92.48
# tracked_price_2 = url_soup.find(class_="a-offscreen")

print(current_price)
# id tp_price_block_total_price_ww


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
