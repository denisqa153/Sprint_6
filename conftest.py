import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    with allure.step('Открыть браузер и перейти на сайт'):
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.get("https://qa-scooter.education-services.ru/")

    with allure.step('Принять куки'):
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        ).click()

    yield browser

    with allure.step('Закрыть браузер'):
        browser.quit()