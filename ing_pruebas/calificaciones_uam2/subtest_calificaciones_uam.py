import unittest
import sys
from calificaciones_uam2.calificaciones_uam import calificacion

class test_calificacion(unittest.TestCase):

    def test_excepcion_tipo_incorrecto(self):
        """Prueba que se lance TypeError si el puntaje no es numérico"""
        with self.assertRaises(TypeError):
            calificacion("9.5")  # tipo str en lugar de float/int

    def test_excepcion_valor_fuera_de_rango(self):
        """Prueba que se lance ValueError si el puntaje está fuera del rango [0,10]"""
        with self.assertRaises(ValueError):
            calificacion(15)  # fuera de rango permitido

    # 🚫 Esta prueba se omite en Windows (solo corre en Linux)
    @unittest.skipIf(sys.platform == "win32", "No se ejecuta en Windows")
    def test_excepcion_valor_fuera_rango_linux(self):
        """Prueba que se lance ValueError fuera de rango (Linux)"""
        with self.assertRaises(ValueError):
            calificacion(15)

    # 🚫 Esta prueba se omite en Linux (solo corre en Windows)
    @unittest.skipIf(sys.platform == "linux", "No se ejecuta en Linux")
    def test_excepcion_valor_fuera_rango_windows(self):
        """Prueba que se lance ValueError fuera de rango (Windows)"""
        with self.assertRaises(ValueError):
            calificacion(15)

#Ejecutar el codigo
if __name__ == "__main__":
    unittest.main(verbosity=2)