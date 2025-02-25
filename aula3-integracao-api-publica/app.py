# Importando o módulo render_template para renderizar o HTML
from flask import Flask, render_template

#Importando o arquivo de rotas
from controllers import routes

# Criando a instância do Flask
# Representa o nome do arquivo, template_folder indica o local das páginas do HTML
app = Flask(__name__, template_folder='views')

routes.init_app(app)

# Iniciando o servidor caso o arquivo executado seja este
if (__name__) == '__main__':
    # host para indicar aonde rodará o servidor / debug para depuração
    app.run(host='localhost', port=5000, debug=True)
