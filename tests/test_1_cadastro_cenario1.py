from .lib import open_browser
from .pages import CadastroPage, TodoPage

browser = open_browser()
page = CadastroPage(browser)
page2 = TodoPage(browser)


# A aplicação deve redirecionar para a página de TODO ao registrar um usuário com sucesso

page.open()
page.formulario.preencher(
    nome='Beto Cone',
    email='beto@cone.com',
    senha='123',
)
page.formulario.enviar()

assert page2.is_in_page()

browser.quit()
