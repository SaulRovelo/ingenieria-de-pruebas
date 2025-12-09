import unittest
import sqlite3
import os
from src.db_manager import DBManager


class TestLibros(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Localizamos la base de datos de la misma forma que en las otras clases de prueba
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "data", "tienda_libros.db")

        # La conexión se comparte entre todas las pruebas de esta clase
        cls.conn = sqlite3.connect(db_path)
        cls.cursor = cls.conn.cursor()
        cls.dbm = DBManager(cls.conn)

    @classmethod
    def tearDownClass(cls):
        # Cerramos la conexión una vez que todas las pruebas han concluido
        cls.conn.close()

    def setUp(self):
        # Antes de cada prueba insertamos un libro que sirva como dato de referencia
        self.cursor.execute(
            "INSERT INTO libros (titulo, precio) VALUES (?, ?)",
            ("Libro X", 200)
        )
        self.libro_id = self.cursor.lastrowid
        self.conn.commit()

    def tearDown(self):
        # Luego de cada test eliminamos el libro creado para no dejar datos residuales
        self.cursor.execute("DELETE FROM libros WHERE id=?", (self.libro_id,))
        self.conn.commit()

    def test_get_libros(self):
        # Verificamos que el método recupere el libro agregado en setUp
        resultado = self.dbm.get_libros()
        titulos = [r[1] for r in resultado]
        self.assertIn("Libro X", titulos)

    def test_add_libro_precio_invalido(self):
        # Probamos que un precio no válido genere la excepción esperada
        with self.assertRaisesRegex(ValueError, r"positivo"):
            self.dbm.add_libro("Libro Malo", -10)


if __name__ == "__main__":
    unittest.main()
