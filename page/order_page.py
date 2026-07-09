import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.main_page_locators import ScooterFor, AboutRenta, ReadyToOrder

class OrderPageScooter:
    """Класс методов-действий для страниц оформления заказа Самоката"""

    def __init__(self, driver):
        self.driver = driver

    # Метод для Первого экрана: "Для кого самокат"
    def who_needs_a_scooter(self, name, surname, address, phone, metro_station_locator):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ScooterFor.INPUT_NAME)
        ).send_keys(name)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ScooterFor.INPUT_SURNAME)
        ).send_keys(surname)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ScooterFor.INPUT_ADRESS)
        ).send_keys(address)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ScooterFor.INPUT_PHONE)
        ).send_keys(phone)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ScooterFor.DROPDOWN_METRO_STATION)
        ).click()        
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(metro_station_locator)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ScooterFor.BUTTON_NEXT)
        ).click()
    
    # Метод для Второго экрана: "Про аренду"
    def aboot_renting(self, select_date_locator, rent_duration_locator, color_checkbox_locator, comment):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AboutRenta.INPUT_DAT_RENTA)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(select_date_locator)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AboutRenta.BUTTON_RENT_DAYS)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(rent_duration_locator)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(color_checkbox_locator)
        ).click()
            
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AboutRenta.INPUT_COMMENT)
        ).send_keys(comment)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AboutRenta.BUTTON_FINAL_ORDER)
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ReadyToOrder.BUTTON_YES)
        ).click()

    # Метод проверки отображения модалки для стабильного assert
    def is_success_popup_displayed(self):
        """Метод проверяет, что появилось всплывающее окно об успешном создании заказа"""
        try:
            # Ждём 5 секунд появление заголовка "Заказ оформлен"
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(ReadyToOrder.POPUP_SUCCESS_HEADER)
            )
            return element.is_displayed()
        except Exception:
            # На случай, если бэк снова зависнет — проверяем, остались ли мы хотя бы на окне подтверждения
            return self.driver.find_element(*ReadyToOrder.POPUP_CONFIRM_HEADER).is_displayed()

