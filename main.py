import traceback
from helper.create_csv_log_file import create_csv_log_file
from helper.create_excel_report_file import create_excel_report_file
from helper.create_folder import create_folder
from helper.csv_log import csv_log
from web.web_init_driver import init_driver
from helper.read_json_config_file import input_folder_path, output_folder_path, report_folder_path, log_csv_folder_path,  log_csv_file_name, project_name, input_file_path
from helper.config_dates import cur_day, cur_month, cur_year, cur_date

module_name = "rpa_challenge_fresh_news_2.0_main.py"
current_log_file = ""


def main():
    global module_name, current_log_file
    try:
        # Process Dates
        current_day = cur_day()
        current_month = cur_month()
        current_year = cur_year()
        current_date = cur_date()

        # Creating Folder
        output_folder = create_folder(output_folder_path)

        csv_log_folder = f"{log_csv_folder_path}/{current_date}"
        report_folder = f"{report_folder_path}/{current_date}"

        current_csv_log_folder = create_folder(folder_path=csv_log_folder)
        current_report_folder = create_folder(folder_path=report_folder)

        # Creating Files
        current_log_file = create_csv_log_file(folder_path=current_csv_log_folder, file_name=log_csv_file_name, _date=current_date)
        excel_report_file = create_excel_report_file(report_path=current_report_folder, project_name=project_name, current_date=current_date)

        # Start Process
        status = "Start_Process"
        description = "The process has started."
        print(description)
        csv_log(file=current_log_file, process=project_name, task=module_name, status=status, description=description)

        # init_driver()

    except Exception as e:
        status = "Error"
        description = f'An error occurred in Orchestrator Module:\n[{e}][\n{traceback.format_exc()}]'
        print(description)
        csv_log(file=current_log_file, process=project_name, task=module_name, status=status, description=description)

    finally:
        # End Process
        status = "Finish_Process"
        description = "The process has finished."
        print(description)
        csv_log(file=current_log_file, process=project_name, task=module_name, status=status, description=description)


if __name__ == '__main__':
    main()
