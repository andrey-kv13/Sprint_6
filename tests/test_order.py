import pytest
import allure
from pages.order_page_methods import OrderPageMethods

class TestOrder:
    """Тесты для проверки оформления заказа"""
    
    @allure.epic("Самокаты")
    @allure.feature("Оформление заказа")
    @allure.story("Полный цикл заказа")
    @allure.title("Оформление заказа через {order_button[0]}")
    @pytest.mark.parametrize("button_name, test_data", 
                             OrderPageMethods.get_order_test_data())
    def test_order_submit(self, base_page_methods, order_page_methods, button_name, test_data):
        """Проверка успешного оформления заказа самоката
        
        Steps:
        1. Кликнуть на кнопку заказа в хедере/футере
        2. Заполнить форму личных данных
        3. Перейти к форме аренды
        4. Заполнить форму аренды
        5. Подтвердить заказ
        6. Проверить сообщение об успехе
        """
        
        try:
            with allure.step(f"Начать оформление заказа из {button_name}"):
                base_page_methods.click(button_name)
            
            with allure.step("Заполнить форму личных данных"):
                order_page_methods.populate_user_form_by_user_data(test_data)
            
            with allure.step("Перейти к форме аренды"):
                order_page_methods.click_next_button()
            
            with allure.step("Заполнить форму аренды"):
                order_page_methods.populate_order_form_by_user_data(test_data)

            with allure.step("Оформить заказ"):
                order_page_methods.click_order_button()
           
            with allure.step("Подтвердить заказ"):    
                order_page_methods.confirm_order()
            
            with allure.step("Проверить сообщение об успешном заказе"):
                message = order_page_methods.check_success_message_displayed()
                
                assert "Заказ оформлен" in message, \
                    f"Ожидалось 'Заказ оформлен', но получено: '{message}'"
            
        except Exception as e:
            pytest.fail(f"Тест завершился с ошибкой: {str(e)}")