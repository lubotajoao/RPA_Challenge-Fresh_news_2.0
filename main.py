from web.web_init_driver import init_driver
from helper.read_json_config_file import input_folder_path, output_folder_path, report_folder_path, log_csv_folder_path,  log_csv_file_name, project_name, input_file_path
from helper.config_dates import cur_day, cur_month, cur_year


def main():
    try:
        # Starting Process
        print("The process has started.")

        # Process Dates
        current_day = cur_day()
        current_moth = cur_month()
        current_year = cur_year()

        print(current_day, current_moth, current_year)

        # Config file inputs
        print(input_folder_path)
        print(output_folder_path)
        print(report_folder_path)
        print(log_csv_folder_path)
        print(log_csv_file_name)
        print(project_name)
        print(input_file_path)

        # Creating Log and Process folder

        # init_driver()

    except Exception as e:
        print(f'An error occurred in Orchestrator Module:\n[{e}]')

    finally:
        # End Process
        print("The process has finished.")


if __name__ == '__main__':
    main()
