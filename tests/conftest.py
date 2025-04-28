import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


#переписано на использование geckodrivermanager без указания пути на компуктере.. до этого убунта сходила с ума
#и не давала юзать вебдрайвер(
@pytest.fixture
def driver():

    firefox = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    firefox.maximize_window()
    firefox.get('https://qa-scooter.praktikum-services.ru/')
    yield firefox
    firefox.quit()