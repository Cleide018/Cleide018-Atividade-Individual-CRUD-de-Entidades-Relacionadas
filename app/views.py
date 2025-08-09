from flask import render_template, request, redirect, url_for
from app import app
from app.services.autores_services import AutorService
from app.services.livros_services import LivroService
from app.models.autor import AutorModel
from app.models.livro import LivroModel
from flask import render_template

autor_service = AutorService()
livro_service = LivroService()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/autores')
def index_autores():
    autores = autor_service.listar()
    return render_template('autores/index.html', autores=autores)

@app.route('/autores/novo', methods=['GET', 'POST'])
def novo_autor():
    if request.method == 'POST':
        nome = request.form['nome']
        nacionalidade = request.form['nacionalidade']
        autor_service.adicionar(AutorModel(None, nome, nacionalidade))
        return redirect(url_for('index_autores'))
    return render_template('autores/form.html')

@app.route('/autores/editar/<int:id>', methods=['GET', 'POST'])
def editar_autor(id):
    autor = autor_service.buscar_por_id(id)
    if not autor:
        return redirect(url_for('index_autores'))

    if request.method == 'POST':
        autor_service.atualizar(id, request.form['nome'], request.form['nacionalidade'])
        return redirect(url_for('index_autores'))
    return render_template('autores/form.html', autor=autor)

@app.route('/autores/excluir/<int:id>')
def excluir_autor(id):
    autor_service.remover(id)
    return redirect(url_for('index_autores'))

@app.route('/livros')
def index_livros():
    livros = livro_service.listar()
    return render_template('livros/index.html', livros=livros)

@app.route('/livros/novo', methods=['GET', 'POST'])
def novo_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form.get('genero')
        ano = request.form.get('ano')

        print(f"Valor do ano recebido (antes da conversão): '{ano}' e tipo: {type(ano)}")

        try:
            ano = int(ano)
        except (TypeError, ValueError):
            ano = None

        print(f"Valor do ano após conversão: '{ano}' e tipo: {type(ano)}")

        autor_id = int(request.form['autor_id'])

        livro = LivroModel(None, titulo, genero, ano, autor_id)
        livro_service.adicionar(livro)
        return redirect(url_for('index_livros'))
    return render_template('livros/form.html', autores=autor_service.listar())





@app.route('/livros/editar/<int:id>', methods=['GET', 'POST'])
def editar_livro(id):
    livro = livro_service.buscar_por_id(id)
    if not livro:
        return redirect(url_for('index_livros'))

    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form.get('genero')
        ano = request.form.get('ano')

        print(f"Valor do ano recebido (antes da conversão): '{ano}' e tipo: {type(ano)}")

        try:
            ano = int(ano)
        except (TypeError, ValueError):
            ano = None
        
        print(f"Valor do ano após conversão: '{ano}' e tipo: {type(ano)}")

        autor_id = int(request.form['autor_id'])

        livro_atualizado = LivroModel(id, titulo, genero, ano, autor_id)
        livro_service.atualizar(livro_atualizado)
        return redirect(url_for('index_livros'))

    return render_template('livros/form.html', livro=livro, autores=autor_service.listar())

@app.route('/livros/excluir/<int:id>')
def excluir_livro(id):
    livro_service.remover(id)
    return redirect(url_for('index_livros'))