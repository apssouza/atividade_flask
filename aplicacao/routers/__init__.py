from flask_wtf import form

from aplicacao import app, db, bcrypt
from flask import redirect, render_template, url_for, flash
from aplicacao.forms import FormLogin,FormCadastrarUsuario
from aplicacao.models import Usuario
from flask_login import login_user,logout_user, login_required


@app.route("/", methods=['GET','POST'])
def login():
    #Não precisa criar um construtor pq o FlaskForm já cria
    form = FormLogin()
    if form.validate_on_submit():
        # Fazendo a busca na tabela usuário
        user = Usuario.query.filter_by(usuario = form.usuario.data).first()
        # COmparando se é igual a senha puxada do banco
        if user and bcrypt.check_password_hash(user.senha, form.senha.data):
            login_user(user)
            # flash possui mensagem(exibida quando o login for feito) e categoria (classe que aplica o efeito desejado, nesse caso usamos bootstrap)
            flash(f'Login feito com sucesso para o user: {form.usuario.data}','alert alert-success')
            return redirect(url_for('produtos'))
        else:
            flash(f'Usuário ou senha inválidos','alert alert-danger')

    return render_template('login.html', form = form)

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Sessão encerrada', 'alert alert-info')
    return redirect(url_for('login'))

@app.route("/cadastro-usuario", methods=['GET','POST'])
@login_required
def cadastro_usuario():
    form = FormCadastrarUsuario()
    # verificando se os campos estão preenchidos de acordo com o validador
    if form.validate_on_submit():
        # criptografando a senha para armazenar no banco
        senha_crypto = bcrypt.generate_password_hash(form.senha.data)
        user = Usuario(usuario=form.usuario.data,email = form.email.data, senha = senha_crypto)
        db.session.add(user)
        db.session.commit()
        return redirect('produtos')
    return render_template('cadastrar_usuario.html', form=form)

@app.route("/produtos")
@login_required
def produtos():
    produtos = ['Caneca', 'Caneta', 'Caderno', 'TV', 'Notebook']
    return render_template('lista_produto.html', nomes = produtos)

@app.route('/cadastros')
def cadastros():
    cadastros = [{form.usuario}, {form.email}]
    return render_template('lista_produto.html', nomes=cadastros)