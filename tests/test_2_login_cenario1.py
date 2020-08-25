from .lib import open_browser
from .pages import LoginPage

browser = open_browser()
page = LoginPage(browser)


# Login com credenciais inválidas

page.open()
page.formulario.preencher(
    email='beto@cone.com',
    senha='321',
)
page.formulario.enviar()

assert page.is_in_page()
assert page.formulario.get_texto_alerta() == 'Email ou senha inválidos!'

browser.quit()
