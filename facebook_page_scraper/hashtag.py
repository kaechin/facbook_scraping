# import pandas as pd
# import re
# import os

# # Load data
# df = pd.read_csv('arnold.csv')

# # Get all unique hashtags from 'content' column
# all_hashtags = set(re.findall(r'@(\w+)', ' '.join(df['content'])))

# while True:
#     # User input for multiple hashtags (comma-separated)
#     hashtag_names = input('Write comma-separated hashtag keywords that you want to retrieve: ').strip()

#     if hashtag_names == "":
#         print("Please enter a hashtag. Do not press the enter key without typing any hashtag.")
#         continue

#     # Convert the input string to a list of hashtags
#     hashtag_list = [hashtag.strip() for hashtag in hashtag_names.split(',')]

#     # Check if all input hashtags are in 'content'
#     if not all(hashtag in all_hashtags for hashtag in hashtag_list):
#         invalid_hashtags = [hashtag for hashtag in hashtag_list if hashtag not in all_hashtags]
#         print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
#         continue

#     break

# # Function to check if any of the hashtags exists in the 'content' field
# def find_hashtags(x):
#     hashtags_in_content = []
#     for hashtag in hashtag_list:
#         if re.search(f"@{hashtag}", x):   
#             hashtags_in_content.append(hashtag)
#     return ', '.join(hashtags_in_content) if hashtags_in_content else ""

# # Find rows where 'content' field contains any of the hashtags
# df['hashtag_name'] = df['content'].apply(find_hashtags)

# # Filter rows with at least one of the specified hashtags
# df_hashtag = df[df['hashtag_name'].astype(bool)]   # changed this line to filter non-empty lists

# # Delete the file if it exists
# if os.path.exists('arnold_hashtag.csv'):
#     os.remove('arnold_hashtag.csv')

# # Write to new CSV
# df_hashtag.to_csv('arnold_hashtag.csv', index=False)

# import pandas as pd
# import re
# import os

# # User input for username
# user_name = input('Please enter user name which you would like to get hashtag data: ').strip()

# # Create file names from user input
# user_data_file = user_name + '.csv'
# user_hashtag_file = user_name + '_hashtag.csv'

# # Load data
# df = pd.read_csv(user_data_file)

# # Get all unique hashtags from 'content' column
# all_hashtags = set(re.findall(r'@(\w+)', ' '.join(df['content'])))

# while True:
#     # User input for multiple hashtags (comma-separated)
#     hashtag_names = input('Write comma-separated hashtag keywords that you want to retrieve: ').strip()

#     if hashtag_names == "":
#         print("Please enter a hashtag. Do not press the enter key without typing any hashtag.")
#         continue

#     # Convert the input string to a list of hashtags
#     hashtag_list = [hashtag.strip() for hashtag in hashtag_names.split(',')]

#     # Check if all input hashtags are in 'content'
#     if not all(hashtag in all_hashtags for hashtag in hashtag_list):
#         invalid_hashtags = [hashtag for hashtag in hashtag_list if hashtag not in all_hashtags]
#         print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
#         continue

#     break

# # Function to check if any of the hashtags exists in the 'content' field
# def find_hashtags(x):
#     hashtags_in_content = []
#     for hashtag in hashtag_list:
#         if re.search(f"@{hashtag}", x):   
#             hashtags_in_content.append(hashtag)
#     return ', '.join(hashtags_in_content) if hashtags_in_content else ""

# # Find rows where 'content' field contains any of the hashtags
# df['hashtag_name'] = df['content'].apply(find_hashtags)

# # Filter rows with at least one of the specified hashtags
# df_hashtag = df[df['hashtag_name'].astype(bool)]   # changed this line to filter non-empty lists

# # Delete the file if it exists
# if os.path.exists(user_hashtag_file):
#     os.remove(user_hashtag_file)

# # Write to new CSV
# df_hashtag.to_csv(user_hashtag_file, index=False)

import pandas as pd
import re
import os

# User input for username
while True:
    user_name = input('Please enter the user name for which you would like to get hashtag data: ').strip()
    if not user_name:
        print("Please enter a user name.")
    elif "," in user_name or ";" in user_name or " " in user_name:
        print("Please enter just one user name. It is not possible to enter multiple user names.")
    elif not os.path.isfile(user_name + '.csv'):
        print(f"No data file exists for the user name: {user_name}")
    else:
        break

# Create file names from user input
user_data_file = user_name + '_specific_date.csv'
user_hashtag_file = user_name + '_hashtag.csv'

# Load data
df = pd.read_csv(user_data_file)

# Get all unique hashtags from 'content' column
all_hashtags = set(re.findall(r'@(\w+)', ' '.join(df['content'])))

while True:
    # User input for multiple hashtags (comma-separated)
    hashtag_names = input('Write comma-separated hashtag keywords that you want to retrieve: ').strip()

    if not hashtag_names:
        print("Please enter a hashtag. Do not press the enter key without typing any hashtag.")
        continue

    # Convert the input string to a list of hashtags
    hashtag_list = [hashtag.strip() for hashtag in hashtag_names.split(',')]

    # Check if all input hashtags are in 'content'
    if not all(hashtag in all_hashtags for hashtag in hashtag_list):
        invalid_hashtags = [hashtag for hashtag in hashtag_list if hashtag not in all_hashtags]
        print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
        continue

    break

# Function to check if any of the hashtags exists in the 'content' field
def find_hashtags(x):
    hashtags_in_content = []
    for hashtag in hashtag_list:
        if re.search(f"@{hashtag}", x):   
            hashtags_in_content.append(hashtag)
    return ', '.join(hashtags_in_content) if hashtags_in_content else ""

# Find rows where 'content' field contains any of the hashtags
df['hashtag_name'] = df['content'].apply(find_hashtags)

# Filter rows with at least one of the specified hashtags
df_hashtag = df[df['hashtag_name'].astype(bool)]   # changed this line to filter non-empty lists

# Delete the file if it exists
if os.path.exists(user_hashtag_file):
    os.remove(user_hashtag_file)

# Write to new CSV
df_hashtag.to_csv(user_hashtag_file, index=False)