from .lib import open_browser
from .pages import LoginPage, TodoPage

browser = open_browser()
login_page = LoginPage(browser)
page = TodoPage(browser)

# Criar tarefa

login_page.open()
login_page.formulario.preencher(
    email='beto@cone.com',
    senha='123',
)
login_page.formulario.enviar()

assert page.is_in_page()

page.formulario.preencher(
    name='Dormir',
    desc='Pq é bom',
)
page.formulario.enviar()
cards = page.afazer.cards
assert any(card.name == 'Dormir' for card in cards)
assert any(card.description == 'Pq é bom' for card in cards)

browser.quit()
