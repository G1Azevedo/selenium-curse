import pytest
from pages.login_pages import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
class TestCT05:
    def test_ct05_retorna_e_add_produto(self):
        login_pages = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = 'Sauce Labs Backpack'
        produto_2 = 'Sauce Labs Bolt T-Shirt'

        # Faz o login
        login_pages.fazer_login('standard_user', 'secret_sauce')

        # Adicionando mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando se a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Retornando para a tela de produtos
        carrinho_page.clicar_continuar_comprando()

        # Adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # # Verificando se os dois produtos estão na mochila
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)
