from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
#app.config é umdicionário que possui as configurações no flask
#Token gerado no terminal
app.config['SECRET_KEY'] ='5942df07ae250fbcbdfce297e4027e21'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///siteprodutos.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Realize login para prosseguir'
login_manager.login_message_category='alert-info'


#precisa importar depois do app pq o router o utiliza
from aplicacao import routers