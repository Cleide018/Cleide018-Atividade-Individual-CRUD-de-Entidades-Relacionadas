from app.models.livro import LivroModel
from app.repository.livros_repository import LivroRepository
from datetime import datetime
from app.repository.autores_repository import AutorRepository

class LivroService:
    def __init__(self):
        self.repo = LivroRepository()
        self.autor_repo = AutorRepository()

    def _validar_ano(self, ano):
        if ano is not None:
            if not isinstance(ano, int):
                raise ValueError("Ano do livro deve ser um número inteiro.")
            if ano <= 0:
                raise ValueError("Ano do livro deve ser um número positivo.")
            if ano < 1450 or ano > datetime.now().year:
                raise ValueError("Ano do livro deve ser entre 1450 e o ano atual.")

    def listar(self):
        return self.repo.get_all_livros()

    def adicionar(self, livro: LivroModel):
        if livro.get_id() is not None:
            raise ValueError("ID do livro deve ser vazio ao criar.")
        if not livro.get_titulo() or livro.get_titulo().strip() == "":
            raise ValueError("Título do livro não pode estar vazio.")
        if livro.get_titulo().isdigit():
            raise ValueError("Título do livro não pode conter apenas números.")

        genero = livro.get_genero() or ""
        if any(char.isdigit() for char in genero):
            raise ValueError("Gênero do livro não pode conter números.")

        self._validar_ano(livro.get_ano())

        if livro.get_autor_id() is None:
            raise ValueError("Autor do livro deve ser informado.")
        autor = self.autor_repo.get_autor_by_id(livro.get_autor_id())
        if autor is None:
            raise ValueError("Autor informado não existe.")
        return self.repo.create_livro(livro)

    def buscar_por_id(self, id):
        if id is None:
            raise ValueError("ID do livro não pode estar vazio.")
        return self.repo.get_livro_by_id(id)

    def atualizar(self, livro: LivroModel):
        if livro.get_id() is None:
            raise ValueError("ID do livro não pode estar vazio para atualização.")
        if not livro.get_titulo() or livro.get_titulo().strip() == "":
            raise ValueError("Título do livro não pode estar vazio.")
        if livro.get_titulo().isdigit():
            raise ValueError("Título do livro não pode conter apenas números.")

        genero = livro.get_genero() or ""
        if any(char.isdigit() for char in genero):
            raise ValueError("Gênero do livro não pode conter números.")

        self._validar_ano(livro.get_ano())

        if livro.get_autor_id() is None:
            raise ValueError("Autor do livro deve ser informado.")
        autor = self.autor_repo.get_autor_by_id(livro.get_autor_id())
        if autor is None:
            raise ValueError("Autor informado não existe.")
        return self.repo.update_livro(livro)

    def remover(self, id):
        if id is None:
            raise ValueError("ID do livro não pode estar vazio para exclusão.")
        return self.repo.delete_livro(id)
