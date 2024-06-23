import csv
import os
from datetime import datetime
from time import sleep


def csv_log(file: str, process: str, task: str, status: str, description: str) -> None:
    try:
        created_at = datetime.now()
        logged_user = os.getlogin()

        process = process.strip()
        status = status.strip()
        description = description.strip()

        description = description.replace("\n", "")
        description = description.replace("         ~~^~~", "")
        description = description.replace("   ", "")

        # Getting the task_name even if it is from the absolute path string ("path/to/delete_file.py"). delete_file.py will be taken.
        if "/" in task:
            task = task[task.rindex('/') + 1:]
            task = task.strip()
        elif "\\" in task:
            task = task[task.rindex('\\') + 1:]
            task = task.strip()

        # "Created_At", "Process", "Task/Module", "User_Name", "Status", "Description"
        data = [str(created_at), str(process), str(task), str(logged_user), str(status), str(description)]

        sleep(1)
        with (open(file, 'a') as file):
            writer = csv.writer(file, delimiter=',', lineterminator='\n', )
            writer.writerow(data)
        file.close()

    except FileNotFoundError as e:
        print(f'An error occurred while setting info into the csv log file:\n[{e}]')
