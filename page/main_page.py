
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators



class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver

    def click_question(self, question_number):
        buttons = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(MainPageLocators.FAQ_BUTTONS)
        )
        buttons[question_number].click()

    def get_answer_text(self, answer_number):
        panels = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(MainPageLocators.FAQ_PANELS)
        )
        return panels[answer_number].text
    

        
    def click_order_button(self, button_locator):
        # 1. Ждём появления переданной кнопки на странице
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(button_locator)
        )
        
        # 2. ПРОСТОЙ СКРОЛЛ: Нативно подкатываем страницу к элементу
        element.location_once_scrolled_into_view
        
        # 3. СТРАХОВКА ОТ ПЕРЕКРЫТИЯ ШАПКОЙ: Чуть-чуть приподнимаем страницу вверх,
        # чтобы кнопка вышла из-под чёрного хедера сайта
        self.driver.execute_script("window.scrollBy(0, -150);")
        
        # 4. Небольшая пауза для Mac, чтобы координаты зафиксировались
        import time
        time.sleep(0.5)
        
        # 5. Кликаем по кнопке, которая теперь в полной безопасности
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(button_locator)
        ).click()
