from .lib import open_browser
from .pages import LoginPage, TodoPage

browser = open_browser()
page = LoginPage(browser)
page2 = TodoPage(browser)


# Login com credenciais válidas

page.open()
page.formulario.preencher(
    email='beto@cone.com',
    senha='123',
)
page.formulario.enviar()

assert page2.is_in_page()

browser.quit()
