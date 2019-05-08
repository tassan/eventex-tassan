# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/tassan/eventex-tassan.svg?branch=master)](https://travis-ci.org/tassan/eventex-tassan)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea579671ffa945cd84031c493b21a592)](https://www.codacy.com/app/tassan/eventex-tassan?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tassan/eventex-tassan&amp;utm_campaign=Badge_Grade)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.7.3
3. Ative o vitualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/tassan/eventex-tassan.git
cd wttd
python -m venv .wttd
source .wttd/bin/activate (Unix) || .wttd\Scripts\activate.bat (Windows)
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```