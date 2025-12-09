import unittest
from unittest.mock import Mock, call 
from src.db_manager import DBManager


class TestClientes(unittest.TestCase):

    def setUp(self):

        # Mock de la conexion
        self.conn = Mock()

        # Mock del cursor
        self.cursor = Mock()

        # La conexion devuelve el cursor mockeado
        self.conn.cursor.return_value = self.cursor

        # Instancia del DBManager usando la conexion mockeada
        self.db = DBManager(self.conn)

    
    #   test_get_clientes
    
    def test_get_clientes(self):

        # Llamamos al metodo que queremos probar 
        self.db.get_clientes()

        # Verificamos que se llamo a execute UNA vez
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que el argumento de esa llamada es el SELECT esperado
        llamada_esperada = call('SELECT * FROM clientes')
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que se llamo a fetchall UNA vez
        self.assertEqual(self.cursor.fetchall.call_count, 1)

    
    #   test_delete_cliente
    
    def test_delete_cliente(self):

        # Ejecutamos delete_cliente con un ID específico
        self.db.delete_cliente(5)

        # Verificamos numero de llamadas a execute
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos los ARGUMENTOS con call + call_args_list
        llamada_esperada = call(
            'DELETE FROM clientes WHERE id=?',
            (5,)
        )
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que commit se llamo exactamente una vez
        self.assertEqual(self.conn.commit.call_count, 1)

    
    #   test_add_cliente_valido
    
    def test_add_cliente_valido(self):

        # Insertamos un cliente valido para verificar el flujo completo
        resultado = self.db.add_cliente("Axel", "axel@uam.com")

        # Verificamos cuantas veces se llamo a execute
        self.assertEqual(self.cursor.execute.call_count, 1)

        # Verificamos que la llamada a execute tenga la sentencia y params correctos
        llamada_esperada = call(
            'INSERT INTO clientes (nombre, correo) VALUES (?, ?)',
            ("Axel", "axel@uam.com")
        )
        self.assertIn(
            llamada_esperada,
            self.cursor.execute.call_args_list
        )

        # Verificamos que se llamo a commit un sola vez
        self.assertEqual(self.conn.commit.call_count, 1)

        # Revisamos que devuelva algo
        self.assertIsNotNone(resultado)

    
    #   test_add_cliente_invalido
    
    def test_add_cliente_invalido(self):

        # Probamos que se lance la excepción por correo inválido
        with self.assertRaises(ValueError):
            self.db.add_cliente("Axel", "correo-invalido")

        # Verificamos que nunca se llamo a execute
        self.assertEqual(self.cursor.execute.call_count, 0)

        # Verificamos que nunca se llamo a commit
        self.assertEqual(self.conn.commit.call_count, 0)
