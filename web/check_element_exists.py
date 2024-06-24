from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def check_element_exists(driver: webdriver, by: str, value) -> bool:
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False
