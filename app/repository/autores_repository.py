from app.database.connection import get_db
from app.models.autor import AutorModel

class AutorRepository:

    def get_all_autores(self):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM autor")
        rows = cursor.fetchall()
        return [AutorModel(id=row[0], nome=row[1], nacionalidade=row[2]) for row in rows]

    def get_autor_by_id(self, autor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM autor WHERE id=?", (autor_id,))
        row = cursor.fetchone()
        return AutorModel(id=row[0], nome=row[1], nacionalidade=row[2]) if row else None

    def create_autor(self, autor):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO autor(nome, nacionalidade) VALUES(?, ?)",
            (autor.get_nome(), autor.get_nacionalidade())
        )
        connection.commit()

    def update_autor(self, autor):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE autor SET nome=?, nacionalidade=? WHERE id=?",
            (autor.get_nome(), autor.get_nacionalidade(), autor.get_id())
        )
        connection.commit()

    def delete_autor(self, autor_id):
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM autor WHERE id=?", (autor_id,))
        connection.commit()
        
    
