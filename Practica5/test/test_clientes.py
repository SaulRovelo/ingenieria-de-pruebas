import unittest
import sqlite3
import os
from src.db_manager import DBManager


class TestClientes(unittest.TestCase):

    @classmethod
    # Preparamos recursos globales 
    def setUpClass(cls):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "data", "tienda_libros.db")  # Ruta a la BD
        
        cls.conn = sqlite3.connect(db_path)     # Conexión a la BD
        cls.cursor = cls.conn.cursor()          # Cursor global para ejecutar SQL
        cls.dbm = DBManager(cls.conn)           # Instancia única de DBManager

    @classmethod
    # Liberamos recursos globales 
    def tearDownClass(cls):
        cls.conn.close()  # Cerramos la conexión

    # Prepara datos antes de cada prueba
    def setUp(self):
        # Datos de prueba que se insertan antes de cada test
        clientes = [("Ana", "ana@example.com"), ("Luis", "luis@example.com")]
        self.ids = []

        # Insertamos clientes sin usar métodos del DBManager
        for nombre, correo in clientes:
            self.cursor.execute(
                "INSERT INTO clientes (nombre, correo) VALUES (?, ?)", 
                (nombre, correo)
            )
            self.ids.append(self.cursor.lastrowid)  # Guardamos IDs generados

        self.conn.commit()  # Confirmamos cambios

    # Limpia los datos después de cada prueba
    def tearDown(self):
        # Eliminamos los clientes insertados en setUp
        for nombre in ["Ana", "Luis"]:
            self.cursor.execute(
                "DELETE FROM clientes WHERE nombre=?", 
                (nombre,)
            )
        self.conn.commit()  # Confirmamos cambios

    # Prueba que get_clientes() devuelva los clientes insertados en setUp
    def test_get_clientes(self):
        resultado = self.dbm.get_clientes()  # Llamamos al método a probar
        nombres = [r[1] for r in resultado]  # Extraemos los nombres devueltos

        # Verificamos que ambos clientes estén en la lista
        for esperado in ["Ana", "Luis"]:
            self.assertIn(esperado, nombres)

    # Prueba que add_cliente() falle si el correo es inválido
    def test_add_cliente_email_invalido(self):
        with self.assertRaisesRegex(ValueError, r"@"):
            self.dbm.add_cliente("Pedro", "correo_invalido")  # Correo sin '@'


if __name__ == "__main__":
    unittest.main()
