from .lib import open_browser
from .pages import LoginPage, TodoPage

browser = open_browser()
login_page = LoginPage(browser)
page = TodoPage(browser)


# Carregamento automático das TODOS

login_page.open()
login_page.formulario.preencher(
    email='beto@cone.com',
    senha='123',
)
login_page.formulario.enviar()

assert page.is_in_page()

page.formulario.preencher(
    name='Liga para Beto',
    desc='Telefone +15 51515151',
    urgent=False,
)
page.formulario.enviar()
page.formulario.preencher(
    name='ir no mercado',
    desc='Promoção no mercado x',
    urgent=True,
)
page.formulario.enviar()
browser.refresh()


cards = page.afazer.cards
assert any(card.name == 'Liga para Beto' for card in cards)
assert any(card.description == 'Telefone +15 51515151' for card in cards)
assert any(card.name == 'ir no mercado' for card in cards)
assert any(card.description == 'Promoção no mercado x' for card in cards)
assert cards[0].name == 'ir no mercado'
assert cards[1].description == 'Promoção no mercado x'

browser.quit()
