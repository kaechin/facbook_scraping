import re
import os
import csv
import datetime as dt

def get_user_name():
    while True:
        user_name = input('Please enter the user name for which you would like to get hashtag data: ').strip()
        if not user_name:
            print("Please enter a user name.")
        elif "," in user_name or ";" in user_name or " " in user_name:
            print("Please enter just one user name. It is not possible to enter multiple user names.")
        elif not os.path.isfile(user_name + '.csv'):
            print(f"No data file exists for the user name: {user_name}")
        else:
            return user_name

def get_date_range(data):
    while True:
        start_specific_date = input("Enter the start date in YYYY-MM-DD format: ")
        end_specific_date = input("Enter the end date in YYYY-MM-DD format: ")

        if not start_specific_date or not end_specific_date:
            print("Please provide both the start date and end date.")
        else:
            start_date = dt.datetime.strptime(start_specific_date, "%Y-%m-%d")
            end_date = dt.datetime.strptime(end_specific_date, "%Y-%m-%d")
            filtered_data = [row for row in data if start_date <= row['posted_on'] <= end_date]
            
            if not filtered_data:
                min_date = data[0]['posted_on'].strftime('%Y-%m-%d')
                max_date = data[-1]['posted_on'].strftime('%Y-%m-%d')
                print(f"No data found within the specified date range.")
                print(f"Please enter a date range between {min_date} and {max_date}.")
            else:
                return filtered_data

def extract_unique_hashtags(data):
    all_content = ' '.join([row['content'] for row in data])
    return set(re.findall(r'@(\w+)', all_content)), set(re.findall(r'#(\w+)', all_content))


def get_user_hashtags(all_atmarks, all_hashtags_hash, atmark=None, hash_hashtags=None):
    atmark_list = []
    hash_hashtag_list = []
    error_messages = []  # List to keep track of error messages

    # Only work with @ tags if they were provided
    if atmark:
        if atmark == "@":
            atmark_list = list(all_atmarks)
        else:
            at_hashtag_names = atmark
            atmark_list = [hashtag.strip() for hashtag in at_hashtag_names.split(',')]
            
            # Check if any @ tags are not in all_atmarks
            for hashtag in atmark_list:
                if hashtag not in all_atmarks:
                    error_messages.append(f"@{hashtag} does not exist in the data.")

    # Only work with # tags if they were provided
    if hash_hashtags:
        if hash_hashtags == "#":
            hash_hashtag_list = list(all_hashtags_hash)
        else:
            hash_hashtag_names = hash_hashtags
            hash_hashtag_list = [hashtag.strip() for hashtag in hash_hashtag_names.split(',')]

            # Check if any # tags are not in all_hashtags_hash
            for hashtag in hash_hashtag_list:
                if hashtag not in all_hashtags_hash:
                    error_messages.append(f"#{hashtag} does not exist in the data.")

    return atmark_list, hash_hashtag_list, error_messages

def filter_data(data, atmark_list, hash_hashtag_list):
    print(atmark_list, hash_hashtag_list)
    def find_hashtags(x):
        atmarks_in_content = [hashtag for hashtag in atmark_list if re.search(f"\@{hashtag}\\b", x)]
        hashtags_in_content = [hashtag for hashtag in hash_hashtag_list if re.search(f"\#{hashtag}\\b", x)]

        return atmarks_in_content, hashtags_in_content

    filtered_data = []
    for row in data:
        atmarks_in_content, hashtags_in_content = find_hashtags(row['content'])
        if atmarks_in_content or hashtags_in_content:
            row['atmark_name'] = ', '.join(atmarks_in_content)
            row['hashtag_name'] = ', '.join(hashtags_in_content)
            filtered_data.append(row)
    
    return filtered_data


def filter_data(data, atmark_list, hash_hashtag_list):
    def find_hashtags(x):
        atmarks_in_content = [hashtag for hashtag in atmark_list if re.search(f"\@{hashtag}\\b", x)]
        hashtags_in_content = [hashtag for hashtag in hash_hashtag_list if re.search(f"\#{hashtag}\\b", x)]

        return atmarks_in_content, hashtags_in_content

    filtered_data = []
    for row in data:
        atmarks_in_content, hashtags_in_content = find_hashtags(row['content'])
        if atmarks_in_content or hashtags_in_content:
            row['atmark_name'] = ', '.join(atmarks_in_content)
            row['hashtag_name'] = ', '.join(hashtags_in_content)
            filtered_data.append(row)
    return filtered_data


def write_to_csv(user_hashtag_file, data, column_names):
    with open(user_hashtag_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=column_names)
        writer.writeheader()
        writer.writerows(data)

def hashtag(username, start_date, end_date, atmark=None, hash_hashtags=None):
    error_messages = []

    user_data_file = f"{username}.csv"

    # Check if username file exists
    if not os.path.exists(user_data_file):
        return {"status": "error", "message": f"{username} does not exist, please scrape first"}

    # Open the file and extract unique "@" and "#" hashtags
    with open(user_data_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        all_atmarks, all_hashtags_hash = extract_unique_hashtags(data)

    atmark_list, hash_hashtag_list, error_messages = get_user_hashtags(all_atmarks, all_hashtags_hash, atmark, hash_hashtags)


    # Rest of the function:
    for row in data:
        row['posted_on'] = dt.datetime.strptime(row['posted_on'].split('T')[0], "%Y-%m-%d")

    data.sort(key=lambda x: x['posted_on'])

    start_date_obj = dt.datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = dt.datetime.strptime(end_date, "%Y-%m-%d")

    filtered_data = [row for row in data if start_date_obj <= row['posted_on'] <= end_date_obj]

    atmark = atmark.split(",")
    hash_hashtags = hash_hashtags.split(",")
    
    if atmark == ['']:
        atmark = []
    
    if hash_hashtags == ['']:
        hash_hashtags = []

    if  atmark or hash_hashtags:

        filtered_data = filter_data(filtered_data, atmark, hash_hashtags)

    user_hashtag_file = f"{username}_hashtag.csv"
    column_names = list(data[0].keys()) + ['atmark_name', 'hashtag_name']
        
    write_to_csv(user_hashtag_file, filtered_data, column_names)

    if error_messages:
        return {"status": "error", "message": " | ".join(error_messages)}


    return {"message": f"Hashtag data for {username} has been extracted and saved to {user_hashtag_file}."}

if __name__ == "__main__":
    hashtag()