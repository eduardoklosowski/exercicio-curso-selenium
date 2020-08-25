from abc import ABC

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from .lib import PageElement


class FormularioCadastro(PageElement):
    label_nome = By.CSS_SELECTOR, '.create-todo label[for=nome]'
    input_nome = By.CSS_SELECTOR, '.create-todo input[name=nome]'
    label_email = By.CSS_SELECTOR, '.create-todo label[for=email]'
    input_email = By.CSS_SELECTOR, '.create-todo form input[name=email]'
    label_senha = By.CSS_SELECTOR, '.create-todo label[for=senha]'
    input_senha = By.CSS_SELECTOR, '.create-todo input[name=senha]'
    submit = By.CSS_SELECTOR, '.create-todo input[type=submit]'
    alerta = By.CSS_SELECTOR, '.create-todo .terminal-alert-error'

    def digitar_nome(self, valor):
        self.find_element(self.input_nome).send_keys(valor)

    def focar_nome(self):
        self.find_element(self.input_nome).click()

    def get_texto_label_nome(self):
        return self.find_element(self.label_nome).text

    def digitar_email(self, valor):
        self.find_element(self.input_email).send_keys(valor)

    def focar_email(self):
        self.find_element(self.input_email).click()

    def get_texto_label_email(self):
        return self.find_element(self.label_email).text

    def digitar_senha(self, valor):
        self.find_element(self.input_senha).send_keys(valor)

    def focar_senha(self):
        self.find_element(self.input_senha).click()

    def get_texto_label_senha(self):
        return self.find_element(self.label_senha).text

    def preencher(self, nome, email, senha):
        self.digitar_nome(nome)
        self.digitar_email(email)
        self.digitar_senha(senha)

    def enviar(self):
        self.find_element(self.submit).click()

    def get_texto_alerta(self):
        return self.find_element(self.alerta).text


class FormularioLogin(PageElement):
    label_email = By.CSS_SELECTOR, '.create-todo label[for=email]'
    input_email = By.CSS_SELECTOR, '.create-todo form input[name=email]'
    label_senha = By.CSS_SELECTOR, '.create-todo label[for=senha]'
    input_senha = By.CSS_SELECTOR, '.create-todo input[name=senha]'
    submit = By.CSS_SELECTOR, '.create-todo input[type=submit]'
    alerta = By.CSS_SELECTOR, '.create-todo .terminal-alert-error'

    def digitar_email(self, valor):
        self.find_element(self.input_email).send_keys(valor)

    def focar_email(self):
        self.find_element(self.input_email).click()

    def get_texto_label_email(self):
        return self.find_element(self.label_email).text

    def digitar_senha(self, valor):
        self.find_element(self.input_senha).send_keys(valor)

    def focar_senha(self):
        self.find_element(self.input_senha).click()

    def get_texto_label_senha(self):
        return self.find_element(self.label_senha).text

    def preencher(self, email, senha):
        self.digitar_email(email)
        self.digitar_senha(senha)

    def enviar(self):
        self.find_element(self.submit).click()

    def get_texto_alerta(self):
        return self.find_element(self.alerta).text


class FormularioTodo(PageElement):
    input_name = By.CSS_SELECTOR, 'input[name=name]'
    input_desc = By.CSS_SELECTOR, 'textarea[name=desc]'
    input_urgent = By.CSS_SELECTOR, 'input[type=checkbox,name=urgent]'
    submit = By.CSS_SELECTOR, 'input#submit'

    def digitar_name(self, valor):
        self.find_element(self.input_name).send_keys(valor)

    def digitar_desc(self, valor):
        self.find_element(self.input_desc).send_keys(valor)

    def marcar_urgent(self):
        self.find_element(self.input_urgent).click()

    def preencher(self, name, desc, urgent=False):
        self.digitar_name(name)
        self.digitar_desc(desc)
        if urgent:
            self.marcar_urgent()

    def enviar(self):
        self.find_element(self.submit).click()


class Logout(PageElement):
    submit = By.CSS_SELECTOR, 'form[action=logout] input[type=submit]'

    def fazer_logout(self):
        self.find_element(self.submit).click()


class CardContainer(PageElement, ABC):
    card = By.CSS_SELECTOR, '.terminal-card'

    @property
    def cards(self):
        card_elements = self.find_element(self.fieldset).find_elements(self.card)
        cards = [Card(card) for card in card_elements]
        return cards


class AFazer(CardContainer):
    fieldset = By.CSS_SELECTOR, 'div.todo fieldset'


class Fazendo(CardContainer):
    fieldset = By.CSS_SELECTOR, 'div.doing fieldset'


class Pronto(CardContainer):
    fieldset = By.CSS_SELECTOR, 'div.done fieldset'


class Card:
    def __init__(self, selenium_object):
        self.selenium_object = selenium_object
        self.label_name = By.CSS_SELECTOR, 'header'
        self.label_description = By.CSS_SELECTOR, 'div'
        self.button_do = By.CSS_SELECTOR, 'button.do'
        self.button_cancel = By.CSS_SELECTOR, 'button.cancel'

    def __repr__(self):
        return f'Card(name={self.name!r}, description={self.description!r})'

    @property
    def name(self):
        name = self.selenium_object.find_element(*self.label_name).text
        return name.split(' #')[0]

    @property
    def description(self):
        return self.selenium_object.find_element(*self.label_description).text

    def do(self):
        self.selenium_object.find_element(*self.button_do).click()

    def cancel(self):
        try:
            self.selenium_object.find_element(*self.button_cancel).click()
        except NoSuchElementException:
            print('Elemento não tem cancelar')
