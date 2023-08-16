# Reference: https://proxyway.com/guides/how-to-scrape-facebook
# Reference: https://github.com/shaikhsajid1111/facebook_page_scraper/tree/master/facebook_page_scraper

from facebook_page_scraper_1 import scraper
from datetime import datetime
from datetime import date
import os
import requests

# Make sure to create this folder
directory = os.getcwd()
if not os.path.exists(directory):
    os.makedirs(directory)


# Function to delete the CSV file if it exists
def delete_existing_file(directory, filename):
    file_path = os.path.join(directory, filename + ".csv")
    if os.path.exists(file_path):
        os.remove(file_path)

# Function to get a valid date input from the user
def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")


# Function to get the valid page list from the user
def get_valid_page_list():
    while True:
        page_list = input("Enter the page list which you want to scrape (You can scrape just one page list name): ").split(',')
        # Check if the user has entered any page name
        if not page_list:
            print("Please enter the name of the page you want to scrape.")
        elif len(page_list) > 1:
            print("Please enter only one page name at a time for scraping.")
        else:
            return page_list[0]
        
def scrape(page_name, start_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    print("For the end date, it will scrape today's date.")
    end_date = datetime.now()

    posts_count = 10000

    browser = "firefox"
    timeout = 600 #600 seconds
    headless = False

    # Check if "page_list.csv" exists and delete it before scraping again
    delete_existing_file(directory, "page_list")

    # Delete existing CSV file if it exists
    delete_existing_file(directory, page_name)

    # Connectiong to the proxy
    proxy = requests.get(
        "https://ipv4.webshare.io/",
        proxies={
            "http": "http://PROXY USERNAME:PROXYPASS WORD@p.webshare.io:80/",
            "https": "http://PROXY USERNAME:PROXYPASS WORD@p.webshare.io:80/"
        }
    ).text

    # Initializing a scraper
    scraper_instance = scraper.Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

    # Scraping and writing into the output CSV file
    filename = page_name
    scraper_instance.scrap_to_csv(filename, directory, start_date=start_date, end_date=end_date)

if __name__ == '__main__':  
    scrape()