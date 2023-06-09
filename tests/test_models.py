import pytest
from aplicacao import db#, create_app
from aplicacao.models import Usuario, Produtos, Cliente, Pedido


# @pytest.fixture(scope='module')
# def app():
#     app = create_app()
#     app.config['TESTING'] = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.session.remove()
#         db.drop_all()

def test_criar_usuario():
    # cria um usuário para teste
    user = Usuario(usuario="user1", email="user1@example.com", senha="senha")

    # adiciona o usuário ao banco de dados
    db.session.add(user)
    db.session.commit()

    # verifica se o usuário foi adicionado corretamente
    assert user in db.session

def test_criar_produto():
    # cria um produto para teste
    produto = Produtos(nome="produto1", tipo="tipo1", preco=10.0)

    # adiciona o produto ao banco de dados
    db.session.add(produto)
    db.session.commit()

    # verifica se o produto foi adicionado corretamente
    assert produto in db.session


def test_criar_cliente(app):
    with app.app_context():
        # cria um cliente para teste
        cliente = Cliente(nome="cliente1", email="cliente1@example.com")

        # adiciona o cliente ao banco de dados
        db.session.add(cliente)
        db.session.commit()

        # verifica se o cliente foi adicionado com sucesso
        assert Cliente.query.filter_by(nome="cliente1").first() is not None


def test_criar_pedido(app):
    with app.app_context():
        # cria um cliente para teste
        cliente = Cliente(nome="cliente2", email="cliente2@example.com")
        db.session.add(cliente)
        db.session.commit()

        # cria um pedido para teste
        pedido = Pedido(data="2022-05-10", cliente_id=cliente.id)

        # adiciona o pedido ao banco de dados
        db.session.add(pedido)
        db.session.commit()

        # verifica se o pedido foi adicionado com sucesso
        assert Pedido.query.filter_by(data="2022-05-10").first() is not None
