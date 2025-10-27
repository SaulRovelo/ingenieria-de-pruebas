import unittest
from calificaciones_uam.calificaciones_uam import calificacion

class test_calificacion(unittest.TestCase):
    def test_puntaje_invalido_negativo(self):
        """Prueba de puntaje inválido negativo"""
        for i in range (-10, 0):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje),f"Puntaje inválido: {puntaje}")
    
    def test_puntaje_invalido_positivo(self):
        """Prueba de puntaje inválido positivo"""
        for i in range (101, 200):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje),f"Puntaje inválido: {puntaje}")
                
    def test_calificacionA(self):
        """Prueba de calificación A"""
        for i in range(90,101):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "A")
    
    def test_calificacionB(self):
        """Prueba de calificación B"""
        for i in range(75,90):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "B")
    
    def test_calificacionS(self):
        """Prueba de calificación S"""
        for i in range(60,75):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "S")
        
    def test_calificacionNA(self):
        """Prueba de calificación NA"""
        for i in range(0,60):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "NA")

#Ejecutar el codigo
if __name__ == "__main__":
    unittest.main(verbosity=2)