from unittest.mock import patch
import pytest
from flask import url_for
from aplicacao import bcrypt, app
from aplicacao.forms import FormLogin
from aplicacao.models import Usuario
from aplicacao.routers import login


def test_login():
    # cria uma instância do formulário de login
    form = FormLogin(usuario='user1', senha='password')

    # cria um usuário com as credenciais informadas no formulário
    user = Usuario(usuario='user1', senha=bcrypt.generate_password_hash('password'))

    # mock é a função de busca no banco de dados para retornar o usuário criado acima
    with patch('app.Usuario.query.filter_by') as mock_query:
        mock_query.return_value.first.return_value == user

    # chama a função login com as credenciais informadas no formulário
    with app.test_request_context('/login', method='POST', data=form.data):
        response = login()

    # verifica se o usuário foi autenticado com sucesso
    assert response.status_code == 302
    assert response.location == url_for('produtos', _external=True)