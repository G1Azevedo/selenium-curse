import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
        driver.find_element(By.XPATH, "//*[@id ='add-to-cart']").click()
        driver.find_element(By.XPATH, "//*[@class ='shopping_cart_badge']").click()
        assert driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").is_displayed()
        print ('O item foi adicionado com sucesso!')



