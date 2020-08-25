from abc import ABC
from os import environ
from urllib.parse import urlparse

from selenium.webdriver import Remote


def open_browser(hub=None, browser_name=None):
    if hub is None:
        hub = environ.get('HUB_HOST', '127.0.0.1')
        hub = f'http://{hub}:4444/wd/hub'
    if browser_name is None:
        browser_name = environ.get('BROWSER_NAME', 'firefox')

    return Remote(
        command_executor=hub,
        desired_capabilities={'browserName': browser_name},
    )


class SeleniumObject:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)


class Page(ABC):
    url = None

    def __init__(self, webdriver, url=None):
        self.webdriver = webdriver
        if url is not None:
            self.url = url
        self._reflection()

    def open(self):
        if not self.url:
            raise Exception('URL da página não definida')
        self.webdriver.get(self.url)

    def is_in_page(self):
        page = urlparse(self.url)
        browser = urlparse(self.webdriver.current_url)
        return page.path == browser.path

    def _reflection(self):
        for atributo in dir(self):
            atributo_real = getattr(self, atributo)
            if isinstance(atributo_real, PageElement):
                atributo_real.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver
