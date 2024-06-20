from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None


def init_driver():
    global driver
    if driver is None:
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        options._use_chromium = True
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

        driver.maximize_window()
    return driver
