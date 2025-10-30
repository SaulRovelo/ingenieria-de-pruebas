import unittest
from Electrodomesticos2.src.electrodomesticos import (
    Electrodomestico, Lavadora, Refrigerador, fabrica_electrodomestico
)
class TestRefrigerador(unittest.TestCase):

    def setUp(self):
        """Configura varios refrigeradores para las pruebas"""
        self.refrigerador1 = Refrigerador("Samsung", "FamilyHub", 300)
        self.refrigerador2 = Refrigerador("Whirlpool", "WRX735SDHZ", 300)
        self.refrigerador3 = Refrigerador("LG", "InstaView", 300)

    def test_varios_refrigeradores(self):
        """Prueba varios Refrigeradores con subTest"""
        refrigeradores = [self.refrigerador1, self.refrigerador2, self.refrigerador3]
        for refrigerador in refrigeradores:
            with self.subTest(refrigerador=refrigerador):
                self.assertIsInstance(refrigerador, Refrigerador)
                self.assertIsInstance(refrigerador, Electrodomestico)
                self.assertEqual(refrigerador.volumen, 300)
                self.assertIsNotNone(refrigerador.marca)
                self.assertIsNotNone(refrigerador.modelo)

    def test_tipo_incorrecto_marca_o_modelo(self):
        """assertRaisesRegex para marca/modelo no string en Refrigerador"""
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Refrigerador(123, "FamilyHub", 300)     # marca inválida
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Refrigerador("Samsung", 456, 300)       # modelo inválido

if __name__ == "__main__":
    unittest.main(verbosity=2)
