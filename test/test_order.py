import pytest
import allure
from page.main_page import MainPageScooter
from page.order_page import OrderPageScooter

from locators.main_page_locators import MainPageLocators, ScooterFor, AboutRenta

@allure.epic('Эпик_Оформление заказа')
@allure.parent_suite('Parent_suite_Сквозные сценарии')
@allure.suite('Suite_Заказ самоката')

class TestYaScooterOrder:

    @allure.feature('Фича_Создание заказа')
    @allure.story('Стори_Позитивный сценарий с разными точками входа и данными')
    @allure.title('Оформление заказа самоката от начала до конца.')
    @allure.description('Проверка полного цикла заполнения формы заказа с параметризованными данными.')
    @pytest.mark.parametrize(
        "order_button_loc, name, surname, address, phone, metro_loc, select_date_loc, rent_loc, color_loc, comment", 
        [
            # === НАБОР ДАННЫХ №1 (Верхняя кнопка, Иван, Сокольники, 31 июля, 1 сутки, Черный) ===
            (
                MainPageLocators.BUTTON_ORDER_TOP,            # Точка входа: Верхняя кнопка
                "Иван", "Иванов", "ул. Ленина, д. 5", "89991112233", 
                ScooterFor.STATION_SOKOLNIKI,                 # Станция метро
                AboutRenta.SELECT_DATE_31_JULY,               # Локатор даты календаря
                AboutRenta.RENT_PERIOD_ONE_DAY,               # Срок: сутки
                AboutRenta.CHECKBOX_BLACK,                    # Цвет: черный
                "Позвонить за час"                            # Комментарий курьеру
            ),
            # === НАБОР ДАННЫХ №2 (Нижняя кнопка, Петр, Черкизовская, 30 июля, 2 суток, Серый) ===
            (
                MainPageLocators.BUTTON_ORDER_MIDDLE,         # Точка входа: Нижняя кнопка
                "Петр", "Петров", "проспект Мира, д. 12", "89994445566", 
                ScooterFor.STATION_CHERKIZOVSKAYA,            # Станция метро
                AboutRenta.SELECT_DATE_30_JULY,               # Локатор даты календаря
                AboutRenta.DROPDOWN_RENT_TWO_DAYS,            # Срок: двое суток
                AboutRenta.CHECKBOX_GREY,                     # Цвет: серый
                "Оставить у двери"                            # Комментарий курьеру
            )
        ]
    )
    def test_order_scooter_success(self, driver, order_button_loc, name, surname, address, phone, metro_loc, select_date_loc, rent_loc, color_loc, comment):
        home_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)
        
        
        
        # 2. Кликаем по кнопке "Заказать", локатор которой пришёл из параметризации
        home_page.click_order_button(order_button_loc) 
        
        # 3. Заполняем первый экран формы (ФИО, адрес, телефон и локатор станции)
        order_page.who_needs_a_scooter(name, surname, address, phone, metro_loc)
        
        # 4. Заполняем второй экран формы (локаторы даты, срока, цвета и текст комментария)
        order_page.aboot_renting(select_date_loc, rent_loc, color_loc, comment)
        
        # 5. НАШ АССЕРТ: Проверяем появление всплывающего окна с успешным заказом
        assert order_page.is_success_popup_displayed() is True, "Окно успешного оформления заказа не появилось!"
