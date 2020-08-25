from .lib import open_browser
from .pages import LoginPage

browser = open_browser()
page = LoginPage(browser)


# Mensagens do formulário

page.open()
page.formulario.focar_email()
assert page.formulario.get_texto_label_email() == 'Tá certo?'
page.formulario.focar_senha()
assert page.formulario.get_texto_label_senha() == 'Não vai errar'

browser.quit()
