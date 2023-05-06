from flask import Flask
# Importando a função render_template para trazer o arquivo que eu quero que renderize
# O flask busca diretamente em uma pasta que por padrão deve se chamar templates
#OBS: Chaves duplas serve para substituição de valor e chave prct serve para substituição de comandos no Python
from flask import render_template
#Importando para não quebrar o link (importado do modulo forms)
from aplicacao.forms import FormLogin,FormCadastrarUsuario
from aplicacao import app

if __name__ == '__main__':
    app.run(debug = True)
