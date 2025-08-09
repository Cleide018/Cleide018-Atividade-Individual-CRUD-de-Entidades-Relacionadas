
# Biblioteca

Um sistema simples e funcional para **gerenciar autores e livros** desenvolvido com **Flask**, **Jinja2** e **SQLite**.  
Permite **listar, cadastrar, editar e excluir** autores e livros de forma prática e direta.

---
# Relacionamento de Entidades
- Um Autor pode escrever vários Livros → 1 para N.

- Um Livro pertence a apenas um Autor → 1 para N.

- Não é possível deletar um autor caso ele tenha um livro associado.

- Não é possível criar um livro sem existir um autor no BD.

---

## Como Rodar o Projeto

### Clonar o Repositório
```bash
git clone https://github.com/Cleide018/Cleide018-Atividade-Individual-CRUD-de-Entidades-Relacionadas.git
cd Cleide018-Atividade-Individual-CRUD-de-Entidades-Relacionadas

```

### Criar Ambiente Virtual
```bash
python -m venv venv
```

Ativar no **Windows**:
```bash
venv\Scripts\activate
```
Ativar no **Linux/Mac**:
```bash
source venv/bin/activate
```

### Instalar Dependências
```bash
pip install --upgrade pip
pip install Flask
```

### Executar o Projeto
```bash
python run.py
```
---

## 📌 Funcionalidades

✅ **Autores**
- Listar autores
- Adicionar autor
- Editar autor
- Excluir autor

✅ **Livros**
- Listar livros com nome do autor
- Adicionar livro
- Editar livro
- Excluir livro


