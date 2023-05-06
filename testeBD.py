from aplicacao import app, db, bcrypt
from aplicacao.models import Usuario

# o comando precisa do with apra funcionar
'''Cria o banco de dados '''
with app.app_context():
    db.create_all()

'''Inserir dados'''
# with app.app_context():
#     user = Usuario(usuario = 'Administrador', email='administrador@gmail.com',senha = '123456')
#     # Verificando a instância e fazendo o insert com os dados da instância
#     db.session.add(user)
#     db.session.commit()

'''Inserir dados com criptografia'''
with app.app_context():
    senha_crypto = bcrypt.generate_password_hash('123456')
    user = Usuario(usuario = 'admin', email='admin@gmail.com',senha = '123456')
    # Verificando a instância e fazendo o insert com os dados da instância
    db.session.add(user)
    db.session.commit()

'''Realizar um select de umm banco'''
# with app.app_context():
#     # pegando todas as linhas da lista (mas não retorna os itens, é preciso criar um for para isso)
#     usuarios = Usuario.query.all()
#     for item in usuarios:
#         print(f'{item.usuario}, {item.email}, {item.senha}, {item.id}')

'''Apagar usuário'''
# with app.app_context():
#     user = Usuario.query.filter_by(id=2).first()
#     print(user.usuario)
#     # Dentro do () precisa passar o usuário que deseja remover
#     db.session.delete(user)
#     db.session.commit()

'''Apagar o banco de dados'''
# with app.app_context():
#     db.drop_all()