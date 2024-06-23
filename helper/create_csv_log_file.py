import csv
import os
import traceback

log_file = ""


def create_csv_log_file(folder_path: str, file_name: str, _date: str) -> str:
    global log_file
    try:
        log_file = f"{folder_path}/{file_name}_{str(_date)}.csv"

        if not os.path.isfile(log_file):
            header = ["Created_At", "Process_Name", "Module_Name", "User_Name", "Status", "Description"]

            with (open(log_file, 'w') as file):
                writer = csv.writer(file, delimiter=',', lineterminator='\n', )
                writer.writerow(header)
            file.close()

        return log_file

    except FileNotFoundError as e:
        print(f'An error occurred while creating the log file[{log_file}]:\n[{e}][\n{traceback.format_exc()}]')