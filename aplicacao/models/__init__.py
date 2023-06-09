from aplicacao import db, login_manager
# UserMixin tem todos os métodos e atributos necessários para criar uma classe login
from flask_login import UserMixin


# Criar função para procurar um usuário através de um id
# login_manager gerencia o login
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# A classe serve para criar as tabelas através do sqlalchemy
# A classe Model possui um padrão para a criação da tabela
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String, nullable= False)
    email =  db.Column(db.String, nullable= False, unique = True)
    senha = db.Column(db.String, nullable= False)

class Produtos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable= False)
    tipo = db.Column(db.String(200))
    preco = db.Column(db.Float, nullable= False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('pedidos', lazy=True))

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)