import unittest
import electrodomesticos

class TestElectrodomesticos(unittest.TestCase):
    def test_lavadora_es_instanacia_lavadora(self):
        """Revisa que un objeto lavadora sea instancia de la clase Lavadora"""
        #1.- Crear un objeto de la clase Lavadora
        l = electrodomesticos.Lavadora("LG", "MX102", 20)
        #2.- Hacer un assert que verifique que el objeto creado es instancia de Lavadora
        self.assertIsInstance(l, electrodomesticos.Lavadora)
        self.assertIsInstance(l,electrodomesticos.Electrodomestico)
    
    def test_refrigerador_es_instanacia_refrigerador(self):
        """Revisa que un objeto refrigerador sea instancia de la clase Refrigerador"""
        #1.- Crear un objeto de la clase Refrigerador
        r = electrodomesticos.Refrigerador("Mabe", "R102", 30)
        #2.- Hacer un assert que verifique que el objeto creado es instancia de Refrigerador
        self.assertIsInstance(r, electrodomesticos.Refrigerador)
        self.assertIsInstance(r, electrodomesticos.Electrodomestico)
    
    def test_fabrica_electrodomestico(self):
        """Prueba que esta funcion cree instancias de Electrodomestico"""
        #1.- Crear una lavadora con la función
        l  = electrodomesticos.fabrica_electrodomestico(electrodomesticos.Lavadora,marca="Whirpool",modelo="MX100",capacidad_carga=30)
        #2.- Revisar que el objeto creado sea una instancia Electrodomestico
        self.assertIsInstance(l, electrodomesticos.Electrodomestico)
        
        #1.- Crear una refrigerador con la función
        r  = electrodomesticos.fabrica_electrodomestico(electrodomesticos.Refrigerador,marca="Patito",modelo="RG100",volumen=25)
        #2.- Revisar que el objeto creado sea una instancia Electrodomestico
        self.assertIsInstance(r, electrodomesticos.Electrodomestico)

if __name__ == "__main__":
    unittest.main(verbosity=2)