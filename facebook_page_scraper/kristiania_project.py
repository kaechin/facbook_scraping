# Reference: https://proxyway.com/guides/how-to-scrape-facebook

from facebook_page_scraper import scraper
from datetime import datetime

# Need to delete the csv file, if you scrape same name's file
# import os

# os.remove("test.tsx")

start_date = datetime(2023, 6, 1)
end_date = datetime(2023, 7, 20)
# start_date = None
# end_date = None

page_list = ['arnold']

#proxy_port = 5578

posts_count = 10000
browser = "firefox"

timeout = 600 #600 seconds
headless = False

# Dir for output if we scrape directly to CSV
# Make sure to create this folder
directory = "/Users/81701/Downloads/Facebook_Scraping"

for page in page_list:
    #our proxy for this scrape
    #proxy = f'webscraping:webscraping1234@proxy_server:{proxy_port}'
    proxy = f'webscraping-rotate:webscraping1234@p.webshare.io:80'
    #proxy = f'webscraping:webscraping1234@154.21.155.40:6483'
    #initializing a scraper
    scraper_instance = scraper.Facebook_scraper(page, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)
    
    # Scraping and writing into output CSV file:
    filename = page
    scraper_instance.scrap_to_csv(filename, directory, start_date=start_date, end_date=end_date)

    # # Rotating our proxy to the next port so we could get a new IP and avoid blocks
    # proxy_port += 1
