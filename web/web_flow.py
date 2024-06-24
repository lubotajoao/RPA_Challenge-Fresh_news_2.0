import traceback

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

from excel.excel_set_report_info import excel_set_report_info
from helper.csv_log import csv_log
from helper.config_dates import cur_date
from helper.read_json_config_file import search_url, search_phrase, search_sort
from web.check_element_exists import check_element_exists

module_name = "web_flow.py"
driver = None


def web_flow(log_file: str, project_name: str, excel_report_file: str, images_folder: str) -> None:
    global module_name, driver
    try:
        current_url = f"{search_url}/search/{search_phrase}?"
        print(current_url)

        options = webdriver.EdgeOptions()
        options.use_chromium = True
        options.add_experimental_option("detach", True)
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

        status = "Info"
        description = f"Launching web browser using [{current_url}] URL."
        csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)

        driver.maximize_window()
        driver.get(current_url)

        element_exists = check_element_exists(driver, By.CLASS_NAME, 'site-logo')
        if element_exists:
            status = "Log"
            description = f"Web browser launched successfully."
            csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)

            search_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "search-bar__button")))
            search_btn.click()

            sleep(2)
            dropdown_element = driver.find_element(By.ID, "search-sort-option")
            select = Select(dropdown_element)
            select.select_by_visible_text(f"{search_sort}")

            sleep(2)
            wait = WebDriverWait(driver, 10)
            div_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-result__list')))
            articles = div_element.find_elements(By.TAG_NAME, 'article')
            total_articles = len(articles)
            print(f'Total number of articles: {total_articles}')

            # Inserting Data into Excel File
            # excel_set_report_info(log_file=log_file, project_name=project_name, report_file=excel_report_file, title=title, date=str(date), description=description,
            #                      picture_filename=picture_filename, count_search_phrase=count_search_phrase, picture_file_path=picture_file_path)

        else:
            status = "Error"
            description = f"An error occurred while launching web browser."
            csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)

        sleep(10)

    except Exception as e:
        status = "Error"
        description = f'An error occurred in Web Flow Module:\n[{e}][\n{traceback.format_exc()}]'
        print(description)
        csv_log(file=log_file, project_name=project_name, task=module_name, status=status, description=description)
    finally:
        # driver.quit()
        pass
