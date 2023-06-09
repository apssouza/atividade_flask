import pytest
from aplicacao.models import Usuario


def test_cadastro_usuario(client, mocker):
    # Cria um mock do formulário preenchido com informações do usuário
    form = mocker.Mock(
        usuario='user1',
        email='user1@example.com',
        senha='password',
        validate_on_submit=mocker.Mock(return_value=True)
    )

    # Simula a criptografia da senha
    mocker.patch('app.bcrypt.generate_password_hash', return_value='encrypted_password')

    # Simula a adição do usuário no banco de dados
    mock_session = mocker.patch('app.db.session')
    mock_add = mock_session.return_value.add

    # Faz uma requisição POST para o endpoint de cadastro de usuário com o formulário preenchido
    response = client.post('/cadastro-usuario', data=form)

    # Verifica se a resposta da requisição contém um redirecionamento para a página de produtos
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/produtos'

    # Verifica se o usuário foi adicionado corretamente no banco de dados
    mock_add.assert_called_once_with(mocker.Any(Usuario))