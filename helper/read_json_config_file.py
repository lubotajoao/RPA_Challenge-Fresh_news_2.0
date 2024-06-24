import json

with open("config.json", "rb") as read_file:
    configFile = json.load(read_file)

# Folders
base_path = configFile['BASE_PATH']
input_folder_path = f"{base_path}/Input"
output_folder_path = f"{base_path}/Output"
images_folder_path = f"{output_folder_path}/Images"
report_folder_path = f"{output_folder_path}/Reports"
log_csv_folder_path = f"{output_folder_path}/CSV Logs"

# Files
log_csv_file_name = configFile['LOG_CSV_DEFAULT_FILENAME']
project_name = configFile['PROJECT_NAME']
input_filename = configFile['INPUT_FILENAME']
input_file_path = f"{input_folder_path}/{input_filename}.xlsx"

# Search Parameters
search_url = configFile['SEARCH_URL']
search_phrase = configFile['SEARCH_PHRASE']
search_sort = configFile['SORT']
