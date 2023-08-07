import csv
import os
import datetime as dt

# Prompt the user for the CSV file name
while True:
    input_file = input("Enter the name of the input CSV file: ")
    if not input_file:
        print("Please enter a valid CSV file name.")
    elif not os.path.isfile(f'{input_file}.csv'):
        print("The file does not exist. Please try again.")
    else:
        break

# Open the CSV file and read it into a list of dictionaries
with open(f'{input_file}.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Convert 'posted_on' column to datetime and sort it in ascending order
for row in data:
    row['posted_on'] = dt.datetime.strptime(row['posted_on'].split('T')[0], "%Y-%m-%d")

# Sort data by date
data.sort(key=lambda x: x['posted_on'])

# Display the min and max dates in the 'posted_on' column after conversion to datetime
print("After conversion:")
print(f"Earliest date: {data[0]['posted_on'].strftime('%Y-%m-%d')}")
print(f"Latest date: {data[-1]['posted_on'].strftime('%Y-%m-%d')}")

filtered_data = []
while not filtered_data:
    # Prompt the user for start and end dates
    while True:
        start_specific_date = input("Enter the start date in YYYY-MM-DD format: ")
        end_specific_date = input("Enter the end date in YYYY-MM-DD format: ")

        # If user just hits enter without typing anything
        if not start_specific_date or not end_specific_date:
            print("Please provide both the start date and end date.")
        else:
            break

    # Convert the user inputs to datetime objects
    start_date = dt.datetime.strptime(start_specific_date, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end_specific_date, "%Y-%m-%d")

    # Filter the data based on the specified date range
    filtered_data = [row for row in data if start_date <= row['posted_on'] <= end_date]

    # Check if the filtered data is empty
    if not filtered_data:
        # If no data within the specified date range, suggest the user enter a date range within the available data range
        min_date = data[0]['posted_on'].strftime('%Y-%m-%d')
        max_date = data[-1]['posted_on'].strftime('%Y-%m-%d')
        print(f"No data found within the specified date range.")
        print(f"Please enter a date range between {min_date} and {max_date}.")

# Create the output CSV file name
output_file = f"{input_file}_specific_date.csv"

# Check if the output file already exists, and delete it if it does
if os.path.exists(output_file):
    os.remove(output_file)

# Write the filtered data to the new CSV file
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

print(f"Filtered data has been saved to '{output_file}'.")
