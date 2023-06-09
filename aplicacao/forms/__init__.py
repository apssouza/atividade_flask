from flask_wtf import FlaskForm
#WTForms é uma bbolioteca que possui varios dados de elementos em html, ao instalar flask-wtf vem junto
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.validators import DataRequired, length, email, equal_to


class FormLogin(FlaskForm):
    #validators recebe uma lista de validadores
    usuario = StringField('Usuário', validators=[DataRequired(),length(5,12)])
    senha = PasswordField('Senha', validators=[DataRequired(),length(6,18)])
    submit_entrar = SubmitField('Entrar')

class FormCadastrarUsuario(FlaskForm):
    usuario = StringField('Nome do usuário', validators=[DataRequired(),length(5,12)])
    email = StringField('Email', validators=[DataRequired(),email()])   #Pode ser EmailField ao invés de StringField
    senha = PasswordField('Senha', validators=[DataRequired(),length(6,18)])
    confirmacao = PasswordField('Confirmar senha', validators=[DataRequired(),equal_to('senha')])
    submit_criar = SubmitField('Criar')


class FormCadastrarProduto(FlaskForm):
    nome = StringField('Nome do produto', validators=[DataRequired()])
    tipo = StringField('Tipo do produto')
    preco = FloatField('Preço do produto', validators=[DataRequired()])
    submit_cadastrar = SubmitField('Criar')
    # submit_excluir = SubmitField('Excluir')


# class ConfirmarExclusaoForm(FlaskForm):
#     submit_excluir = SubmitField('Excluir')