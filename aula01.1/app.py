from flask import Flask, render_template   #Importando o módulo render_template para renderizar o HTML

#Criando a instância do Flask
app = Flask(__name__, template_folder='views') #Representa o nome do arquivo, template_folder indica o local das páginas do HTML

#Criando a primeira rota da aplicação >@decorator sempre em cima da função que está linkada à rota<

#O método route do Flask precisa de uma função

@app.route('/') #Rota principal e sua função logo abaixo
def home(): #Função para retorno na rota (View Function)
    return render_template('index.html') #Retorna a página index

@app.route('/games') #Rota secundária e sua função logo abaixo
def gamePage(): #Função para retorno na rota
    return render_template('games.html') #Retorna a página games

#Iniciando o servidor caso o arquivo executado seja este
if(__name__) == '__main__':
    app.run(host='localhost', port=5000, debug=True) #host para indicar aonde rodará o servidor / debug para depuração
    
    
