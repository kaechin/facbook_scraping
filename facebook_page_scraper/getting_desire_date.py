# import os
# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('arnold.csv')

# # Prompt the user for start and end dates
# start_specific_date = input("Enter the start date in YYYY-MM-DD format: ")
# end_specific_date = input("Enter the end date in YYYY-MM-DD format: ")

# # Convert the user inputs to datetime objects
# start_date = pd.to_datetime(start_specific_date, errors='coerce')
# end_date = pd.to_datetime(end_specific_date, errors='coerce')

# # Modify the end date to be inclusive (add 1 day)
# end_date = end_date + pd.DateOffset(days=1)

# # Filter the data based on the specified date range
# df['posted_on'] = pd.to_datetime(df['posted_on'], errors='coerce')  # Convert the 'posted_on' column to datetime
# filtered_df = df[(df['posted_on'] >= start_date) & (df['posted_on'] < end_date)]  # Use '<' for the end date comparison


# # Drop rows with invalid dates (NaT) if any
# filtered_df = filtered_df.dropna(subset=['posted_on'])

# # Check if the filtered dataframe is empty
# if filtered_df.empty:
#     # If no data within the specified date range, suggest the user to enter a date range within the available data range
#     min_date = df['posted_on'].min().strftime('%Y-%m-%d')
#     max_date = df['posted_on'].max().strftime('%Y-%m-%d')
#     print(f"No data found within the specified date range.")
#     print(f"Please enter a date range between {min_date} and {max_date}.")
# else:
#     # Save the filtered data to a new CSV file
#     output_file = 'arnold_specific_date.csv'
    
#     # Check if the output file already exists, and delete it if it does
#     if os.path.exists(output_file):
#         os.remove(output_file)

#     filtered_df.to_csv(output_file, index=False)
#     print("Filtered data has been saved to 'arnold_specific_date.csv'.")

import os
import pandas as pd

# Read the CSV file
input_file = input("Enter the name of the input CSV file: ")
df = pd.read_csv(f'{input_file}.csv')

# Prompt the user for start and end dates
start_specific_date = input("Enter the start date in YYYY-MM-DD format: ")
end_specific_date = input("Enter the end date in YYYY-MM-DD format: ")

# Convert the user inputs to datetime objects
start_date = pd.to_datetime(start_specific_date, errors='coerce')
end_date = pd.to_datetime(end_specific_date, errors='coerce')

# Modify the end date to be inclusive (add 1 day)
end_date = end_date + pd.DateOffset(days=1)

# Filter the data based on the specified date range
df['posted_on'] = pd.to_datetime(df['posted_on'], errors='coerce')  # Convert the 'posted_on' column to datetime
filtered_df = df[(df['posted_on'] >= start_date) & (df['posted_on'] < end_date)]  # Use '<' for the end date comparison

# Drop rows with invalid dates (NaT) if any
filtered_df = filtered_df.dropna(subset=['posted_on'])

# Check if the filtered dataframe is empty
if filtered_df.empty:
    # If no data within the specified date range, suggest the user enter a date range within the available data range
    min_date = df['posted_on'].min().strftime('%Y-%m-%d')
    max_date = df['posted_on'].max().strftime('%Y-%m-%d')
    print(f"No data found within the specified date range.")
    print(f"Please enter a date range between {min_date} and {max_date}.")
else:
    # Create the output CSV file name
    output_file = f"{input_file}_specific_date.csv"

    # Check if the output file already exists, and delete it if it does
    if os.path.exists(output_file):
        os.remove(output_file)

    filtered_df.to_csv(output_file, index=False)
    print(f"Filtered data has been saved to '{output_file}'.")