import unittest
from test.test_clientes import TestClientes
from test.test_libros import TestLibros
from test.test_compras import TestCompras

def suite_completa():
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestLibros))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestCompras))
    return suite

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite_completa())
