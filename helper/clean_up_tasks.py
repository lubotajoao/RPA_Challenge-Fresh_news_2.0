import psutil
from AppOpener import close
from helper.csv_log import csv_log

module_name = "clean_up_tasks.py"
description = ''
status = "Log"


def closing_apps(log_file: str, project_name: str) -> None:
    global description, status
    try:
        for process in psutil.process_iter():
            if process.name() == "msedge.exe":
                close("msedge")
                description = "Microsoft Edge task closed successfully."
                csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)

            if process.name() == "EXCEL.EXE":
                close("EXCEL")
                description = "Microsoft Excel task closed successfully."
                csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)

    except Exception as e:
        status = "Error"
        description = f'An error occurred in Clean Up Tasks Module: [{e}].'
        print(description)
        csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)
