# Reference: https://proxyway.com/guides/how-to-scrape-facebook
# Reference: https://github.com/shaikhsajid1111/facebook_page_scraper/tree/master/facebook_page_scraper

from facebook_page_scraper import scraper
from datetime import datetime
import os
import requests

# Make sure to create this folder
directory = "/Users/81701/Downloads/Facebook_Scraping/facebook_page_scraper"

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

# Get the start date and end date from the user
print("Enter the start date (YYYY-MM-DD):")
start_date = get_valid_date("Start Date: ")

print("For the end date, it will scrape today's date.")
end_date = datetime.now()

#page_list = ['arnold']
posts_count = 1000

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

# Get the page list from the user and split it into a list of pages
page_name = get_valid_page_list()
#posts_count = int(input("Enter the number of posts you want to scrape: "))

browser = "firefox"
timeout = 600 #600 seconds
headless = False

# Check if "page_list.csv" exists and delete it before scraping again
delete_existing_file(directory, "page_list")

# Delete existing CSV file if it exists
delete_existing_file(directory, page_name)

# Our proxy for this scrape
#proxy = f'webscraping-rotate:webscraping1234@p.webshare.io:80'
#proxy = f'webscraping:webscraping1234@154.21.155.40:6483'
proxy = requests.get(
    "https://ipv4.webshare.io/",
    proxies={
        "http": "http://webscraping-rotate:webscraping1234@p.webshare.io:80/",
        "https": "http://webscraping-rotate:webscraping1234@p.webshare.io:80/"
    }
).text

# Initializing a scraper
scraper_instance = scraper.Facebook_scraper(page_name, posts_count, browser, proxy=proxy, timeout=timeout, headless=headless)

# Scraping and writing into the output CSV file
filename = page_name
scraper_instance.scrap_to_csv(filename, directory, start_date=start_date, end_date=end_date)