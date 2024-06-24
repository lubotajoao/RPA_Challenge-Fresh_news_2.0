import traceback

from helper.clean_up_tasks import closing_apps
from helper.create_csv_log_file import create_csv_log_file
from helper.create_excel_report_file import create_excel_report_file
from helper.create_folder import create_folder
from helper.csv_log import csv_log
from helper.read_json_config_file import images_folder_path, output_folder_path, report_folder_path, log_csv_folder_path,  log_csv_file_name, project_name
from helper.config_dates import cur_date
from web.web_flow import web_flow

module_name = "rpa_challenge_fresh_news_2.0_main.py"
current_log_file = ""


def main():
    global module_name, current_log_file
    try:
        current_date = cur_date()

        # Creating Folder
        output_folder = create_folder(output_folder_path)

        images_folder = f"{images_folder_path}/{current_date}"
        csv_log_folder = f"{log_csv_folder_path}/{current_date}"
        report_folder = f"{report_folder_path}/{current_date}"

        current_images_folder = create_folder(folder_path=images_folder)
        current_csv_log_folder = create_folder(folder_path=csv_log_folder)
        current_report_folder = create_folder(folder_path=report_folder)

        # Creating Files
        current_log_file = create_csv_log_file(folder_path=current_csv_log_folder, file_name=log_csv_file_name, _date=current_date)
        excel_report_file = create_excel_report_file(report_path=current_report_folder, project_name=project_name, current_date=current_date)

        # Start Process
        status = "Start_Process"
        description = "The process has started."
        print(description)
        csv_log(file=current_log_file, project_name=project_name, task=module_name, status=status, description=description)

        # Clean_Up Tasks
        closing_apps(log_file=current_log_file, project_name=project_name)

        # Web Flow
        web_flow(log_file=current_log_file, project_name=project_name, excel_report_file=excel_report_file, images_folder=current_images_folder)

        # Clean_Up Tasks
        # closing_apps(log_file=current_log_file, project_name=project_name)

    except Exception as e:
        status = "Error"
        description = f'An error occurred in Orchestrator Module:\n[{e}][\n{traceback.format_exc()}]'
        print(description)
        csv_log(file=current_log_file, project_name=project_name, task=module_name, status=status, description=description)

    finally:
        # End Process
        status = "Finish_Process"
        description = "The process has finished."
        print(description)
        csv_log(file=current_log_file, project_name=project_name, task=module_name, status=status, description=description)


if __name__ == '__main__':
    main()
