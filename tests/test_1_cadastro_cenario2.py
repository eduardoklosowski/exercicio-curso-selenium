from .lib import open_browser
from .pages import CadastroPage, TodoPage

browser = open_browser()
page = CadastroPage(browser)
page2 = TodoPage(browser)


# A aplicação deve redirecionar para a página de register ao tentar cadastrar um usuário com e-mail já cadastrado

page.open()
page.formulario.preencher(
    nome='Beto Cone',
    email='beto@cone.com',
    senha='123',
)
page.formulario.enviar()

assert page2.is_in_page()
page2.logout.fazer_logout()

assert page.is_in_page()
page.open()
page.formulario.preencher(
    nome='Beto Cone',
    email='beto@cone.com',
    senha='123',
)
page.formulario.enviar()
assert page.formulario.get_texto_alerta() == 'Algo deu errado!'

browser.quit()
