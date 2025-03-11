# Importando o módulo render_template para renderizar o HTML
from flask import Flask, render_template

#Importando o arquivo de rotas
from controllers import routes

#Instância do SQLAlchemy
from models.database import db
#Importando OS
import os

# Criando a instância do Flask
# Representa o nome do arquivo, template_folder indica o local das páginas do HTML
app = Flask(__name__, template_folder='views')

routes.init_app(app)

#Permite ler o diretório absoluto de um arquivo
dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/game.sqlite3')

#Iniciando o servidor caso o arquivo executado seja este
if (__name__) == '__main__':
    db.init_app(app=app)
    #Cria o banco de dados se não existir
    with app.test_request_context():
        db.create_all()
    
    #host para indicar aonde rodará o servidor / debug para depuração
    app.run(host='0.0.0.0', port=5000, debug=True)
