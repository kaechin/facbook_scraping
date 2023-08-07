# The follwing solution is that solving by using pandas and without start date and end date asking to the user
# import pandas as pd
# import re
# import os

# # User input for username
# while True:
#     user_name = input('Please enter the user name for which you would like to get hashtag data: ').strip()
#     if not user_name:
#         print("Please enter a user name.")
#     elif "," in user_name or ";" in user_name or " " in user_name:
#         print("Please enter just one user name. It is not possible to enter multiple user names.")
#     elif not os.path.isfile(user_name + '.csv'):
#         print(f"No data file exists for the user name: {user_name}")
#     else:
#         break

# # Create file names from user input
# user_data_file = user_name + '.csv'
# user_hashtag_file = user_name + '_hashtag.csv'

# # Load data
# df = pd.read_csv(user_data_file)

# # Get all unique hashtags from 'content' column
# df['content'] = df['content'].astype(str)   # Convert the 'content' column to str type
# all_hashtags_at = set(re.findall(r'@(\w+)', ' '.join(df['content'])))
# all_hashtags_hash = set(re.findall(r'#(\w+)', ' '.join(df['content'])))

# # Checking if the file has no @ or #
# if not all_hashtags_at and not all_hashtags_hash:
#     print("The file does not contain any @ or #. Please use a different file.")
#     os._exit(0)

# # If the file has only one of @ or #, guide the user accordingly
# if not all_hashtags_at:
#     print("The file does not contain any @. You can only provide # as input.")
# elif not all_hashtags_hash:
#     print("The file does not contain any #. You can only provide @ as input.")

# # User input for multiple @ hashtags (comma-separated)
# if all_hashtags_at:
#     while True:
#         at_hashtag_names = input('Please enter at mark (@). Do not press the enter key without typing any hashtag: ').strip()
#         if not at_hashtag_names:
#             print("Please enter an at mark (@) hashtag.")
#             continue

#         # Convert the input string to a list of @ hashtags
#         at_hashtag_list = [hashtag.strip() for hashtag in at_hashtag_names.split(',')]

#         # Check if all input @ hashtags are in 'content'
#         if not all(hashtag in all_hashtags_at for hashtag in at_hashtag_list):
#             invalid_hashtags = [hashtag for hashtag in at_hashtag_list if hashtag not in all_hashtags_at]
#             print(f"The at mark (@) hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different at mark (@) hashtag.")
#             continue

#         break
# else:
#     at_hashtag_list = []

# # User input for multiple # hashtags (comma-separated)
# if all_hashtags_hash:
#     while True:
#         hash_hashtag_names = input('Please enter hashtag (#). Do not press the enter key without typing any hashtag: ').strip()
#         if not hash_hashtag_names:
#             print("Please enter a hashtag (#).")
#             continue

#         # Convert the input string to a list of # hashtags
#         hash_hashtag_list = [hashtag.strip() for hashtag in hash_hashtag_names.split(',')]

#         # Check if all input # hashtags are in 'content'
#         if not all(hashtag in all_hashtags_hash for hashtag in hash_hashtag_list):
#             invalid_hashtags = [hashtag for hashtag in hash_hashtag_list if hashtag not in all_hashtags_hash]
#             print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
#             continue

#         break
# else:
#     hash_hashtag_list = []

# # Function to check if any of the hashtags exists in the 'content' field
# def find_hashtags(x):
#     atmarks_in_content = []
#     hashtags_in_content = []
#     for hashtag in at_hashtag_list:
#         if re.search(f"@{hashtag}\\b", x):   
#             atmarks_in_content.append(hashtag)
#     for hashtag in hash_hashtag_list:
#         if re.search(f"#{hashtag}\\b", x):   
#             hashtags_in_content.append(hashtag)
#     return atmarks_in_content, hashtags_in_content

# # Find rows where 'content' field contains any of the hashtags
# df['atmark_name'], df['hashtag_name'] = zip(*df['content'].apply(find_hashtags))

# # Filter rows with at least one of the specified hashtags or atmarks
# df_hashtag = df[df['atmark_name'].astype(bool) | df['hashtag_name'].astype(bool)]   # changed this line to filter non-empty lists

# # Delete the file if it exists
# if os.path.exists(user_hashtag_file):
#     os.remove(user_hashtag_file)

# # Write to new CSV
# df_hashtag.to_csv(user_hashtag_file, index=False)

# # Successful message
# print(f"Hashtag data for {user_name} has been extracted and saved to {user_hashtag_file}.")

# The follwing solution is that solving by using csv library and without start date and end date asking to the user
# import re
# import os
# import csv

# # User input for username
# while True:
#     user_name = input('Please enter the user name for which you would like to get hashtag data: ').strip()
#     if not user_name:
#         print("Please enter a user name.")
#     elif "," in user_name or ";" in user_name or " " in user_name:
#         print("Please enter just one user name. It is not possible to enter multiple user names.")
#     elif not os.path.isfile(user_name + '.csv'):
#         print(f"No data file exists for the user name: {user_name}")
#     else:
#         break

# # Create file names from user input
# user_data_file = user_name + '.csv'
# user_hashtag_file = user_name + '_hashtag.csv'

# # Load data
# with open(user_data_file, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     data = list(reader)

# # Extract all unique hashtags from 'content' column
# all_content = ' '.join([row['content'] for row in data])
# all_hashtags_at = set(re.findall(r'@(\w+)', all_content))
# all_hashtags_hash = set(re.findall(r'#(\w+)', all_content))

# # Checking if the file has no @ or #
# if not all_hashtags_at and not all_hashtags_hash:
#     print("The file does not contain any @ or #. Please use a different file.")
#     os._exit(0)

# # If the file has only one of @ or #, guide the user accordingly
# if not all_hashtags_at:
#     print("The file does not contain any @. You can only provide # as input.")
# elif not all_hashtags_hash:
#     print("The file does not contain any #. You can only provide @ as input.")

# # User input for multiple @ hashtags (comma-separated)
# if all_hashtags_at:
#     while True:
#         at_hashtag_names = input('Please enter at mark (@). Do not press the enter key without typing any hashtag: ').strip()
#         if not at_hashtag_names:
#             print("Please enter an at mark (@) hashtag.")
#             continue

#         # Convert the input string to a list of @ hashtags
#         at_hashtag_list = [hashtag.strip() for hashtag in at_hashtag_names.split(',')]

#         # Check if all input @ hashtags are in 'content'
#         if not all(hashtag in all_hashtags_at for hashtag in at_hashtag_list):
#             invalid_hashtags = [hashtag for hashtag in at_hashtag_list if hashtag not in all_hashtags_at]
#             print(f"The at mark (@) hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different at mark (@) hashtag.")
#             continue

#         break
# else:
#     at_hashtag_list = []

# # User input for multiple # hashtags (comma-separated)
# if all_hashtags_hash:
#     while True:
#         hash_hashtag_names = input('Please enter hashtag (#). Do not press the enter key without typing any hashtag: ').strip()
#         if not hash_hashtag_names:
#             print("Please enter a hashtag (#).")
#             continue

#         # Convert the input string to a list of # hashtags
#         hash_hashtag_list = [hashtag.strip() for hashtag in hash_hashtag_names.split(',')]

#         # Check if all input # hashtags are in 'content'
#         if not all(hashtag in all_hashtags_hash for hashtag in hash_hashtag_list):
#             invalid_hashtags = [hashtag for hashtag in hash_hashtag_list if hashtag not in all_hashtags_hash]
#             print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
#             continue

#         break
# else:
#     hash_hashtag_list = []

# # Function to check if any of the hashtags exists in the 'content' field
# def find_hashtags(x):
#     atmarks_in_content = []
#     hashtags_in_content = []
#     for hashtag in at_hashtag_list:
#         if re.search(f"@{hashtag}\\b", x):   
#             atmarks_in_content.append(hashtag)
#     for hashtag in hash_hashtag_list:
#         if re.search(f"#{hashtag}\\b", x):   
#             hashtags_in_content.append(hashtag)
#     return atmarks_in_content, hashtags_in_content

# # Find rows where 'content' field contains any of the hashtags
# filtered_data = []

# for row in data:
#     atmarks_in_content, hashtags_in_content = find_hashtags(row['content'])
#     if atmarks_in_content or hashtags_in_content:
#         row['atmark_name'] = ','.join(atmarks_in_content)
#         row['hashtag_name'] = ','.join(hashtags_in_content)
#         filtered_data.append(row)

# # Delete the file if it exists
# if os.path.exists(user_hashtag_file):
#     os.remove(user_hashtag_file)

# # Write to new CSV
# with open(user_hashtag_file, mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=data[0].keys())
#     writer.writeheader()
#     writer.writerows(filtered_data)

# # Successful message
# print(f"Hashtag data for {user_name} has been extracted and saved to {user_hashtag_file}.")

# The following code is before organizing the code
# import re
# import os
# import csv
# import datetime as dt

# # User input for username
# while True:
#     user_name = input('Please enter the user name for which you would like to get hashtag data: ').strip()
#     if not user_name:
#         print("Please enter a user name.")
#     elif "," in user_name or ";" in user_name or " " in user_name:
#         print("Please enter just one user name. It is not possible to enter multiple user names.")
#     elif not os.path.isfile(user_name + '.csv'):
#         print(f"No data file exists for the user name: {user_name}")
#     else:
#         break

# # Create file names from user input
# user_data_file = user_name + '.csv'
# user_hashtag_file = user_name + '_hashtag.csv'

# # Load data
# with open(user_data_file, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)
#     data = list(reader)

# # Get column names from the original CSV and add new column names
# column_names = list(data[0].keys())
# column_names.extend(['atmark_name', 'hashtag_name'])

# # Convert 'posted_on' column to datetime and sort it in ascending order
# for row in data:
#     row['posted_on'] = dt.datetime.strptime(row['posted_on'].split('T')[0], "%Y-%m-%d")

# # Sort data by date
# data.sort(key=lambda x: x['posted_on'])

# # Display the min and max dates in the 'posted_on' column after conversion to datetime
# print("After conversion:")
# print(f"Earliest date: {data[0]['posted_on'].strftime('%Y-%m-%d')}")
# print(f"Latest date: {data[-1]['posted_on'].strftime('%Y-%m-%d')}")

# filtered_data = []
# while not filtered_data:
#     # Prompt the user for start and end dates
#     while True:
#         start_specific_date = input("Enter the start date in YYYY-MM-DD format: ")
#         end_specific_date = input("Enter the end date in YYYY-MM-DD format: ")

#         # If user just hits enter without typing anything
#         if not start_specific_date or not end_specific_date:
#             print("Please provide both the start date and end date.")
#         else:
#             break

#     # Convert the user inputs to datetime objects
#     start_date = dt.datetime.strptime(start_specific_date, "%Y-%m-%d")
#     end_date = dt.datetime.strptime(end_specific_date, "%Y-%m-%d")

#     # Filter the data based on the specified date range
#     filtered_data = [row for row in data if start_date <= row['posted_on'] <= end_date]

#     # Check if the filtered data is empty
#     if not filtered_data:
#         # If no data within the specified date range, suggest the user enter a date range within the available data range
#         min_date = data[0]['posted_on'].strftime('%Y-%m-%d')
#         max_date = data[-1]['posted_on'].strftime('%Y-%m-%d')
#         print(f"No data found within the specified date range.")
#         print(f"Please enter a date range between {min_date} and {max_date}.")

# # Extract all unique hashtags from 'content' column
# all_content = ' '.join([row['content'] for row in data])
# all_hashtags_at = set(re.findall(r'@(\w+)', all_content))
# all_hashtags_hash = set(re.findall(r'#(\w+)', all_content))

# # Checking if the file has no @ or #
# if not all_hashtags_at and not all_hashtags_hash:
#     print("The file does not contain any @ or #. Please use a different file.")
#     os._exit(0)

# # If the file has only one of @ or #, guide the user accordingly
# if not all_hashtags_at:
#     print("The file does not contain any @. You can only provide # as input.")
# elif not all_hashtags_hash:
#     print("The file does not contain any #. You can only provide @ as input.")

# # User input for multiple @ hashtags (comma-separated)
# if all_hashtags_at:
#     while True:
#         at_hashtag_names = input('Please enter at mark (@). Do not press the enter key without typing any hashtag: ').strip()
#         if not at_hashtag_names:
#             print("Please enter an at mark (@) hashtag.")
#             continue

#         # Convert the input string to a list of @ hashtags
#         at_hashtag_list = [hashtag.strip() for hashtag in at_hashtag_names.split(',')]

#         # Check if all input @ hashtags are in 'content'
#         if not all(hashtag in all_hashtags_at for hashtag in at_hashtag_list):
#             invalid_hashtags = [hashtag for hashtag in at_hashtag_list if hashtag not in all_hashtags_at]
#             print(f"The at mark (@) hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different at mark (@) hashtag.")
#             continue

#         break
# else:
#     at_hashtag_list = []

# # User input for multiple # hashtags (comma-separated)
# if all_hashtags_hash:
#     while True:
#         hash_hashtag_names = input('Please enter hashtag (#). Do not press the enter key without typing any hashtag: ').strip()
#         if not hash_hashtag_names:
#             print("Please enter a hashtag (#).")
#             continue

#         # Convert the input string to a list of # hashtags
#         hash_hashtag_list = [hashtag.strip() for hashtag in hash_hashtag_names.split(',')]

#         # Check if all input # hashtags are in 'content'
#         if not all(hashtag in all_hashtags_hash for hashtag in hash_hashtag_list):
#             invalid_hashtags = [hashtag for hashtag in hash_hashtag_list if hashtag not in all_hashtags_hash]
#             print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
#             continue

#         break
# else:
#     hash_hashtag_list = []

# # Function to check if any of the hashtags exists in the 'content' field
# def find_hashtags(x):
#     atmarks_in_content = []
#     hashtags_in_content = []
#     for hashtag in at_hashtag_list:
#         if re.search(f"@{hashtag}\\b", x):   
#             atmarks_in_content.append(hashtag)
#     for hashtag in hash_hashtag_list:
#         if re.search(f"#{hashtag}\\b", x):   
#             hashtags_in_content.append(hashtag)
#     return atmarks_in_content, hashtags_in_content

# # Find rows where 'content' field contains any of the hashtags
# filtered_data = []

# # Determine the complete set of fieldnames for the output CSV
# fieldnames = set(data[0].keys()) | {'atmark_name', 'hashtag_name'}

# for row in data:
#     atmarks_in_content, hashtags_in_content = find_hashtags(row['content'])
#     if atmarks_in_content or hashtags_in_content:
#         row['atmark_name'] = ', '.join(atmarks_in_content)
#         row['hashtag_name'] = ', '.join(hashtags_in_content)
#         filtered_data.append(row)

# # Write the filtered data to a new CSV file
# with open(user_hashtag_file, mode='w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=column_names)
#     writer.writeheader()
#     writer.writerows(filtered_data)

# print(f"Hashtag data for {user_name} has been extracted and saved to {user_hashtag_file}.")


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

def get_user_hashtags(all_hashtags_at, all_hashtags_hash):
    at_hashtag_list = []
    hash_hashtag_list = []

    if all_hashtags_at:
        while True:
            at_hashtag_names = input('Please enter at mark (@). Do not press the enter key without typing any hashtag: ').strip()
            if at_hashtag_names:
                at_hashtag_list = [hashtag.strip() for hashtag in at_hashtag_names.split(',')]
                if all(hashtag in all_hashtags_at for hashtag in at_hashtag_list):
                    break

    if all_hashtags_hash:
        while True:
            hash_hashtag_names = input('Please enter hashtag (#). Do not press the enter key without typing any hashtag: ').strip()
            if hash_hashtag_names:
                hash_hashtag_list = [hashtag.strip() for hashtag in hash_hashtag_names.split(',')]
                if all(hashtag in all_hashtags_hash for hashtag in hash_hashtag_list):
                    break

    return at_hashtag_list, hash_hashtag_list

def filter_data(data, at_hashtag_list, hash_hashtag_list):
    def find_hashtags(x):
        atmarks_in_content = [hashtag for hashtag in at_hashtag_list if re.search(f"@{hashtag}\\b", x)]
        hashtags_in_content = [hashtag for hashtag in hash_hashtag_list if re.search(f"#{hashtag}\\b", x)]
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

def main():
    user_name = get_user_name()
    user_data_file = user_name + '.csv'
    user_hashtag_file = user_name + '_hashtag.csv'

    with open(user_data_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    for row in data:
        row['posted_on'] = dt.datetime.strptime(row['posted_on'].split('T')[0], "%Y-%m-%d")

    data.sort(key=lambda x: x['posted_on'])

    filtered_data = get_date_range(data)

    all_hashtags_at, all_hashtags_hash = extract_unique_hashtags(data)

    at_hashtag_list, hash_hashtag_list = get_user_hashtags(all_hashtags_at, all_hashtags_hash)

    filtered_data = filter_data(filtered_data, at_hashtag_list, hash_hashtag_list)

    column_names = list(data[0].keys()) + ['atmark_name', 'hashtag_name']
    write_to_csv(user_hashtag_file, filtered_data, column_names)

    print(f"Hashtag data for {user_name} has been extracted and saved to {user_hashtag_file}.")

if __name__ == "__main__":
    main()
