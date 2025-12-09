import unittest

from test.test_clientes import TestClientes
from test.testLibros import TestLibros
from test.test_compras import TestCompras



def suite_completa():
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestLibros))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCompras))

    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_completa())
