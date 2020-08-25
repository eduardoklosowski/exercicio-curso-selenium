Exercício do Curso de Selenium
==============================

Exercício do curso de Selenium para o certificado.

- https://dunossauro.github.io/curso-python-selenium/
- https://selenium.dunossauro.live/

Ambiente
--------

Todo o ambiente do selenium foi feito com o `docker-compose`, e pode ser criado com o comando:

```sh
docker-compose up
```

A página http://127.0.0.1:4444/grid/console pode ser verificada para visualizar os navegadores disponíveis no selenium. O firefox pode ser acessado via VNC em `127.0.0.1:5900` com a senha `secret`.

Os testes são executados na máquina local, podendo ser criado através de um virtualenv do python:

```sh
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

Executar os Testes
------------------

Os testes podem ser executador chamando-os como módulos do python, onde a variável de ambiente `BROWSER_NAME` define o navegador, exemplo:

```sh
BROWSER_NAME=firefox python -m tests.test_1_cadastro_cenario1
```

Os testes disponíveis podem ser verificados com:

```sh
ls -1 tests/test_*
```
