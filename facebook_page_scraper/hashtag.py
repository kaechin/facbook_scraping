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
user_data_file = user_name + '.csv'
user_hashtag_file = user_name + '_hashtag.csv'

# Load data
df = pd.read_csv(user_data_file)

# Get all unique hashtags from 'content' column
df['content'] = df['content'].astype(str)   # Convert the 'content' column to str type
all_hashtags_at = set(re.findall(r'@(\w+)', ' '.join(df['content'])))
all_hashtags_hash = set(re.findall(r'#(\w+)', ' '.join(df['content'])))

# Checking if the file has no @ or #
if not all_hashtags_at and not all_hashtags_hash:
    print("The file does not contain any @ or #. Please use a different file.")
    os._exit(0)

# If the file has only one of @ or #, guide the user accordingly
if not all_hashtags_at:
    print("The file does not contain any @. You can only provide # as input.")
elif not all_hashtags_hash:
    print("The file does not contain any #. You can only provide @ as input.")

# User input for multiple @ hashtags (comma-separated)
if all_hashtags_at:
    while True:
        at_hashtag_names = input('Please enter at mark (@). Do not press the enter key without typing any hashtag: ').strip()
        if not at_hashtag_names:
            print("Please enter an at mark (@) hashtag.")
            continue

        # Convert the input string to a list of @ hashtags
        at_hashtag_list = [hashtag.strip() for hashtag in at_hashtag_names.split(',')]

        # Check if all input @ hashtags are in 'content'
        if not all(hashtag in all_hashtags_at for hashtag in at_hashtag_list):
            invalid_hashtags = [hashtag for hashtag in at_hashtag_list if hashtag not in all_hashtags_at]
            print(f"The at mark (@) hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different at mark (@) hashtag.")
            continue

        break
else:
    at_hashtag_list = []

# User input for multiple # hashtags (comma-separated)
if all_hashtags_hash:
    while True:
        hash_hashtag_names = input('Please enter hashtag (#). Do not press the enter key without typing any hashtag: ').strip()
        if not hash_hashtag_names:
            print("Please enter a hashtag (#).")
            continue

        # Convert the input string to a list of # hashtags
        hash_hashtag_list = [hashtag.strip() for hashtag in hash_hashtag_names.split(',')]

        # Check if all input # hashtags are in 'content'
        if not all(hashtag in all_hashtags_hash for hashtag in hash_hashtag_list):
            invalid_hashtags = [hashtag for hashtag in hash_hashtag_list if hashtag not in all_hashtags_hash]
            print(f"The hashtag(s) {', '.join(invalid_hashtags)} is/are not in the list. Please enter a different hashtag.")
            continue

        break
else:
    hash_hashtag_list = []

# Function to check if any of the hashtags exists in the 'content' field
def find_hashtags(x):
    atmarks_in_content = []
    hashtags_in_content = []
    for hashtag in at_hashtag_list:
        if re.search(f"@{hashtag}\\b", x):   
            atmarks_in_content.append(hashtag)
    for hashtag in hash_hashtag_list:
        if re.search(f"#{hashtag}\\b", x):   
            hashtags_in_content.append(hashtag)
    return atmarks_in_content, hashtags_in_content

# Find rows where 'content' field contains any of the hashtags
df['atmark_name'], df['hashtag_name'] = zip(*df['content'].apply(find_hashtags))

# Filter rows with at least one of the specified hashtags or atmarks
df_hashtag = df[df['atmark_name'].astype(bool) | df['hashtag_name'].astype(bool)]   # changed this line to filter non-empty lists

# Delete the file if it exists
if os.path.exists(user_hashtag_file):
    os.remove(user_hashtag_file)

# Write to new CSV
df_hashtag.to_csv(user_hashtag_file, index=False)