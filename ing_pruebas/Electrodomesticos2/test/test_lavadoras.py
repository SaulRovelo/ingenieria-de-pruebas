import unittest
from Electrodomesticos2.src.electrodomesticos import (
    Electrodomestico, Lavadora, Refrigerador, fabrica_electrodomestico
)

class TestLavadora(unittest.TestCase):

    def setUp(self):
        """Configura varias lavadoras antes de cada prueba"""
        self.lavadora1 = Lavadora("LG", "TwinWash", 10)
        self.lavadora2 = Lavadora("Bosch", "Serie 6", 10)
        self.lavadora3 = Lavadora("Samsung", "AddWash", 10)
        self.lavadoras = [self.lavadora1, self.lavadora2, self.lavadora3]

    def test_varias_lavadoras(self):
        """Prueba varias Lavadoras con subTest"""
        for lavadora in self.lavadoras:
            with self.subTest(lavadora=lavadora):
                self.assertIsInstance(lavadora, Lavadora)
                self.assertIsInstance(lavadora, Electrodomestico)
                self.assertEqual(lavadora.capacidad_carga, 10)
                self.assertIsNotNone(lavadora.marca)
                self.assertIsNotNone(lavadora.modelo)

    def test_tipo_incorrecto_marca_o_modelo(self):
        """assertRaisesRegex para marca/modelo no string en Lavadora"""
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Lavadora(123, "TwinWash", 10)   # Marca inválida
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Lavadora("LG", 999, 10)         # Modelo inválido

if __name__ == "__main__":
    unittest.main(verbosity=2)
