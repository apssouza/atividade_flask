from aplicacao import app, db, bcrypt
from aplicacao.models import Usuario, Produtos


'''Criando o banco de dados '''
with app.app_context():
    db.create_all()

'''Inserindo dados com criptografia na tabela usuario'''
with app.app_context():
    senha_crypto = bcrypt.generate_password_hash('123456')
    user = Usuario(usuario = 'admin', email='admin@gmail.com',senha = '123456')
    # Verificando a instância e fazendo o insert com os dados da instância
    db.session.add(user)
    db.session.commit()

'''Inserindo dados na tabela produtos'''
with app.app_context():
    prod = Produtos(nome = 'É Assim que Acaba', tipo='',preco = '35.00')
    db.session.add(prod)
    prod = Produtos(nome = 'Mindset: A nova psicologia do sucesso', tipo='',preco = '45.00')
    db.session.add(prod)
    prod = Produtos(nome='Os sete maridos de Evelyn Hugo ', tipo='', preco='25.00')
    db.session.add(prod)
    prod = Produtos(nome='Jogos vorazes (Trilogia Jogos Vorazes Livro 1)', tipo='', preco='30.00')
    db.session.add(prod)
    prod = Produtos(nome='Alice no País das Maravilhas (Classic Edition)', tipo='', preco='45.00')
    db.session.add(prod)
    db.session.commit()

'''Exibindo todos os produtos cadastrados'''
with app.app_context():
    # pegando todas as linhas da lista (mas não retorna os itens, é preciso criar um for para isso)
    produtos = Produtos.query.all()
    for item in produtos:
        print(f'{item.nome}, {item.tipo}, {item.preco}, {item.id}')

