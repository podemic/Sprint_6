import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os
import time


@pytest.fixture(scope="function")
def driver():
    os.system("pkill -f firefox")
    os.system("pkill -f geckodriver")
    time.sleep(1)


    options = Options()
    options.binary_location = "/opt/firefox/firefox"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")


    service = Service(
        executable_path="/usr/local/bin/geckodriver",
        service_args=["--log", "debug"]
    )
    service.start_timeout = 30

    try:
        driver = webdriver.Firefox(
            service=service,
            options=options
        )
        driver.set_page_load_timeout(30)
        driver.get('https://qa-scooter.praktikum-services.ru/')
        yield driver
    except Exception as e:
        pytest.fail(f"Ошибка инициализации драйвера: {str(e)}")
    finally:
        try:
            driver.quit()
        except:
            pass
        os.system("pkill -f firefox")
        os.system("pkill -f geckodriver")