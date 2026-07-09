from selenium.webdriver.common.by import By


class MainPageLocators:
    FAQ_BUTTONS = [By.CLASS_NAME, 'accordion__button']
    FAQ_PANELS = [By.CLASS_NAME, 'accordion__panel']
    BUTTON_ORDER_TOP = [By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']"]
    BUTTON_ORDER_MIDDLE = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]

    
class ScooterFor:
    INPUT_NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    INPUT_SURNAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    INPUT_ADRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    DROPDOWN_METRO_STATION = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    STATION_SOKOLNIKI = [By.XPATH, "//*[text()='Сокольники']"]
    STATION_CHERKIZOVSKAYA = [By.XPATH, "//*[text()='Черкизовская']"]

    INPUT_PHONE = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]

class AboutRenta:
    INPUT_DAT_RENTA = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    SELECT_DATE_31_JULY = [By.XPATH, "//div[contains(@aria-label, '31-е июля 2026')]"]
    SELECT_DATE_30_JULY = [By.XPATH, "//div[contains(@aria-label, '30-е июля 2026')]"]


    BUTTON_RENT_DAYS = [By.CLASS_NAME, "Dropdown-control"]
    
    DROPDOWN_RENT_TWO_DAYS = [By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"]
    RENT_PERIOD_ONE_DAY = [By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"]
    
    CHECKBOX_BLACK = [By.ID, "black"]
    CHECKBOX_GREY = [By.ID, "grey"]
    
    INPUT_COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    BUTTON_FINAL_ORDER = [By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"]
class ReadyToOrder:
    POPUP_CONFIRM_HEADER = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Хотите оформить заказ?']"]
    BUTTON_YES = [By.XPATH, "//button[text()='Да']"]
    POPUP_SUCCESS_HEADER = [By.XPATH, "//*[contains(text(), 'Заказ оформлен')]"]

