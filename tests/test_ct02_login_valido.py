import pytest
from pages.login_pages import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self):
        # Instância os objetos a serem usados no teste
        login_pages = LoginPage()
        home_page = HomePage()

        # Faz o login
        login_pages.fazer_login('standard_user', 'secret_sauce')
        
        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()