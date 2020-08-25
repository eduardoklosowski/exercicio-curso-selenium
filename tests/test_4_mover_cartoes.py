from .lib import open_browser
from .pages import LoginPage, TodoPage

browser = open_browser()
login_page = LoginPage(browser)
page = TodoPage(browser)

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
page.formulario.preencher(
    name='Acordar',
    desc='Pois é necessário',
)
page.formulario.enviar()
page.formulario.preencher(
    name='Comer',
    desc='Se não eu morro',
)
page.formulario.enviar()


# Mover tarefa para Fazendo

[card.name == 'Dormir' for card in page.afazer.cards][0].do()
assert any(card.name == 'Dormir' for card in page.fazendo.cards)
assert any(card.name == 'Acordar' for card in page.afazer.cards)
assert any(card.name == 'Comer' for card in page.afazer.cards)


# Mover tarefa para Pronto

[card.name == 'Dormir' for card in page.fazendo.cards][0].do()
assert any(card.name == 'Dormir' for card in page.pronto.cards)


# Voltar cartão para A fazer

[card.name == 'Dormir' for card in page.pronto.cards][0].cancel()
assert any(card.name == 'Dormir' for card in page.afazer.cards)


# Cancelar cartão

[card.name == 'Dormir' for card in page.pronto.cards][0].cancel()
assert not any(card.name == 'Dormir' for card in page.afazer.cards)


# Cartões devem ser carregados nas colunas corretas

browser.refresh()
[card.name == 'Dormir' for card in page.afazer.cards][0].do()
[card.name == 'Dormir' for card in page.fazendo.cards][0].do()
[card.name == 'Acordar' for card in page.afazer.cards][0].do()
browser.refresh()
assert any(card.name == 'Acordar' for card in page.fazendo.cards)
assert any(card.name == 'Dormir' for card in page.pronto.cards)

browser.quit()
