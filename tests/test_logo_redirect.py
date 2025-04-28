import allure
from page_objects.main_page import MainPage

class TestLogoRedirect:
    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_redirect_to_main_page_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_order_button_in_header()   #проверяем видимость кнопки заказать в хедере
        main_page.click_on_order_button_in_header() #кликаем её
        main_page.wait_visibility_of_header_logo_scooter()  #проверка видимости лого самоката
        main_page.click_on_header_logo_scooter()    #кликаем её
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на Дзен через лого Яндекса')
    def test_logo_redirect_to_dzen_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        current_url = main_page.wait_url_contains("dzen.ru") #убран webdriverwait
        assert "dzen.ru" in current_url