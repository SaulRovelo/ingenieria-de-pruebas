import unittest
import sqlite3
import os
from src.db_manager import DBManager


class TestCompras(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ubicamos la base de datos usando la misma ruta que el resto de pruebas
        base_dir = os.path.dirname(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, "data", "tienda_libros.db")

        # La conexión y el cursor se comparten entre todas las pruebas de esta clase
        cls.conn = sqlite3.connect(db_path)
        cls.cursor = cls.conn.cursor()
        cls.dbm = DBManager(cls.conn)

    @classmethod
    def tearDownClass(cls):
        # Al finalizar toda la clase de pruebas cerramos la conexión
        cls.conn.close()

    def setUp(self):
        # Preparamos un cliente y un libro para cada prueba
        self.cursor.execute(
            "INSERT INTO clientes (nombre, correo) VALUES (?, ?)",
            ("Axel", "a@a.com")
        )
        self.cliente_id = self.cursor.lastrowid

        self.cursor.execute(
            "INSERT INTO libros (titulo, precio) VALUES (?, ?)",
            ("Libro Y", 150)
        )
        self.libro_id = self.cursor.lastrowid

        # Confirmamos los cambios antes de ejecutar el test
        self.conn.commit()

    def tearDown(self):
        # Dejamos limpia la base eliminando lo que se insertó en setUp
        self.cursor.execute("DELETE FROM compras")
        self.cursor.execute("DELETE FROM clientes WHERE id=?", (self.cliente_id,))
        self.cursor.execute("DELETE FROM libros WHERE id=?", (self.libro_id,))
        self.conn.commit()

    def test_registrar_compra_valida(self):
        # Se registra una compra usando los datos preparados en setUp
        compra_id = self.dbm.registrar_compra(
            self.cliente_id,
            self.libro_id,
            "2024-11-01"
        )

        # Después verificamos que realmente quedó registrada
        compras = self.dbm.get_compras()
        self.assertEqual(len(compras), 1)
        self.assertEqual(compras[0][1], "Axel")        # nombre cliente
        self.assertEqual(compras[0][2], "Libro Y")     # título libro
        self.assertEqual(compras[0][3], "2024-11-01")  # fecha

    def test_registrar_compra_cliente_inexistente(self):
        # Intento registrar una compra con un cliente que no existe
        with self.assertRaisesRegex(ValueError, "cliente no existe"):
            self.dbm.registrar_compra(999, self.libro_id, "2024-11-01")

    def test_registrar_compra_libro_inexistente(self):
        # Caso donde el cliente sí existe pero el libro no
        with self.assertRaisesRegex(ValueError, "libro no existe"):
            self.dbm.registrar_compra(self.cliente_id, 999, "2024-11-01")


if __name__ == "__main__":
    unittest.main()
