# Reference: https://proxyway.com/guides/how-to-scrape-facebook
# Reference: https://github.com/shaikhsajid1111/facebook_page_scraper/tree/master/facebook_page_scraper

from facebook_page_scraper import scraper
from datetime import datetime
import os

# Make sure to create this folder
directory = "/Users/81701/Downloads/Facebook_Scraping"

# Function to delete the CSV file if it exists
def delete_existing_file(directory, filename):
    file_path = os.path.join(directory, filename + ".csv")
    if os.path.exists(file_path):
        os.remove(file_path)

start_date = datetime(2022, 11, 29)
end_date = datetime(2023, 7, 20)
# start_date = None
# end_date = None

page_list = ['tsudaoffcampus']
posts_count = 10000
browser = "firefox"
timeout = 600 #600 seconds
headless = False

# Check if "page_list.csv" exists and delete it before scraping again
delete_existing_file(directory, "page_list")

for page in page_list:
    # Delete existing CSV file if it exists
    delete_existing_file(directory, page)

    # Our proxy for this scrape
    proxy = f'webscraping-rotate:webscraping1234@p.webshare.io:80'
    #proxy = f'webscraping:webscraping1234@154.21.155.40:6483'

    # Initializing a scraper
    scraper_instance = scraper.Facebook_scraper(page, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

    # Scraping and writing into the output CSV file
    filename = page
    scraper_instance.scrap_to_csv(filename, directory, start_date=start_date, end_date=end_date)

