import unittest
from Electrodomesticos2.src.electrodomesticos import (
    Electrodomestico, Lavadora, Refrigerador, fabrica_electrodomestico
)

class TestElectrodomestico(unittest.TestCase):
    
    def setUp(self):
        """Configura objetos comunes antes de cada prueba"""
        self.lavadora = Lavadora("LG", "TwinWash", 10)
        self.refrigerador = Refrigerador("Samsung", "FamilyHub", 350)
        self.productos = [self.lavadora, self.refrigerador]

    def test_fabrica_varios_electrodomesticos(self):
        """Usa la fábrica para crear objetos y probarlos con subTest"""
        for producto in self.productos:
            with self.subTest(producto=producto):
                self.assertIsInstance(producto, Electrodomestico)
                self.assertIsNotNone(producto.marca)
                self.assertIsNotNone(producto.modelo)

    def test_tipo_incorrecto_refrigerador_marca_modelo(self):
        """Verifica que la marca y el modelo del refrigerador sean strings"""
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Refrigerador(123, "FamilyHub", 350)  # Marca inválida
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Refrigerador("Samsung", 456, 350)    # Modelo inválido


if __name__ == "__main__":
    unittest.main(verbosity=2)
