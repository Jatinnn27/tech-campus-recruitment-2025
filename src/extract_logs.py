import json
import random
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


# Path to your .log file
log_file_path = r"C:\Users\Lenovo\test_logs.log"

# Function to extract the JSON data
def extract_json_from_log(log_file_path):
    # Open and read the log file
    with open(log_file_path, 'r', encoding='utf-8') as file:
        # Read the file content
        content = file.read()

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Find the script tag containing the JSON object
    script_tag = soup.find('script', text=lambda text: text and 'window.ENV' in text)

    if script_tag:
        # Extract the JSON part from the script tag
        json_text = script_tag.string.split('window.ENV = ')[1].strip(';')

        try:
            # Parse the JSON text
            json_data = json.loads(json_text)
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        print("No script tag with window.ENV found.")
        return None

# Extract the JSON data
json_data = extract_json_from_log(log_file_path)

if json_data:
    print("Extracted JSON data:")
    print(json.dumps(json_data, indent=4))
else:
    print("No JSON data found.")



# Parse the JSON
log_data = json.loads(json.dumps(json_data, indent=4))

# Generate a random timestamp for each log entry and assign a log level
log_levels = ["INFO", "ERROR", "WARN"]

# Function to generate a random timestamp
def generate_random_timestamp():
    base_time = datetime.strptime(log_data["NOW"], "%Y-%m-%dT%H:%M:%S.%fZ")
    time_diff = timedelta(minutes=random.randint(1, 60), seconds=random.randint(0, 59))
    new_time = base_time + time_diff
    return new_time.strftime("%Y-%m-%d %H:%M:%S")

# Create a list of log entries with random timestamps and log levels
log_entries = [
    f"{generate_random_timestamp()} {random.choice(log_levels)} User logged in",
    f"{generate_random_timestamp()} {random.choice(log_levels)} Failed to connect to the database",
    f"{generate_random_timestamp()} {random.choice(log_levels)} Disk space running low"
]

# Print the formatted log entries
for log in log_entries:
    print(log)