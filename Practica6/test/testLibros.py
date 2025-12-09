import unittest
from unittest.mock import Mock, call
from src.db_manager import DBManager


class TestLibros(unittest.TestCase):

    def setUp(self):

        # Mock de la conexion
        self.conn = Mock()

        # Mock del cursor
        self.cursor = Mock()

        # La conexion devuelve el cursor mockeado
        self.conn.cursor.return_value = self.cursor

        # Instancia del DBManager usando la conexion mockeada
        self.db = DBManager(self.conn)

    #   test_get_libros

    def test_get_libros(self):

        # llamamos al metodo que debe hacer el SELECT de libros
        self.db.get_libros()

        # Verificamos que se llamo a execute una sola vez
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que el argumento de esa llamada es el SELECT esperado
        llamada_esperada = call('SELECT * FROM libros')
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que se llamo a fetchall una sola vez
        self.assertEqual(self.cursor.fetchall.call_count, 1)

    #   test_delete_libro

    def test_delete_libro(self):

        # Ejecutamos delete_libro con un id de libro
        self.db.delete_libro(7)

        # Verificamos que execute se llamo una vez
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que la sentencia DELETE y el parámetro sean correctos
        llamada_esperada = call(
            'DELETE FROM libros WHERE id=?',
            (7,)
        )
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que commit se llamo exactamente una vez
        self.assertEqual(self.conn.commit.call_count, 1)

    #   test_add_libro_valido

    def test_add_libro_valido(self):

        # Agregamos un libro con un precio válido
        resultado = self.db.add_libro("Clean Code", 350)

        # Verificamos que execute se llamo una sola vez
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que el INSERT y los parámetros sean correctos
        llamada_esperada = call(
            'INSERT INTO libros (titulo, precio) VALUES (?, ?)',
            ("Clean Code", 350)
        )
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que commit se llamo una sola vez
        self.assertEqual(self.conn.commit.call_count, 1)

        # Revisamos que el método devuelva algo (aunque sea un Mock)
        self.assertIsNotNone(resultado)

    #   test_add_libro_invalido

    def test_add_libro_invalido(self):

        # Probamos que lance ValueError con precio inválido
        with self.assertRaises(ValueError):
            self.db.add_libro("Clean Code", -10)

        # Verificamos que nunca se llamo a execute
        self.assertEqual(self.cursor.execute.call_count, 0)

        # Verificamos que nunca se llamo a commit
        self.assertEqual(self.conn.commit.call_count, 0)
