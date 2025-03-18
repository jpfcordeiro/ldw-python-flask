from flask import redirect, render_template, request, url_for
from models.database import db, Game
import urllib  # Importando a biblioteca urllib para fazer requisições de API
import json

# Criando a primeira rota da aplicação >@decorator sempre em cima da função que está linkada à rota<

# O método route do Flask precisa de uma função

jogadores = []
gamelist = [{'titulo': 'CS-GO', 'ano': 2012, 'categoria': 'FPS Online'}]


def init_app(app):

    @app.route('/')  # Rota principal e sua função logo abaixo
    def home():  # Função para retorno na rota (View Function)
        return render_template('index.html')  # Retorna a página index

    # Rota secundária e sua função logo abaixo

    @app.route('/games', methods=['GET', 'POST'])
    def gamePage():  # Função para retorno na rota
        game = gamelist[0]
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
                return redirect(url_for('gamePage'))
        # Retorna a página games e passando variáveis que serão exibidas na página
        return render_template('games.html', game=game, jogadores=jogadores)

    # Rota para cadastro de jogos aceitando metodos GET e POST
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadGames():

        if request.method == 'POST':
            form_data = request.form.to_dict()
            gamelist.append(form_data)
            return redirect(url_for('cadGames'))
        return render_template('cadgames.html', gamelist=gamelist)

    @app.route('/apigames', methods=['GET', 'POST'])
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None):
        # Fazendo uma requisição de API
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        print(response)
        data = json.loads(response.read())
        if id:
            ginfo = []
            for g in data:
                if g['id'] == id:
                    ginfo = g
                    break
            if ginfo:
                return render_template('gameinfo.html', game=ginfo)
            else:
                return 'Jogo não Encontrado!'
        return render_template('apigames.html', data=data)

    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<int:id>', methods=['GET', 'POST'])
    def estoque(id=None):
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        if request.method == 'POST':
            newgame = Game(request.form['titulo'], request.form['ano'], request.form['categoria'],
                           request.form['plataforma'], request.form['preco'], request.form['quantidade'])
            db.session.add(newgame)
            db.session.commit()
            return redirect(url_for('estoque'))
        else:
            #paginação
            page = request.args.get('page', 1, type=int)
            #Valor padrão de registros por pag
            per_page = 5
            #Faz o select baseado na paginação
            games_page = Game.query.paginate(page=page, per_page=per_page)
            
            # gamesestoque = Game.query.all()
            return render_template('estoque.html', games=games_page)
    
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
        game = Game.query.get(id)
        if request.method == 'POST':
            game.titulo = request.form['titulo']
            game.ano = request.form['ano']
            game.categoria = request.form['categoria']
            game.plataforma = request.form['plataforma']
            game.preco = request.form['preco']
            game.quantidade = request.form['quantidade']
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editgame.html', game=game)
