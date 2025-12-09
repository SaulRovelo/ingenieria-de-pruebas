import unittest
from unittest.mock import Mock
import sqlite3


class TestConnect(unittest.TestCase):

    def test_llamadas_ordenadas(self):
        """Prueba que sqlite3.connect se llame 3 veces con diferentes argumentos"""

        # 1. Mockear sqlite3.connect
        sqlite3.connect = Mock()

        # 2. Hacer las 3 llamadas:
        sqlite3.connect()                          # sin argumentos
        sqlite3.connect("mi_base.db")              # argumento posicional
        sqlite3.connect(database="mi_base.db")     # argumento nombrado

        # 3. Verificar que se llamó 3 veces
        self.assertEqual(sqlite3.connect.call_count, 3) 


if __name__ == "__main__":
    unittest.main(verbosity=2)
