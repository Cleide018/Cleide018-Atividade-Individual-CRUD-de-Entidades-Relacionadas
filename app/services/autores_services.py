from app.models.autor import AutorModel
from app.repository.autores_repository import AutorRepository
from app.repository.livros_repository import LivroRepository

class AutorService:
    def __init__(self):
        self.repo = AutorRepository()
        self.livro_repo = LivroRepository()

    def listar(self):
        return self.repo.get_all_autores()

    def adicionar(self, autor: AutorModel):
        if autor.get_id() is not None:
            raise ValueError("ID do autor deve ser vazio ao criar.")
        if not autor.get_nome() or autor.get_nome().strip() == "":
            raise ValueError("Nome do autor não pode estar vazio.")
        if any(char.isdigit() for char in autor.get_nome()):
            raise ValueError("O nome do autor não pode conter números.")
        if autor.get_nacionalidade() is not None:
            if any(char.isdigit() for char in autor.get_nacionalidade()):
                raise ValueError("Nacionalidade não pode conter números.")
        return self.repo.create_autor(autor)

    def buscar_por_id(self, id):
        if id is None:
            raise ValueError("ID do autor não pode estar vazio.")
        return self.repo.get_autor_by_id(id)

    def atualizar(self, id, nome, nacionalidade):
        if id is None:
            raise ValueError("ID do autor não pode estar vazio para atualização.")
        if not nome or nome.strip() == "":
            raise ValueError("Nome do autor não pode estar vazio.")
        if any(char.isdigit() for char in nome):
            raise ValueError("O nome do autor não pode conter números.")
        if any(char.isdigit() for char in nacionalidade):
            raise ValueError("Nacionalidade não pode conter números.")
        autor = AutorModel(id=id, nome=nome, nacionalidade=nacionalidade)
        return self.repo.update_autor(autor)

    def remover(self, id):
        if id is None:
            raise ValueError("ID do autor não pode estar vazio para exclusão.")
        livros = self.livro_repo.get_livros_by_autor(id)
        if livros:
            raise Exception("Não é possível deletar o autor pois ele possui livros associados.")
        return self.repo.delete_autor(id)