from .lib import open_browser
from .pages import CadastroPage

browser = open_browser()
page = CadastroPage(browser)


# Mensagens do formulário

page.open()
page.formulario.focar_nome()
assert page.formulario.get_texto_label_nome() == 'Lembre-se de colocar um falso'
page.formulario.focar_email()
assert page.formulario.get_texto_label_email() == 'Se for válido, todo mundo vai saber'
page.formulario.focar_senha()
assert page.formulario.get_texto_label_senha() == 'Será que é segura?'

browser.quit()
