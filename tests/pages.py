from urllib.parse import urljoin

from .elements import FormularioCadastro, FormularioLogin, FormularioTodo, Logout, AFazer, Fazendo, Pronto
from .lib import Page

BASE_URL = 'https://todo-brython.herokuapp.com/'


class CadastroPage(Page):
    url = urljoin(BASE_URL, '/register')
    formulario = FormularioCadastro()


class LoginPage(Page):
    url = urljoin(BASE_URL, '/login')
    formulario = FormularioLogin()


class TodoPage(Page):
    url = urljoin(BASE_URL, '/')
    logout = Logout()
    formulario = FormularioTodo()
    afazer = AFazer()
    fazendo = Fazendo()
    pronto = Pronto()
