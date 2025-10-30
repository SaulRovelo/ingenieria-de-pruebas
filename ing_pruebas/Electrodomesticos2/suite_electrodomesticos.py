# 📄 Electrodomesticos2/suite_electrodomesticos.py

import unittest
from Electrodomesticos2.test.test_electrodomesticos import TestElectrodomestico
from Electrodomesticos2.test.test_lavadoras import TestLavadora
from Electrodomesticos2.test.test_refrigeradores import TestRefrigerador

def suite_electrodomesticos():
    """Crea una suite que agrupa todas las pruebas de electrodomésticos"""
    test_electro = unittest.defaultTestLoader.loadTestsFromTestCase(TestElectrodomestico)
    test_lavadora = unittest.defaultTestLoader.loadTestsFromTestCase(TestLavadora)
    test_refri = unittest.defaultTestLoader.loadTestsFromTestCase(TestRefrigerador)

    suite = unittest.TestSuite([test_electro, test_lavadora, test_refri])
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite_electrodomesticos())
