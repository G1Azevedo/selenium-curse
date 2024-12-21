from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

# Fazendo login
driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

# Adicionando mochila ao carrinho
driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
driver.find_element(By.XPATH, "//*[@id ='add-to-cart']").click()

# Verificando se a mochila foi adicionada
driver.find_element(By.XPATH, "//*[@class ='shopping_cart_badge']").click()
assert driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").is_displayed()
print ('O item foi adicionado com sucesso!')

# Retornando para a tela de produtos
driver.find_element(By.ID, 'continue-shopping').click()

# Adicionando mais um produto ao carrinho
driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").click()
driver.find_element(By.XPATH, "//*[@id ='add-to-cart']").click()

# Verificando se os dois produtos estão na mochila
driver.find_element(By.XPATH, "//*[@class ='shopping_cart_badge']").click()
assert driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").is_displayed()
assert driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").is_displayed()
print ('Os dois produtos foram adicionados com sucesso.')
