import unittest
from unittest.mock import Mock, call
from src.db_manager import DBManager


class TestCompras(unittest.TestCase):

    def setUp(self):

        # Mock de la conexion
        self.conn = Mock()

        # Mock del cursor
        self.cursor = Mock()

        # La conexion devuelve el cursor mockeado
        self.conn.cursor.return_value = self.cursor

        # Instancia del DBManager usando la conexion mockeada
        self.db = DBManager(self.conn)

    #   test_get_comprass

    def test_get_comprass(self):

        # llamamos al metodo que consulta todas las compras
        self.db.get_compras()

        # Verificamos que execute se llamo una sola vez
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que se llamo a fetchall una sola vez
        self.assertEqual(self.cursor.fetchall.call_count, 1)

    #   test_delete_compras

    def test_delete_compras(self):

        # Eliminamos una compra por id
        self.db.delete_compra(3)

        # Verificamos que se llamo una vez a execute
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que la sentencia DELETE y el parametro sean correctos
        llamada_esperada = call(
            'DELETE FROM compras WHERE id=?',
            (3,)
        )
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que commit se llamo una sola vez
        self.assertEqual(self.conn.commit.call_count, 1)

    #   test_registrar_compra_valida

    def test_registrar_compra_valida(self):

        # Simulamos que tanto el cliente como el libro existen en la BD
        # primer fetchone : cliente, segundo fetchone :  libro
        self.cursor.fetchone.side_effect = [True, True]

        # Registramos una compra valida
        resultado = self.db.registrar_compra(1, 2, "2025-01-01")

        # En este flujo se deben hacer 3 execute:
        # 1) SELECT cliente
        # 2) SELECT libro
        # 3) INSERT compra
        self.assertEqual(self.cursor.execute.call_count, 3)

        # Verificamos que se haya hecho commit exactamente una vez
        self.assertEqual(self.conn.commit.call_count, 1)

        # Revisamos que el método devuelva algo (aunque sea Mock)
        self.assertIsNotNone(resultado)

    #   test_registrar_compra_cliente_no_existe

    def test_registrar_compra_cliente_no_existe(self):

        # Simulamos que el cliente NO existe (primer SELECT ya falla)
        self.cursor.fetchone.return_value = None

        # Debe lanzar ValueError por cliente inexistente
        with self.assertRaises(ValueError):
            self.db.registrar_compra(99, 2, "2025-01-01")

        # Solo se debio ejecutar un SELECT (cliente) y nada mas
        self.assertEqual(self.cursor.execute.call_count, 1)

        # No se debe hacer commit porque no se inserto nada
        self.assertEqual(self.conn.commit.call_count, 0)

    #   test_registrar_compra_libro_no_existe

    def test_registrar_compra_libro_no_existe(self):

        # Simulamos: cliente sí existe, libro no existe
        # primer fetchone : True (cliente ok)
        # segundo fetchone : None (libro no encontrado)
        self.cursor.fetchone.side_effect = [True, None]

        # Debe lanzar ValueError por libro inexistente
        with self.assertRaises(ValueError):
            self.db.registrar_compra(1, 999, "2025-01-01")

        # En este caso se hacen 2 execute:
        # 1) SELECT cliente
        # 2) SELECT libro
        self.assertEqual(self.cursor.execute.call_count, 2)

        # No debe haber commit porque no se inserta la compra
        self.assertEqual(self.conn.commit.call_count, 0)
