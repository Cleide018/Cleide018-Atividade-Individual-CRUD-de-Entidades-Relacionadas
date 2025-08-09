from app.database.connection import get_db
from app.models.livro import LivroModel

class LivroRepository:

    def get_all_livros(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT l.id, l.titulo, l.genero, l.ano, l.autor_id, a.nome
            FROM livro l
            JOIN autor a ON l.autor_id = a.id
        """)
        rows = cursor.fetchall()
        livros = []
        for row in rows:
            livro = LivroModel(id=row[0], titulo=row[1], genero=row[2], ano=row[3], autor_id=row[4])
            livro.autor_nome = row[5]
            livros.append(livro)
        return livros


    def get_livro_by_id(self, livro_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT l.id, l.titulo, l.genero, l.ano, l.autor_id, a.nome
            FROM livro l
            JOIN autor a ON l.autor_id = a.id
            WHERE l.id=?
        """, (livro_id,))
        row = cursor.fetchone()
        if row:
            livro = LivroModel(id=row[0], titulo=row[1], genero=[2], ano=row[3], autor_id=row[4])
            livro.autor_nome = row[5]
            return livro
        return None


    def create_livro(self, livro):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO livro(titulo, genero, ano, autor_id) VALUES(?, ?, ?, ?)",
            (livro.get_titulo(), livro.get_genero(), livro.get_ano(), livro.get_autor_id())
        )
        connection.commit()

    def update_livro(self, livro):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE livro SET titulo=?, genero=?, ano=?, autor_id=? WHERE id=?",
            (livro.get_titulo(), livro.get_genero(), livro.get_ano(), livro.get_autor_id(), livro.get_id())
        )
        connection.commit()

    def delete_livro(self, livro_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM livro WHERE id=?", (livro_id,))
        connection.commit()

    def get_livros_by_autor(self, autor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM livro WHERE autor_id = ?", (autor_id,))
        return cursor.fetchall()  # lista de livros

